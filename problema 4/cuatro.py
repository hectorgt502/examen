from ast import For, If
from sqlite3 import Cursor
from unittest import result
import psycopg2
import numpy as npobject
import random


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


def guardar (an1, an2,an3,an4,estado):
    cursor=conexion.cursor()
    #nametable = "uno"
   
    cursor.execute("INSERT INTO cuatro(partida,dado1,dado2,resultado,estado) values(%s,%s,%s,%s,%s);",(str(an1),str(an2),str(an3),str(an4),str(estado)))
    conexion.commit()

def historial():

    nhistorial = cursor.execute("SELECT * FROM cuatro;")
    nhistorial = str(cursor.fetchall())


    print(nhistorial+"\n-------------------------------\n")

try:
    #CrearTXT()
    salida=1
    resultado =0
    partida=0

    while salida != 0:
        menu= int( input("Bienvenido\ningrese la opcion que desea realizar \n 1- Iniciar juego \n 2- ver historia \n 0- Salir \n"))
        resultado =0
        mensaje=""

        if menu==1:
           
            

            while resultado !=7:
                print("\n---------------------------------------------\n")
                pausa= input("De enter para lanzar los dados")
                partida=partida+1
                dado1 = random.randint(0,6)
                dado2 = random.randint(0,6)
                resultado= dado1+dado2
                
                salida= "\nEl valor del dado 1 es "+str(dado1)+"\nel valor del dado 2 es "+str(dado2)+"\nEl resultado es "+str(resultado)+"\n"
                print(salida)

                if resultado == 8:
                    print("\n-------------YOU WIN--------------\n Puedes seguir jugando")
                    mensaje="Gano"
                    
                elif resultado == 7:
                    print("\n-------------GAME OVER!!--------------\n")
                    mensaje="Perdio"
                    
                else:
                    mensaje="Sigue jugando"
                    print("Puedes seguir lanzando los dados \n")
                print("\n---------------------------------------------\n")

                guardar(partida,dado1,dado2,resultado,mensaje)


            

       
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
