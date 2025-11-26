mi_archivo= open("mi_archivo.txt", "w", newline='')
mi_archivo.write("\nsegunda línea")
mi_archivo.close()

mi_archivo= open("mi_archivo.txt", "r", newline='')
print(mi_archivo.read())
mi_archivo.close()

opt = 0

while (True):
    print("BIENVENIDO")
    print("1.    Agregar línea\n2.    leer\n3.    borrar\n0.    SALIR")
    opt = int(input("Que desea hacer?"))
    match (opt):
        case 1:
            texto_añadir = str(input("Ingrese la nueva linea: "))
            mi_archivo = open("mi_archivo.txt", "a", newline='')
            mi_archivo.write(texto_añadir+"\n")
            mi_archivo.close()
        case 2:
            mi_archivo= open("mi_archivo.txt")
            print(mi_archivo.read())
            mi_archivo.close()
        case 3:
            print("Se removerá su archivo...")
            mi_archivo = open("mi_archivo.txt", "w", newline='')
            mi_archivo.write('')
            mi_archivo.close

    if opt == 0:
        print("Bye bye")
        break        
                   
from csv import reader, writer, DictReader, DictWriter  

with open("a.csv", "r") as file:
    lector = reader(file)
    for row in lector:
        print(row)



myData = [
    ["firstName","SecondName", "Grade"],
    ["Alex","Godoy","2"],
    ["Carlos","De la Torre","2"],
]        

myFile = open("personas.csv","w", newline='')

with myFile:
    escritor = writer(myFile)
    escritor.writerows(myData)

with open('ventas_semana_pasada.csv') as f:
    DictReader_obj = DictReader(f)
    for item in DictReader_obj:
        print(f"{item['DIA']}, {item['JORNADA1']} ")


def write_reservations(f, reservations, headers):
    with open(f, "w", newline='') as f2:
        writer = DictWriter(f2, fieldnames = headers)
        if headers:
            writer.writeheader()
        for reservation in reservations:
            writer.writerow({
                'availability_zone': reservation["availability_zone"],
                'tenancy': reservation["tenancy"],
                'product': reservation["product"],
                'cost_hourly': reservation["cost_hourly"],
                'cost_upfront': reservation["cost_upfront"],
                'count': reservation["count"],
                'count_used': reservation["count_used"],           
            })   

headers = [
    'availability_zone',
    'tenancy',
    'product',
    'cost_hourly',
    'cost_upfront',
    'count',
    'count_used',
    ]
reservations = [
            {"availability_zone": 2,
                "tenancy": 3,
                'product': 1,
                'cost_hourly': 3500,
                'cost_upfront': 4800,
                "count": 45,
                "count_used": 1
            },{"availability_zone": 3,
                 "tenancy": 3,
                 'product': 4,
                 'cost_hourly': 3700,
                 'cost_upfront': 5800,
                 "count": 25,
                 "count_used": 13
             }]
write_reservations("reservations.csv", reservations, headers)


