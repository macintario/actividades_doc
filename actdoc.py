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
        turno = row[17]
        asi_id = row[28]
        asignatura = row[29]
        hrs_asig = row[30]
        tipo_asig = row[33]
        semestre = row[34]
        id_pa = row[27]
        hrs_base = row[42]
        hrs_interinato = row[41]
        if asi_id != '':
            with open('salida.csv', mode='a') as salida:
                linewrite = csv.writer(salida,delimiter=',')
                linewrite.writerow([pla_id, plantel, nombre_docente, id_docente,horas_min,
                                    horas_max, turno, asi_id, asignatura, hrs_asig, tipo_asig, semestre, id_pa, ' ', hrs_base, hrs_interinato])
print("ok")