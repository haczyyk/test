import json

path = 'gov.json'
with open(path, 'r') as read_file:
    dictionary = json.load(read_file)   #podajemy strumień do pliku
    print(dictionary)
    print(type(dictionary))