with open("miPrimerArchivoPython.txt","w") as archivo:
    archivo.write("Hola!! \nViva John Frusciante")
    
with open("miPrimerArchivoPython.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)
    
