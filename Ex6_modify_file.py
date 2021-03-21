#Edycja/modyfikacja json-ów
#io.UnsupportedOperation: not readable     nie mogę otworzyć w trybie wright bo był stworzony jako tylko read
import json

import json
import pprint           #widok blokowy
pp = pprint.PrettyPrinter(indent=6)

# path = 'gov.json'
# with open(path) as file:
#     dictionary = json.load(file)   #podajemy strumień do pliku

#dodawanie nowego klucza głównego

path = 'gov.json'

politicians = {'politicians': []}   #definicja klucza głównego
n = {'name': 'Marcin', 'surname': 'Kwasik', 'Language': ['PL', 'Eng', 'Fr']}        #definicja nowego polityka
n2 = {'name': 'Sylwek', 'surname': 'Jamik', 'Language': ['PL']}        #definicja nowego polityka


with open(path) as file:
    dictionary = json.load(file)

    #dodawanie nowych kluczy głównych
    dictionary.update(politicians)      #dodanie nowego klucza głównego politicians
    print(dictionary)

    #dodawanie nowego klucza wewnęętrznego do politicians:
    dictionary['politicians'].append(n)       #otwieramy słownik szukamy hasła politicians i do niego dodajemy/append zmienną n czyli polityka
    pp.pprint(dictionary)


    dictionary['politicians'].append(n2)          #możemy u8żywać append bo klucz jest w formacie lista
    pp.pprint(dictionary)

