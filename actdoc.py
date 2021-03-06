import csv
import os



#clean all
os.remove('salida.csv')
with open('salida.csv', mode='a') as salida:
    linewrite = csv.writer(salida, delimiter=',')
    linewrite.writerow(["ID",
	"NOMBRE DE LA UNIDAD ACADÉMICA",
	"nombre_docente",
	"id_docente",
	"horas_min",
	"horas_máx",
	"hrs_nom",
	"TURNO",
	"ID UA",
	"unidad_de_aprendizaje",
	"HORAS UA",
	"TIPO",
	"SEMESTRE_O_NIVEL",
	"ID PA",
	"PROGRAMA ACADÉMICO",
	"hrs_asignadas BASE",
	"hrs_asignadas INTERINATO",
	"id_grupo",
	"id_mod",
	"id_salón",
	"lunes",
	"martes",
	"miércoles",
	"jueves",
	"viernes",
	"sábado",
	"domingo",
	"TOTAL",
	"INGRESO"])
des_hrs_activ = ''
ingreso = ''
cve_act = ''
actividad = ''
lugar = ''
d_lunes = ''
d_martes = ''
d_miercoles = ''
d_jueves = ''
d_viernes = ''
d_sabado = ''
d_domingo = ''
des_hrs_activ = ''
hrs_base = ''
hrs_interinato = ''


def limpia_escalerita():
    des_hrs_activ = ''
    cve_act = ''
    ingreso = ''
    actividad = ''
    lugar = ''
    d_lunes = ''
    d_martes = ''
    d_miercoles = ''
    d_jueves = ''
    d_viernes = ''
    d_sabado = ''
    d_domingo = ''
    des_hrs_activ = ''




def busca_carrera(pla_id, carr_id):
    carrera = 'noencontrada'
    with open('carreras_x_plantel.csv') as catalogo:
        cat = csv.reader(catalogo, delimiter=',')
        for rcat in cat:
            if pla_id == rcat[0]:
                if carr_id == rcat[8]:
                    carrera = rcat[5]
    return carrera



with open('RUAS.csv') as csvfile:
#with open('1016.csv') as csvfile:
    limpia_escalerita()
    act = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in act:
        pla_id = row[11][0:4]
        plantel = row[11][5:]
        nombre_docente = row[7]
        id_docente = row[6]
        horas_min = row[2]
        ingreso = row[1]
        horas_max = row[16]
        turno = row[17]
        asi_id = row[28]
        asignatura = row[29]
        hrs_asig = row[30]
        tipo_asig = row[33]
        semestre = row[34]
        id_pa = row[27]
        #base
        if row[42] != '':
            hrs_base = float(row[42]) + float(row[45])+ float(row[46])+ float(row[47])

        ## interinato
        if row[41] != '':
            hrs_interinato = float(row[41])+float(row[38])+float(row[39])+float(row[40])

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
        hrs_nom = row[86]
## la m'endiga escalerita
        if row[62] != '':
            des_hrs_activ = row[62]
        if row[68] != '':
            cve_act = row[68]
            limpia_escalerita()
        if row[69] != '':
            actividad = row[69]
        if row[70] != '':
            lugar = row[70]
        if row[71] != '':
            d_lunes = row[71]
        if row[72] != '':
            d_martes = row[72]
        if row[73] != '':
            d_miercoles = row[73]
        if row[74] != '':
            d_jueves = row[74]
        if row[75] != '':
            d_viernes = row[75]
        if row[75] != '':
            d_sabado = row[76]
        if row[75] != '':
            d_domingo = row[77]
        des_cic_id = row[80]
        if asi_id != ''  and 'CENTRO DE ESTUDIOS' not in plantel:
            with open('salida.csv', mode='a') as salida:
                linewrite = csv.writer(salida, delimiter=',', quotechar='"')
                linewrite.writerow([pla_id, plantel, nombre_docente, id_docente,horas_min,
                                    horas_max, hrs_nom, turno, asi_id, asignatura, hrs_asig, tipo_asig, semestre, id_pa, busca_carrera(pla_id, id_pa),
                                    hrs_base, hrs_interinato, id_grupo, id_mod, id_salon,
                                    c_lunes, c_martes, c_miercoles, c_jueves, c_viernes, c_sabado, c_domingo, hrs_total, ingreso])
                hrs_base = ''
                hrs_interinato = ''

#        if des_cic_id != '' and actividad != '' and cve_act != '' and 'CENTRO DE ESTUDIOS' not in plantel:
        if des_cic_id != '' and 'CENTRO DE ESTUDIOS' not in plantel:
            with open('salida.csv', mode='a') as salida:
                linewrite = csv.writer(salida, delimiter=',', quotechar='"')
                linewrite.writerow([pla_id, plantel, nombre_docente, id_docente,horas_min,
                                    horas_max, hrs_nom, turno, cve_act, actividad, hrs_asig, tipo_asig, semestre,
                                    id_pa, ' ',
                                    hrs_base,
                                    hrs_interinato,
                                    id_grupo, 'A',
                                    lugar,
                                    d_lunes, d_martes, d_miercoles, d_jueves, d_viernes, d_sabado, d_domingo, des_hrs_activ, ingreso])
                des_hrs_activ = ''
                cve_act = ''
                actividad = ''
                ingreso = ''
                lugar = ''
                d_lunes = ''
                d_martes = ''
                d_miercoles = ''
                d_jueves = ''
                d_viernes = ''
                d_sabado = ''
                d_domingo = ''
                des_hrs_activ = ''
                hrs_base = ''
                hrs_interinato = ''
        if pza_num_emp != '':
            print(pza_num_emp)
            limpia_escalerita()
print("ok")



