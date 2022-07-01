import csv

nombreArchivo = input("Escriba el nombre del archivo")

numeroDni = input("Escriba el numero de DNI")

salida = input("Escriba PANTALLA o CSV")

tipoCheque = input("Escriba EMITIDO o DEPOSITADO")


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


