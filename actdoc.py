import csv
import os
#clean all
os.remove('salida.csv')

with open('1016.csv') as csvfile:
    act = csv.reader(csvfile, delimiter = ',' )
    for row in act:
        pla_id = row[11][0:4]
        plantel = row[11][5:]
        nombre_docente = row[7]
        id_docente = row[6]
        horas_min = row[2]
        horas_max = row[12]
        with open('salida.csv', mode='a') as salida:
            linewrite = csv.writer(salida,delimiter=',')
            linewrite.writerow([pla_id, plantel, nombre_docente, id_docente])
print("ok")