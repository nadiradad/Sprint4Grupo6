from inputs.inputsAsk import nombreArchivo
from fileReading.openCsv import objIterator
from component.alert import alert
import csv

newRenameCsv = alert(nombreArchivo)

value = "csv/" + str(newRenameCsv)

def desectructurarInfo(argument):
    if argument != "csv/None":
        with open(value, encoding='utf-8') as file:
            objCsv = csv.DictReader(file, delimiter=',')
            objIterator(objCsv)
    else:
        print("Vuelve a intentarlo colocando valores validos, Muchas gracias por elegirnos.")

desectructurarInfo(value)