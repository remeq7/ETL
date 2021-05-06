import pandas as pd
import csv
import sqlite3
import time
import datetime


start = time.process_time()


print("wczytywanie unique_tracks.txt")
# # # ścieżka do pliku unique_tracks.txt EDIT
with open('unique_tracks.txt', 'r', encoding='utf-8') as rf:
    with open('unique_tracksComma.csv', 'w', encoding='utf-8') as wf:
        for line in rf:
            cos = ','.join(line.split('<SEP>'))
            wf.write(cos)

print("wczytywanie triplets_sample_20p.txt")
# # ścieżka do pliku triplets_sample_20p.txt EDIT
with open('triplets_sample_20p.txt', 'r', encoding='utf-8') as rf:
    with open('tripletsComma.csv', 'w', encoding='utf-8') as wf:
        for line in rf:
            cos = ','.join(line.split('<SEP>'))
            wf.write(cos)

print("załadowanie do bazy pliku triplets_sample_20p")
# # # wczytywanie do bazy danych sqlitestudio
con = sqlite3.connect("data.db")
cur = con.cursor()

a_file = open("tripletsComma.csv")
rows = csv.reader(a_file)
cur.execute("""CREATE TABLE triplets_sample (
    id_uzytkownika text,
    id_utw text,
    data text
    )""")
cur.executemany("INSERT INTO triplets_sample VALUES (?, ?,?)", rows)

con.commit()
con.close()

print("załadowanie do bazy pliku unique_tracks")
# # wczytywanie do bazy danych sqlitestudio
con = sqlite3.connect("data.db")
cur = con.cursor()

a_file = open("unique_tracksComma.csv")
rows = csv.reader(a_file)
cur.execute("""CREATE TABLE unique_tracks (
    id_wyk text,
    id_utw text,
    artist text,
    title text
    )""")
cur.executemany("INSERT INTO unique_tracks VALUES (?, ?,?,?)", rows)

con.commit()
con.close()

print("LEFT JOIN unique_tracks - triplets_sample")
# LEFT JOIN
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE utts AS
SELECT id_wyk,
triplets_sample.id_utw,
artist,
title,
id_uzytkownika,
data
FROM triplets_sample
LEFT JOIN unique_tracks ON
triplets_sample.id_utw = unique_tracks.id_utw
""")
con.commit()
con.close()

print("usuwanie duplikatow")
# usuwanie duplikatow
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE utts_bezduplikatow
AS
SELECT DISTINCT id_utw, artist,title,id_uzytkownika,data FROM utts
""")
con.commit()
con.close()


print("Artysta z największą liczba odsłuchań: ")
# wyszukiwanie
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("""
SELECT COUNT(artist), artist
FROM utts_bezduplikatow
GROUP BY artist
ORDER BY COUNT(artist) DESC
LIMIT 1
""")

output = cur.fetchall()
for item in output:
    print(item)

print("5 najpopularniejszych utworow: ")
cur.execute("""
SELECT COUNT(id_utw), title
FROM utts_bezduplikatow
GROUP BY id_utw
ORDER BY COUNT(id_utw) DESC
LIMIT 5
""")

output = cur.fetchall()
for item in output:
    print(item)

con.commit()
con.close()


czas = round(time.process_time() - start)

conversion = datetime.timedelta(seconds=czas)
converted_time = str(conversion)
print(converted_time + " min")
