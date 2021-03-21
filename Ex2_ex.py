import json

person = '{"name": "Jacek", "language": ["Eng", "Fr"]}'

person_dict = json.loads(person) #Uwaga na S na końcu

print(person_dict)
print(type(person_dict))
print(person_dict["name"])