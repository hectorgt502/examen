from ast import For, If
from sqlite3 import Cursor
import psycopg2
import numpy as npobject



#####################pgadmin###########################
NameBase = "examen"


#######################################################
try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "7234mandarina",
        dbname = NameBase
    )
    print("conect")
except psycopg2.Error as error:
    print("No se pudo conectar a la base de datos")



cursor=conexion.cursor()


def guardar (an1, an2,an3):
    cursor=conexion.cursor()
    #nametable = "uno"
   
    cursor.execute("INSERT INTO dos(angulo1,angulo2,angulo3) values(%s,%s,%s);",(str(an1),str(an2),str(an3)))
    conexion.commit()

def historial():

    nhistorial = cursor.execute("SELECT * FROM dos;")
    nhistorial = str(cursor.fetchall())


    print(nhistorial+"\n-------------------------------\n")

try:
    #CrearTXT()
    salida=1
   

    while salida != 0:
        menu= int( input("Bienvenido\ningrese la opcion que desea realizar \n 1- ejecutar programa \n 2- ver historia \n 0- Salir \n"))

        if menu==1:
           
            lado1 = float( input("Bienvenido ingrese los datos en grados sexagesimales \n\r Ingrese el angulo 1 \n"))
            lado2 = float( input("\n\r Ingrese el angulo 2 \n"))
         
            lado3 = 180-(lado1+lado2)
            
            
            salida= "\ngrado 1 = "+str(lado1)+"   grado 2 = "+str(lado2)+"   grado 3 = "+str(lado3)+"\n"

            print(salida)
            #EscribirTXT(salida)
            guardar(lado1,lado2,lado3)

       
        elif menu == 0:
            salida=0
            cursor.close()
            conexion.close()
        elif menu == 2:
            historial()
except ValueError:
        print ("¡Porfavor ingrese un numero no una letra!\n")
except ZeroDivisionError:
        print ("¡Se ha realizado una division entre cero! \n")
except :
    print("Error vuelva a intentarlo.") 
