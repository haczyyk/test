from Ex6_modify_file import dictionary          #nasz ex7 wywoła cały program z Ex6 czyli dicionary będzie zmieniony bo najpierw poleci program z Ex6
import json

with open('polish_gov.txt', 'w') as json_file:
    json.dump(dictionary, json_file, indent=6)