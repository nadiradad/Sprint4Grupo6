import csv
from inputs.inputsAsk import numeroDni, salida, tipoCheque
from component.mostrarDatos import imprimirDatosPantalla
from datetime import datetime



def mostrarAlgo(argument):
    for row in argument:
        
        if row["DNI"] == numeroDni and row["Tipo"] == tipoCheque:
            if len(row["NroCheque"]) >= len(set(row["NroCheque"])):
                if salida == "PANTALLA":
                    imprimirDatosPantalla(row)
                elif salida == "CSV":
                    row1 = row["DNI"]
                    row2 = datetime.today().strftime('%Y-%m-%d')
                    print(row2)
                    newfile = open(f"csv/{row1}{row2}.csv","a")
                    writerCSV = csv.writer(newfile)
                    writerCSV.writerow([row["FechaOrigen"], row["FechaPago"], row["Valor"], row["NroCheque"]])
                    print(writerCSV)
            else:
                return print("Error: Valores repetidos en la Base de datos")