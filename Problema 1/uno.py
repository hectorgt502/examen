from ast import For, If
from sqlite3 import Cursor
from tkinter import Menu
import psycopg2
import numpy as npobject
from ast import Str
from datetime import date
from datetime import datetime
from datetime import timedelta






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


def guardar (dia,mes,año,edad,comentario):
    cursor=conexion.cursor()
    #nametable = "uno"
   
    cursor.execute("INSERT INTO uno(dia,mes,año,edad,comentario) values(%s,%s,%s,%s,%s);",(str(dia),str(mes),str(año),str(edad),str(comentario)))
    conexion.commit()

def historial():

    nhistorial = cursor.execute("SELECT * FROM uno;")
    nhistorial = str(cursor.fetchall())


    print(nhistorial+"\n-------------------------------\n")
    # nhistorial = nhistorial[2:nhistorial.find(',')]
    # # print(nhistorial)

    # # print(11,"         ", consultaOperacion(11),"               ",consultaValor1(11),"         ",consultaValor2(11),"         ",consultaResultado(11))

    # print("No.          Operacion             Valor1            Valor2        Resultado\n")
    
    # #print(consultaValor1(1))

    # for i in range(int(nhistorial)):
    #     #print(consultaOperacion(i))

    #     print(i,"         ", consultaOperacion(i),"               ",consultaValor1(i),"         ",consultaValor2(i),"         ",consultaResultado(i))

###################################################################


try:
    
    salida=1
    

    while salida != 0:
        menu= int( input("Bienvenido\ningrese la opcion que desea realizar \n 1- ejecutar programa \n 2- ver historia \n 0- Salir \n"))
        print("-----------------------------------------")

        if menu==1:
            print("-----------------------------------------")
            mensaje=""
            


            año = int( input("\nBienvenido\n\r Ingrese el año\n"))
            mes = int( input("\n\r Ingrese el mes\n"))
            dia = int( input("\n\r Ingrese el dia\n"))



            fecha = datetime.now()
            ingreso = datetime(año, mes, dia)


            edad = int(fecha.year)-año



            if ( (ingreso.day< fecha.day) ):
                if (ingreso.month>=fecha.month):

                    mensaje="aun no cumplio años"
                if (ingreso.month<=fecha.month):
                    mensaje="ya cumplio años"
            elif(  (ingreso.day> fecha.day)    ):
                if (ingreso.month>=fecha.month):
                    mensaje="aun no cumplio años"
                if (ingreso.month<=fecha.month):
                    mensaje="ya cumplio años"
            else:
                if (ingreso.month>fecha.month):
                    mensaje="aun no cumplio años"
                elif (ingreso.month<fecha.month):
                    mensaje="ya cumplio años"
                else:
                    mensaje="hoy es su cumpleaños"



            salida= "DIA: "+str(dia)+ " MES: "+ str(mes)+ " AÑO: "+str(año)+"\nEsta persona cumple "+ str(edad) +" este año y " + mensaje+"\n"

            print(salida)

            guardar(dia,mes,año,edad,mensaje)

       
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
