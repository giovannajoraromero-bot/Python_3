n=(input("Ingrese la contraseña: "))
if "clave" not in n and "123" not in n and 8==len(n):
    print("La contraseña valida es: ",n)
else:
    print("Contraseña invalida")