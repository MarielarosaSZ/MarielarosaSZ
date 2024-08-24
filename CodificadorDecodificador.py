# codificador/decodificador

def Codificar (texto):
    for i in texto:
        valor_ascii = ord(i)
        print (valor_ascii) #para saber si hace bien esta codificación
        binario = bin(valor_ascii)
        print( binario ) #Por qué imprime una b?

def Decodificar(binario):
    texto=""
    if len(binario)%8 == 0:
       palabras_8bit = [binario[i:i+8] for i in range(0, len(binario), 8)]
       print(palabras_8bit)
    else:
       print("No se puede separar en palabras de 8bits")

    for n in range(0, len(palabras_8bit)):
        valor_ascii= int (palabras_8bit[n], 2)
        print(valor_ascii)
        caracter = chr(valor_ascii)
        texto += caracter
    print(texto)

opcion= input("elige 1 para codificar o 2 para decodificar")

if opcion=="1":
    texto=input("Escribe el texo para codificar: ")
    Codificar(texto)
else:
    binario1=input("ingresa un número binario: ")
    Decodificar(binario1)
    
