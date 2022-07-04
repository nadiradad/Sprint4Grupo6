from datetime import datetime

def imprimirDatosPantalla(row):
    print(f' Numero Cheque: {row["NroCheque"]}, Codigo: {row["CodigoBanco"]}, Sucursal: {row["CodigoScurusal"]}, Destino: {row["NumeroCuentaDestino"]}, Valor: {row["Valor"]}, Fecha Origen: {datetime.fromtimestamp(int(row["FechaOrigen"]))}, Fecha Pago: {datetime.fromtimestamp(int(row["FechaPago"]))}, Dni: {row["DNI"]}, Tipo: {row["Tipo"]}, Estado: {row["Estado"]}')