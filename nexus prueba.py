import sys
import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error

Alumnos = {"Hugo" : {}, "Sergio" : {}, "Mario" : {}, "Kevin" : {}, "Alberto" :{}, \
           "Felipe" : {}, "Cristian" : {}, "Luis" : {}, "Angel" : {}, "Adamaris" : {}, \
           "Mariana" : {}, "Elena" : {}, "Cristal" : {}, "Cristina" : {}, "Karla" : {}, \
           "Lizbeth" : {}, "Fernanda" :{}, "Aracely" : {}, "Ilena" : {}, "Norma" : {}, \
           "Janeth": {}, "Erick" :{}, "Daniel" : {}, "Juan" : {}, "Ivan" : {}, \
           "Brenda": {}, "Rubi" : {}, "Kate" : {}, "Alma" : {}, "Gignac" : {}}
  
  
diccionario_materia= {"Programacion" : {}, "Base De Datos": {}, "Creatividad": {}, "Contabilidad" :{}, "Economia" :{}}

y=diccionario_materia.keys()
materiaskeys=pd.DataFrame(y)
x=Alumnos.keys()
Alumnoskeys = pd.DataFrame(x)
framematerias = pd.DataFrame(diccionario_materia)
framealumnos = pd.DataFrame(Alumnoskeys)
concatenacion = pd.concat([framealumnos, framematerias], axis=0)

d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
reprobados=[]
AlumnosDesc=[]
Numero1=0
Numero2=0
Numero3=0
Numero5=0

Proceso=True
while Proceso == True:
    print("1 para ver a los usuarios y sus calificaciones")
    print("2 para subir calificaciones")
    print("3 para ver la estadistica descriptiva de las materias")
    print("4 para ver a los alumnos reprobados")
    print("5 para Exportar")
    print("6 para ver la estadistica descriptiva por alumno")
    print("7 para salir")

    Proceso2= int(input("¿Que quieres realizar?:"))
   
    if Proceso2 == 1:
        print(concatenacion.iloc[:,0])
    
    
    elif Proceso2 == 2:
        for i in range(1):
            try:
                Nombres=Alumnoskeys.iloc[Numero2, 0]
                print(f"Calificación para el alumno {Numero3} en la lista")
                c1= int(input("Dime la calificacion en Base De Datos: "))
                c2= int(input("Dime la calificacion en Contabilidad: "))
                c3= int(input("Dime la calificacion en Creatividad: "))
                c4= int(input("Dime la calificacion en Economia: "))
                c5= int(input("Dime la calificacion en Programacion: "))
                concatenacion.loc[Numero1] = [Nombres, c1, c2, c3, c4, c5]
                if c1 < 70:
                    d1.append((Nombres, c1))
                if c2 < 70:
                    d2.append((Nombres, c2))
                if c3 < 70:
                    d3.append((Nombres, c3))
                if c4 < 70:
                    d4.append((Nombres, c4))
                if c5 < 70:
                    d5.append((Nombres, c5))
                if Nombres in (d1 and d2) or (d1 and d3) or (d1 and d4) or (d1 and d5) or (d2 and d3) or (d2 and d4) or (d2 and d5) or (d3 and d4) or (d3 and d5) or (d4 and d5):
                    reprobados.append(Nombres)
                Numero1 = Numero1+1
                Numero2 = Numero2+1
                Numero3 = Numero3+1
                print(concatenacion)
            except Error as e:
                print(e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")



    elif Proceso2 == 3:
        print(concatenacion.describe())
    
    
    elif Proceso2 == 4:
            print(f"Alumnos con 2 o mas materias reprobadas: {reprobados}")
                
    elif Proceso2 == 5:
        exp=int(input("¿A que archivo quieres exportar? \n 1-CSV \n 2-JSON \n Exportar: "))
        if exp== 1:
            concatenacion.T.to_csv(r'calificaciones.csv', index=True, header=True)
            print("Se ha exportado a CSV con éxito")
        elif exp== 2:
            concatenacion.T.to_json('calificaciones.json', orient="index")
            print("Se ha exportado a JSON con éxito")
        else:
            print("No se ha podido exportar el documento, volviendo al menú")

        
    elif Proceso2 == 6:
        Numero4=0
        Numero5=0
        concatenacion.fillna(0, inplace=True)
        concatenacionT=concatenacion.T
        #Materias
        for i in range(5):
            Nombres2=materiaskeys.iloc[Numero4,0]
            Calif=concatenacion[Nombres2].describe()
            print(f"Estadistica Para {Nombres2}")
            print(Calif)
            Numero4=Numero4+1
        for i in range(1):
            Calif2=concatenacionT.describe()
            Califtodos = Calif2.describe()
            Cal = pd.DataFrame(Califtodos).T
            print("Estadistica por alumno")
            print(Cal)
            Numero5=Numero5+1
        exp2=int(input("¿Cual exportarás? \n 1-Materias \n 2-Alumnos \n Exportar: "))
        if exp2== 1:
            Calif.T.to_json('EstadisticaPorAlumno.json', orient="index")
            print("Se ha exportado a Texto plano con éxito")
        elif exp2== 2:
            Cal.T.to_json('EstadisticaPorAlumno.json', orient="index")
            print("Se ha exportado a texto plano con éxito")
        else:
            print("No se ha podido exportar el documento, volviendo al menú")
        

    elif Proceso2 == 7:
        print("Fin del programa")
        Proceso= False