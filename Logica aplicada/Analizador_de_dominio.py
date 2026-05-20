n=input("Ingrese su correo electronico: ")
if @ in n:
  dominio=n.split("@")^[1]
  print("El dominio del correo es: ",dominio)
else:
  print("Este no es un correo")
