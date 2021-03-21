import json

black_jack = (8, "Q")       #to jest tupla

encoded = json.dumps(black_jack)
decoded = json.loads(encoded)

print(type(black_jack))
print(decoded)
print(type(decoded))

integer = 3
enc_int = json.dumps(integer)
dec_int = json.loads(enc_int)

print(type(dec_int))