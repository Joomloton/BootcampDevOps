'''Ejercicio 3:
Instrucciones: pide al usuario que indique su nombre y su edad. Como mensaje de salida le indicarás qué edad tuvo el año pasado y cuantos años tendrá el siguiente año.
Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años. '''

print("Welcome User")
name = input("What is your name? ")
age = int(input("What is your age? "))
past = age - 1
future = age + 1

print(f"Nice to meet you, {name}, a year ago you had {past} and next year you'll have {future}")
