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
        cve_act = row[68]
        pza_num_emp = row[25]
        id_grupo = row[36]
        id_mod = row[37]
        id_salon = row[60]
        c_lunes = row[49]
        c_martes = row[50]
        c_miercoles = row[51]
        c_jueves = row[52]
        c_viernes = row[53]
        c_sabado = row[54]
        c_domingo = row[55]
        hrs_total = row[44]
## la m'endiga escalerita
        if row[62] != '':
            des_hrs_activ = row[62]

        des_cic_id = row[80]
        if asi_id != '':
            with open('salida.csv', mode='a') as salida:
                linewrite = csv.writer(salida, delimiter=',')
                linewrite.writerow([pla_id, plantel, nombre_docente, id_docente,horas_min,
                                    horas_max, turno, asi_id, asignatura, hrs_asig, tipo_asig, semestre, id_pa, ' ',
                                    hrs_base, hrs_interinato, id_grupo, id_mod, id_salon,
                                    c_lunes, c_martes, c_miercoles, c_jueves, c_viernes, c_sabado, c_domingo, hrs_total])
        if des_cic_id != '':
            print(des_hrs_activ)
        if pza_num_emp != '':
            print(pza_num_emp)
print("ok")