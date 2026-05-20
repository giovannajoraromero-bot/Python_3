while True:
    t=input("Ingrese un texto (para iniciar 'LOG:'y finalizar 'EXIT'): ")
    if t.startswith("EXIT"):
        print("Finalizando")
        break
    elif t.startswith("LOG:"):
        print(t[4:].strip())
    else:
         print("No se reconoce la entrada")