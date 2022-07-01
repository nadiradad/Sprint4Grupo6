import csv

print("Escriba el nombre del archivo")
nombreArchivo = input()
print("Escriba el numero de DNI")
numeroDni = input()
print("Escriba PANTALLA o CSV")
salida = input()
print("Escriba EMITIDO o DEPOSITADO")
tipoCheque = input()


file = open(nombreArchivo,"r")
reader = csv.reader(file)
encabezado = file.readline()
print(encabezado)
for NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
    if DNI == numeroDni:
        if Tipo == tipoCheque:
            if salida == "PANTALLA":
                print(NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado)
            elif salida == "CSV":
                newfile = open("test2.csv","a")
                writerCSV = csv.writer(newfile)
                writerCSV.writerow([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])

file.close()


