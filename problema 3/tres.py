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


def guardar (an1, an2,an3,an4):
    cursor=conexion.cursor()
    #nametable = "uno"
   
    cursor.execute("INSERT INTO tres(numero,centenas,decenas,unidades) values(%s,%s,%s,%s);",(str(an1),str(an2),str(an3),str(an4)))
    conexion.commit()

def historial():

    nhistorial = cursor.execute("SELECT * FROM tres;")
    nhistorial = str(cursor.fetchall())


    print(nhistorial+"\n-------------------------------\n")

try:
    #CrearTXT()
    salida=1
   

    while salida != 0:
        menu= int( input("Bienvenido\ningrese la opcion que desea realizar \n 1- ejecutar programa \n 2- ver historia \n 0- Salir \n"))

        if menu==1:
           
            numero = int (input ('Ingresa el valor de numero: '))
            centenas=(numero%1000-numero%100)//100
            decenas=(numero%100-numero%10)//10
            unidades=numero%10
            
            
            salida= "\ncentenas = "+str(centenas)+"   decenas = "+str(decenas)+"   unidades = "+str(unidades)+"\n"

            print(salida)
            #EscribirTXT(salida)
            guardar(numero,centenas,decenas,unidades)

       
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
