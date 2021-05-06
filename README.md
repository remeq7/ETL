## Libraries:

* pandas
* csv
* sqlite3
* time
* datetime

## Loading data
Loading data from big .txt file and convert to .csv file
```python
with open('triplets_sample_20p.txt', 'r', encoding='utf-8') as rf:
    with open('tripletsComma.csv', 'w', encoding='utf-8') as wf:
        for line in rf:
            cos = ','.join(line.split('<SEP>'))
            wf.write(cos)
```

## Create table and insert data

```python
import sqlite3
con = sqlite3.connect("data.db") #connect to data.db
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

```

## Description

## ENG
By default, the path to unique_tracks.txt and triplets_sample_20p.txt is in the same directory as main.py.

The total data processing time on the Ryzen 5 3600x processor was 14 minutes and 20 seconds.

In case of an error loading unique_tracksComma to the database, delete the last empty line in the unique_tracks.txt file
## PL
Domyślnie ścieżka do plików unique_tracks.txt i triplets_sample_20p.txt znajduje się w tym samym katalogu co plik main.py.

Całkowity czas przetwarzania danych na procesorze Ryzen 5 3600x wyniósł 14 min i 20s.

W przypadku błędu przy wczytywaniu unique_tracksComma do bazy danych należy usunąć ostatnią pustą linijke w pliku unique_tracks.txt
