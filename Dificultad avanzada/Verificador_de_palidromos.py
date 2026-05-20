t=input("Ingrese una palabra o frase: ")
b=t.replace(" ", "").lower()
if b==b[::-1]:
    print("Es palídrimo")
else:
    print("No es palídromo")