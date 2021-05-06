import pandas as pd
import csv
import sqlite3
import time
import datetime



Domyślnie ścieżka do plików unique_tracks.txt i triplets_sample_20p.txt znajduje się w tym samym katalogu co plik main.py. 

Całkowity czas przetwarzania danych na procesorze Ryzen 5 3600x wyniósł 14 min i 20s.

W przypadku błędu przy wczytywaniu unique_tracksComma do bazy danych należy usunąć ostatnią pustą linijke w pliku unique_tracks.txt
