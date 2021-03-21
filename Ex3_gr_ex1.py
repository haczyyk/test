"""Zadanie 1
Z podanego tekstu w formacie json wyciągnij wiek Johna.
{   "name":"John",
    "age":30,
    "city":"New
    York"}
 Wynik wyświetl na ekranie.
"""

import json

dic = {   "name":"John",
    "age":30,
    "city":"New York"}

print(dic["age"])