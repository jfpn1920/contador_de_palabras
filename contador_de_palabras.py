print("--| contador de palabras |--")
texto = input("ingrese un texto: ")
palabras = texto.split()
contador = 0
for palabra in palabras:
    contador += 1
print(f"\nel texto ingresado tiene {contador} palabra(s).")