'''

jsony - sia podobne do słowników posiadają klucz i wartość np.:

dictionary = {
    'klucz' : 'wartosc'
    lub też wartości:
    'wiele' : [1,2,3]
    'język' : ['pl', 'eng', 'de']
    lub posiadać słowniki wewnętrzne:
    'uczestnicy': [
        {'name' : 'Ada', 'age', : 18},

        {'name': 'artur', high': 190}
    ]
}

odwołąnie się do wieku Ady:

print(dictionary['uczestnicy'][0]['age'])

1. otwarcie słownika
2. szukamy uczestnicy
3. wskazujemy pierwszy name czyli Ada
4. odołanie do parametru age

odwołanie do klucza:
print(dictionary['klucz'])

'''

#json:

import json

#tworzymy słwonik z wieloma wartościami
data = {
    'president': {
        'name' : 'Andrzej',
        'surname' : 'Kaczka',
        'country' : 'Polska'
    }
}

#zapisujemy do pliku

with open('president.json', 'w') as write_file:
    json.dump(data, write_file, indent=4) #zmieniamy słownik na json podajemy mu słownik nasz stworzony oraz plik do zapisu indent zmienia wyświetlanie
                                    # jsona na taki jak tworzyliśmy słownik wcześniej liczba podaje ilośc wcięc "Tabów" w wynikowym jsonie najbezpieczniej jest podać 4

# json.dumps(data)        #Dumps zwraca json do zmiennej a nie pliku
print(json.dumps(data, indent=2))
#
#
# print(json.dumps(data, indent=2, separators=(';', '!')))


print(json.dumps(data, indent=2, separators=(';', '!'), sort_keys=True))