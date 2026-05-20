n=input("Ingrese el nombre de la organizacion: ")
om=["de", "la", "del", "y", "en", "los", "las"]
s= "".join([palabra[0].upper() for palabra in n.split() if palabra.lower() not in om])
print("Las siglas de la organizacion es: ",s)