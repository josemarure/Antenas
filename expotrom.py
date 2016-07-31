#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import sqlite3

print("\t\t\t\t--------")
print("\t\t\t\tEXPOTRON")
print("\t\t\t\t--------\n")

def menu():
    def nosotros():
        print("-----------------------")
        print("Que es el Expotron ?")
        print("-----------------------\n")
        print("El EXPOTRON es uno de los eventos de robótica más grandes a nivel nacional, que se encarga de fomentar la investigación y el desarrollo tecnológico en nuestro país. Este evento año tras año reúne a decenas de estudiantes de distintas parte del Perú y, para que en 3 días demuestren sus habilidades y destrezas en temas de robótica y automatización en los concursos.")
        input("Presione 'Enter'\\\\\\\\\\\\\\\\\\")
        print("-----------------------")
        print("Quienes somos ?")
        print("-----------------------\n")
        print("Este evento está organizado por la Rama Estudiantil IEEE-UNSA, y la Escuela Profesional de Ingeniería Electrónica (EPIE) de la Universidad Nacional de San Agustín.")
        input("Presione 'Enter'\\\\\\\\\\\\\\\\\\")
        print("-----------------------")
        print("Donde se realizara ?")
        print("-----------------------\n")
        print("Loza Deportiva de la Escuela Profesional de Ingeniería Electrónica")
        input("Presione 'Enter' para regresar al MENU \\\\\\\\\\\\\\\\\\")
        menu()
    def inscripcion():
        def feria():
            print()
            print("Opciones:")
            print()
            print("(1)....Inscritos ")
            print("(2)....Inscribirse ")
            print()
            k=int(input("Escoja opcion: "))
            if k==1:
                print("Registro")
                print()
                archivo=open("regis")
                print(archivo.read())
                j=input("digite 's' para salir: ")
                if j.lower()=='s':
                    inscripcion()
                  

            elif k==2:
                print("Llene los siguientes datos ...Para reservar su stand...")
                print("==================================")
            
                archivo=open("regis")
            
                nempresa=input("Nombre de la empresa : ")
                nombre=input("Nombre :")
                apellidos=input("Apellidos :")
                dni=input("DNI : ")
                telefono=input("Telefono :")
                correo=input("Correo electronico : ")
                descripcion=input("Descripcion breve de que dara a conocer : ")

                input("UD. se registro con exito...")

                archivo.write("EMPRESA: ")
                archivo.write(nempresa)
                archivo.write("\n")
                archivo.write("NOMBRE: ")
                archivo.write(nombre)
                archivo.write("\n")
                archivo.write("APELLIDOS: ")
                archivo.write(apellidos)
                archivo.write("\n")
                archivo.write("DNI: ")
                archivo.write(dni)
                archivo.write("\n")
                archivo.write("TELEFONO: ")
                archivo.write(telefono)
                archivo.write("\n")
                archivo.write("CORREO:")
                archivo.write(correo)
                archivo.write("\n")
                archivo.write("DESCRIPCION: ")
                archivo.write(descripcion)
                archivo.write("\n")
                archivo.write("\n")

                archivo.close()
                inscripcion()

        def taller():
            print()
            print("Opciones:")
            print()
            print("(1)....Inscritos ")
            print("(2)....Inscribirse ")
            print()
            k=int(input("Escoja opcion: "))
            if k==1:
                print("Registro")
                print()
                archivo=open("TALLER")
                print(archivo.read())
                print()
                j=input("digite 's' para salir: ")
                if j.lower()=='s':
                    print()
                    inscripcion()
            elif k==2:
                archivo=open("TALLER","a")
                print("Llene los siguientes datos ...Para reservar su stand...")
                print("==================================")
                ntaller=input("Nombre del taller : ")
                nombre=input("Nombre : ")
                apellidos=input("Apellidos :")
                dni=input("DNI : ")
                telefono=input("Telefono :")
                correo=input("Correo electronico : ")
                descripcion=input("Descripcion breve del taller : ")

                archivo.write("TALLER: ")
                archivo.write(ntaller)
                archivo.write("\n")
                archivo.write("NOMBRE: ")
                archivo.write(nombre)
                archivo.write("\n")
                archivo.write("APELLIDOS: ")
                archivo.write(apellidos)
                archivo.write("\n")
                archivo.write("DNI: ")
                archivo.write(dni)
                archivo.write("\n")
                archivo.write("TELEFONO: ")
                archivo.write(telefono)
                archivo.write("\n")
                archivo.write("CORREO:")
                archivo.write(correo)
                archivo.write("\n")
                archivo.write("DESCRIPCION: ")
                archivo.write(descripcion)
                archivo.write("\n")
                archivo.write("\n")

                archivo.close()
                inscripcion()

        def proyectos():
            print()
            print("Opciones:")
            print()
            print("(1)....Inscritos ")
            print("(2)....Inscribirse ")
            print()
            k=int(input("Escoja opcion: "))
            if k==1:
                print("Registro")
                print()
                archivo=open("PROYECTOS")
                print(archivo.read())
                print()
                j=input("digite 's' para salir: ")
                if j.lower()=='s':
                    print()
                    inscripcion()

            elif k==2:
                archivo.open("PROYECTOS")
                print("Llene los siguientes datos ...Para exponer su proyecto...")
                print("==================================")
                nproyecto=input("Nombre del proyecto : ")
                nombre=input("Nombre : ")
                apellidos=input("Apellidos :")
                dni=input("DNI : ")
                telefono=input("Telefono :")
                correo=input("Correo electronico : ")
                descripcion=input("Descripcion breve del proyecto : ")

                input("UD. se registro con exito...")

                archivo.write("PROYECTO: ")
                archivo.write(nproyecto)
                archivo.write("\n")
                archivo.write("NOMBRE: ")
                archivo.write(nombre)
                archivo.write("\n")
                archivo.write("APELLIDOS: ")
                archivo.write(apellidos)
                archivo.write("\n")
                archivo.write("DNI: ")
                archivo.write(dni)
                archivo.write("\n")
                archivo.write("TELEFONO: ")
                archivo.write(telefono)
                archivo.write("\n")
                archivo.write("CORREO:")
                archivo.write(correo)
                archivo.write("\n")
                archivo.write("DESCRIPCION: ")
                archivo.write(descripcion)
                archivo.write("\n")
                archivo.write("\n")

                archivo.close()
                inscripcion()

        def competencias():
            def segvel():
                print()
                print("Opciones:")
                print()
                print("(1)....Inscritos ")
                print("(2)....Inscribirse ")
                print()
                k=int(input("Escoja opcion: "))
                if k==1:
                    print("Registro")
                    print()
                    archivo=open("SEGVEL")
                    print(archivo.read())
                    print()
                    j=input("digite 's' para salir: ")
                    if j.lower()=='s':
                        print()
                        competencias()

                elif k==2:
                    archivo.open("SEGVEL")
                    print("Llene los siguientes datos ...Para inscribir su seguidor/velocista...")
                    print("==================================")
                    print("/t/tDatos del Participante ")
                    print("==================================")
                    nombre=input("Nombre : ")
                    apellidos=input("Apellidos :")
                    dni=input("DNI : ")
                    telefono=input("Telefono :")
                    correo=input("Correo electronico : ")
                    print("==================================")
                    print("/t/tDatos del Seguidor/Velocista  ")
                    print("==================================")
                    nomrobot=input("Nombre del S/V :")
                    colorbot=input("Color del S/V :")
                    materialbot=input("Material del S/V :")
                    pesobot=input("Peso del S/V :")

                    input("UD. se registro con exito ...")

                    archivo.write("DATOS DEL PARTICIPANTE: ")
                    archivo.write("\n")
                    archivo.write("NOMBRE: ")
                    archivo.write(nombre)
                    archivo.write("\n")
                    archivo.write("APELLIDOS: ")
                    archivo.write(apellidos)
                    archivo.write("\n")
                    archivo.write("DNI: ")
                    archivo.write(dni)
                    archivo.write("\n")
                    archivo.write("TELEFONO: ")
                    archivo.write(telefono)
                    archivo.write("\n")
                    archivo.write("CORREO:")
                    archivo.write(correo)
                    archivo.write("\n")
                    archivo.write("DATOS DEL SEGUIDOR/VELOCISTA ")
                    archivo.write("NOMBRE: ")
                    archivo.write(nomrobot)
                    archivo.write("\n")
                    archivo.write("MATERIAL: ")
                    archivo.write(materialbot)
                    archivo.write("\n")
                    archivo.write("PESO: ")
                    archivo.write(pesobot)
                    archivo.write("\n")
                    archivo.write("COLOR: ")
                    archivo.write(colorbot)
                    archivo.write("\n")
                    archivo.write("\n")
                  

                    archivo.close()
                    competencias()
                    
            def minisumos():
                def medio():
                    print()
                    print("Opciones:")
                    print()
                    print("(1)....Inscritos ")
                    print("(2)....Inscribirse ")
                    print()
                    k=int(input("Escoja opcion: "))
                    if k==1:
                        print("Registro")
                        print()
                        archivo=open("MEDIO")
                        print(archivo.read())
                        print()
                        j=input("digite 's' para salir: ")
                        if j.lower()=='s':
                            print()
                            minisumos()

                    elif k==2:
                        archivo.open("MEDIO")
                        print("Llene los siguientes datos ...Para exponer su minisumo...")
                        print("==================================")
                        print("/t/tDatos del Participante ")
                        print("==================================")
                        nombre=input("Nombre : ")
                        apellidos=input("Apellidos :")
                        dni=input("DNI : ")
                        telefono=input("Telefono :")
                        correo=input("Correo electronico : ")
                        print("==================================")
                        print("/t/tDatos del minisumo  ")
                        print("==================================")
                        nomsumo=input("Nombre del minisumo:")
                        colorsumo=input("Color del minisumo :")
                        matsumo=input("Material del minisumo :")
                        pesosumo=input("Peso del minisumo :")

                        input("UD. se registro con exito ...")

                        archivo.write("DATOS DEL PARTICIPANTE: ")
                        archivo.write("\n")
                        archivo.write("NOMBRE: ")
                        archivo.write(nombre)
                        archivo.write("\n")
                        archivo.write("APELLIDOS: ")
                        archivo.write(apellidos)
                        archivo.write("\n")
                        archivo.write("DNI: ")
                        archivo.write(dni)
                        archivo.write("\n")
                        archivo.write("TELEFONO: ")
                        archivo.write(telefono)
                        archivo.write("\n")
                        archivo.write("CORREO:")
                        archivo.write(correo)
                        archivo.write("\n")
                        archivo.write("DATOS DEL MINISUMO ")
                        archivo.write("NOMBRE: ")
                        archivo.write(nomsumo)
                        archivo.write("\n")
                        archivo.write("MATERIAL: ")
                        archivo.write(matsumo)
                        archivo.write("\n")
                        archivo.write("PESO: ")
                        archivo.write(pesosumo)
                        archivo.write("\n")
                        archivo.write("COLOR: ")
                        archivo.write(colorsumo)
                        archivo.write("\n")
                        archivo.write("\n")
                  
                        archivo.close()
                        minisumos()
                        
                def tres():
                    print()
                    print("Opciones:")
                    print()
                    print("(1)....Inscritos ")
                    print("(2)....Inscribirse ")
                    print()
                    k=int(input("Escoja opcion: "))
                    if k==1:
                        print("Registro")
                        print()
                        archivo=open("TRES")
                        print(archivo.read())
                        print()
                        j=input("digite 's' para salir: ")
                        if j.lower()=='s':
                            print()
                            minisumos()

                    elif k==2:
                        archivo.open("TRES")
                        print("Llene los siguientes datos ...Para inscribir su minisumo ...")
                        print("==================================")
                        print("/t/tDatos del Participante ")
                        print("==================================")
                        nombre=input("Nombre : ")
                        apellidos=input("Apellidos :")
                        dni=input("DNI : ")
                        telefono=input("Telefono :")
                        correo=input("Correo electronico : ")
                        print("==================================")
                        print("/t/tDatos del Minisumo  ")
                        print("==================================")
                        nomsumo=input("Nombre del minisumo :")
                        colorsumo=input("Color del S/V :")
                        matsumo=input("Material del minisumo :")
                        pesosumo=input("Peso del minisumo :")

                        input("UD. se registro con exito ...")

                        archivo.write("DATOS DEL PARTICIPANTE: ")
                        archivo.write("\n")
                        archivo.write("NOMBRE: ")
                        archivo.write(nombre)
                        archivo.write("\n")
                        archivo.write("APELLIDOS: ")
                        archivo.write(apellidos)
                        archivo.write("\n")
                        archivo.write("DNI: ")
                        archivo.write(dni)
                        archivo.write("\n")
                        archivo.write("TELEFONO: ")
                        archivo.write(telefono)
                        archivo.write("\n")
                        archivo.write("CORREO:")
                        archivo.write(correo)
                        archivo.write("\n")
                        archivo.write("DATOS DEL MINISUMO ")
                        archivo.write("NOMBRE: ")
                        archivo.write(nomsumo)
                        archivo.write("\n")
                        archivo.write("MATERIAL: ")
                        archivo.write(matsumo)
                        archivo.write("\n")
                        archivo.write("PESO: ")
                        archivo.write(pesosumo)
                        archivo.write("\n")
                        archivo.write("COLOR: ")
                        archivo.write(colorsumo)
                        archivo.write("\n")
                        archivo.write("\n")
                  
                        archivo.close()
                        minisumos()

                print("\n//////////CATEGORIAS///////////\n")
                print("-------------------------------")
                print("\t (1) 500 gr. ")
                print("-------------------------------")
                print("\t (2) 3 kgr. ")
                print("-------------------------------")
                print("\t (3) Volver al menu de competencias ")
                print("-------------------------------")
                deci=int(input("Digite una opcion del MENU DE COMPETENCIAS "))
                if deci==1:
                    medio()
                elif deci==2:
                    tres()
                elif deci==3:
                    input("Presione 'Enter' para regresar al menu")
                    competencias()
                else:
                    input("Digite una opcion valida ...")
                    minisumos()
            def mirosoft():
                print()
                print("Opciones:")
                print()
                print("(1)....Inscritos ")
                print("(2)....Inscribirse ")
                print()
                k=int(input("Escoja opcion: "))
                if k==1:
                    print("Registro")
                    print()
                    archivo=open("MIROSOFT")
                    print(archivo.read())
                    print()
                    j=input("digite 's' para salir: ")
                    if j.lower()=='s':
                        print()
                        competencias()

                elif k==2:
                    archivo.open("MIROSOFT")
                    print("Llene los siguientes datos ...Para inscribir su robot(misoft)...")
                    print("==================================")
                    print("/t/tDatos del Participante ")
                    print("==================================")
                    nombre=input("Nombre : ")
                    apellidos=input("Apellidos :")
                    dni=input("DNI : ")
                    telefono=input("Telefono :")
                    correo=input("Correo electronico : ")
                    print("==================================")
                    print("/t/tDatos del Mirosoft  ")
                    print("==================================")
                    nomsoft1=input("Nombre del mirosoft 1 :")
                    nomsoft2=input("Nombre del mirosoft 2 :")
                    colsoft=input("Color de los mirosofts  :")
                    materialsoft=input("Material de los mirosofts :")
                    pesosoft1=input("Peso del mirosoft 1 :")
                    pesosoft2=input("Peso del mirosoft 2 :")

                    input("UD. se registro con exito ...")

                    archivo.write("DATOS DEL PARTICIPANTE: ")
                    archivo.write("\n")
                    archivo.write("NOMBRE: ")
                    archivo.write(nombre)
                    archivo.write("\n")
                    archivo.write("APELLIDOS: ")
                    archivo.write(apellidos)
                    archivo.write("\n")
                    archivo.write("DNI: ")
                    archivo.write(dni)
                    archivo.write("\n")
                    archivo.write("TELEFONO: ")
                    archivo.write(telefono)
                    archivo.write("\n")
                    archivo.write("CORREO:")
                    archivo.write(correo)
                    archivo.write("\n")
                    archivo.write("DATOS DEL SEGUIDOR/VELOCISTA ")
                    archivo.write("NOMBRE MIROSOFT 1: ")
                    archivo.write(nomsoft1)
                    archivo.write("\n")
                    archivo.write("NOMBRE MIROSOFT 2: ")
                    archivo.write(nomsoft2)
                    archivo.write("\n")
                    archivo.write("MATERIAL DE MIROSOFTS: ")
                    archivo.write(materialsoft)
                    archivo.write("\n")
                    archivo.write("PESO MIROSOFT 1: ")
                    archivo.write(pesosoft1)
                    archivo.write("\n")
                    archivo.write("PESO MIROSOFT 2: ")
                    archivo.write(pesosoft2)
                    archivo.write("\n")
                    archivo.write("COLOR DE MIROSOFTS: ")
                    archivo.write(colsoft)
                    archivo.write("\n")
                    archivo.write("\n")
                  
                    archivo.close()
                    competencias()
            print("\n//////////COMPETENCIAS///////////\n")
            print("-------------------------------")
            print("\t (1) Seguidores y Velocistas ")
            print("-------------------------------")
            print("\t (2) Minisumos ")
            print("-------------------------------")
            print("\t (3) Mirosoft ")
            print("-------------------------------")
            print("\t (4) Volver al MENU DE INSCRIPCIONES ")
            print("-------------------------------")
            opci=int(input("Digite una opcion del MENU DE COMPETENCIAS "))
            if opci==1:
                segvel()
            elif opci==2:
                minisumos()
            elif opci==3:
                mirosoft()
            elif opci==4:
                input("Presione 'Enter' para regresar al MENU DE INSCRIPCIONES")
                inscripcion()
            else:
                input("Digite una opcion valida ...")
                competencias()
        def warbots():
            print()
            print("Opciones:")
            print()
            print("(1)....Inscritos ")
            print("(2)....Inscribirse ")
            print()
            k=int(input("Escoja opcion: "))
            if k==1:
                print("Registro")
                print()
                archivo=open("WARBOOTS")
                print(archivo.read())
                print()
                j=input("digite 's' para salir: ")
                if j.lower()=='s':
                    print()
                    inscripcion()

            elif k==2:
                archivo.open("WARBOOTS")
                print("Llene los siguientes datos ...Para inscribir su warbot...")
                print("==================================")
                print("/t/tDatos del Participante ")
                print("==================================")
                nombre=input("Nombre : ")
                apellidos=input("Apellidos :")
                dni=input("DNI : ")
                telefono=input("Telefono :")
                correo=input("Correo electronico : ")
                print("==================================")
                print("/t/tDatos del Warbot  ")
                print("==================================")
                nomwarbot=input("Nombre del Warbot  :")
                matwarbot=input("Material Warbot :")
                pesowarbot=input("Peso del Warbot :")
                asistentes=input("Numero de Asistentes :")

                input("UD. se registro con exito ...")

                archivo.write("DATOS DEL PARTICIPANTE")
                archivo.write("\n")
                archivo.write("NOMBRE: ")
                archivo.write(nombre)
                archivo.write("\n")
                archivo.write("APELLIDOS: ")
                archivo.write(apellidos)
                archivo.write("\n")
                archivo.write("DNI: ")
                archivo.write(dni)
                archivo.write("\n")
                archivo.write("TELEFONO: ")
                archivo.write(telefono)
                archivo.write("\n")
                archivo.write("CORREO:")
                archivo.write(correo)
                archivo.write("\n")
                archivo.write("DATOS DEL WARBOT")
                archivo.write("NOMBRE: ")
                archivo.write(nomwarbot)
                archivo.write("\n")
                archivo.write("MATERIAL: ")
                archivo.write(matwarbot)
                archivo.write("\n")
                archivo.write("PESO: ")
                archivo.write(pesowarbot)
                archivo.write("\n")
                archivo.write("ASISTENTES: ")
                archivo.write(asistentes)
                archivo.write("\n")
                archivo.write("\n")
                
                archivo.close()
                inscripcion()

        print("\n//////////INSCRIPCIONES ///////////\n")
        print("-------------------------------")
        print("\t (1) Feria de Tecnologia ")
        print("-------------------------------")
        print("\t (2) Talleres ")
        print("-------------------------------")
        print("\t (3) Proyectos ")
        print("-------------------------------")
        print("\t (4) Competencias ")
        print("-------------------------------")
        print("\t (5) WARBOTS ")
        print("-------------------------------")
        print("\t (6) Volver al MENU PRINCIPAL ")
        print("-------------------------------")
        opci=int(input("Digite una opcion del MENU DE INSCRIPCIONES "))
        if opci==1:
            feria()
        elif opci==2:
            taller()
        elif opci==3:
            proyectos()
        elif opci==4:
            competencias()
        elif opci==5:
            warbots()
        elif opci==6:
            input("Presione 'Enter' para regresar al MENU PRINCIPAL ")
            menu()
        else:
            input("Digite una opcion valida ...")
            inscripcion()
    def cronograma():

        def primero():
            print("--------------------------------------------------------------------------")
            print("(9:00-10:00)  |                      Inaguracion                         |")
            print("--------------------------------------------------------------------------")
            print("(10:00-11:00) | Feria de Tecnologia |     Tuenti      |                  |")
            print("--------------------------------------------------------------------------")
            print("(11:00-12:00) | Feria de Tecnologia |  Larvic -UCSP   |  CARRERAS KIDS   |")
            print("--------------------------------------------------------------------------")
            print("(12:00-13:00) | Feria de Tecnologia |      YURA       | SEGUIDOR JUNIOR  |")
            print("--------------------------------------------------------------------------")
            print("(13:00-14:00) | Feria de Tecnologia |   Hackerspace   |   SCRATCH        |")
            print("--------------------------------------------------------------------------")
            print("(14:00-15:00) | Feria de Tecnologia |      Entel      |   RECICLAJE      |")
            print("--------------------------------------------------------------------------")
            print("(15:00-16:00) |   Taller Arduino    |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("(16:00-17:00) |   Taller Arduino    |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("(17:00-18:00) |   Taller Arduino    |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("(18:00-19:00) |                     |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("")
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()
        def segundo():
            print("---------------------------------------------------------------------------------")
            print("(9:00-10:00)  |                                                                 |")
            print("---------------------------------------------------------------------------------")
            print("(10:00-11:00) | Taller de PLC  | Feria de Tecnologia |   Rama IEEE  | LEGO      |")
            print("---------------------------------------------------------------------------------")
            print("(11:00-12:00) | Taller de PLC  | Feria de Tecnologia |  Tec Hunter  | LEGO      |")
            print("---------------------------------------------------------------------------------")
            print("(12:00-13:00) | Taller de PLC  | Feria de Tecnologia | Larvic UCSP  | SOCCER    |")
            print("---------------------------------------------------------------------------------")
            print("(13:00-14:00) | Taller de PLC  | Feria de Tecnologia |              | LIBRE     |")
            print("---------------------------------------------------------------------------------")
            print("(14:00-15:00) |                | Feria de Tecnologia | Eagle Diseño |           |")
            print("---------------------------------------------------------------------------------")
            print("(15:00-16:00) | Taller Arduino |        Taller       |   diseño     | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("(16:00-17:00) | Taller Arduino |         de          |  de PCBs     | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("(17:00-18:00) | Taller Arduino |      creacion de    |              | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("(18:00-19:00) |                |      videojuegos    |              | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("")
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()
        def tercero():
            print("--------------------------------------------------------------------")
            print("(9:00-10:00)  |                                                    |")
            print("--------------------------------------------------------------------")
            print("(10:00-11:00) | Feria de Tecnologia |Grupo EDUCATIVA | SEGUIDORES  |")
            print("--------------------------------------------------------------------")
            print("(11:00-12:00) | Feria de Tecnologia | Fablab TECSUP  | SEGUIDORES  |")
            print("--------------------------------------------------------------------")
            print("(12:00-13:00) | Feria de Tecnologia |    MECANOS     | VELOCISTAS  |")
            print("--------------------------------------------------------------------")
            print("(13:00-14:00) | Feria de Tecnologia |                | VELOCISTAS  |")
            print("--------------------------------------------------------------------")
            print("(14:00-15:00) | Feria de Tecnologia |                |             |")
            print("--------------------------------------------------------------------")
            print("(15:00-16:00) |                     |    Proyectos   | MINI SUMOS  |")
            print("--------------------------------------------------------------------")
            print("(16:00-17:00) |                     |    Proyectos   | MINU SUMOS  |")
            print("------------------------------------------------------------------- ")
            print("(17:00-18:00) |                     |    Proyectos   |  WAR BOTS   |")
            print("--------------------------------------------------------------------")
            print("(18:00-19:00) |                     |                |  WAR BOTS   |")
            print("--------------------------------------------------------------------")
            print("(19:00-20:00) |                     |                |  WAR BOTS   |")
            print("--------------------------------------------------------------------")
            print()
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()
        def cuarto():

            print("---------------------------------------------------------")
            print("(9:00-10:00)  |                                         |")
            print("---------------------------------------------------------")
            print("(10:00-11:00) | Feria de Tecnologia | FINAL SEGUIDORES  |")
            print("---------------------------------------------------------")
            print("(11:00-12:00) | Feria de Tecnologia | FINAL VELOCISTA   |")
            print("---------------------------------------------------------")
            print("(12:00-13:00) | Feria de Tecnologia |    SUMOBOTS       |")
            print("---------------------------------------------------------")
            print("(13:00-14:00) | Feria de Tecnologia |      MIROSOFT     |")
            print("---------------------------------------------------------")
            print("(14:00-15:00) | Feria de Tecnologia |      MIROSOFT     |")
            print("---------------------------------------------------------")
            print("(15:00-16:00) |                                         |")
            print("---------------------------------------------------------")
            print("(16:00-17:00) |               CLAUSURA                  |")
            print("---------------------------------------------------------")
            print("(17:00-18:00) |                     |       WAR BOTS    |")
            print("---------------------------------------------------------")
            print("(18:00-19:00) |                     |       WAR BOTS    |")
            print("---------------------------------------------------------")
            print("(19:00-20:00) |                     |       WAR BOTS    |")
            print("---------------------------------------------------------")
            print("")
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()

        print("\n/////////////CRONOGRAMA//////////////\n")
        print("-------------------------------")
        print("\t (1) Primer dia")
        print("-------------------------------")
        print("\t (2) Segundo dia ")
        print("-------------------------------")
        print("\t (3) Tercer dia ")
        print("-------------------------------")
        print("\t (4) Cuarto dia ")
        print("-------------------------------")
        print("\t (5) Regresar al menu  ")
        print("-------------------------------")

        op=int(input("Digite una opcion : "))
        if op==1:
            primero()
        elif op==2:
            segundo()
        elif op==3:
            tercero()
        elif op==4:
            cuarto()
        elif op==5:
            salirmenu()
        else:
            input("Digite una opcion valida ...")
            cronograma()
    def contactenos():
        print("FACEBOOK : ")
        print("https://www.facebook.com/IEEEUNSA/?fref=ts# ")
        input("Presione 'Enter' para regresar al MENU PRINCIPAL ")
        menu()

    print("\n//////////MENU PRINCIPAL///////////\n")
    print("-------------------------------")
    print("\t (1) Sobre EXPOTRON")
    print("-------------------------------")
    print("\t (2) Inscripciones ")
    print("-------------------------------")
    print("\t (3) Ver cronograma ")
    print("-------------------------------")
    print("\t (4) contactenos ")
    print("-------------------------------")
    print("\t (5) Salir ")
    print("-------------------------------")

    opcion=int(input("Digite una opcion del Menú :"))

    if opcion==1:
        nosotros()
    elif opcion==2:
        inscripcion()
    elif opcion==3:
        cronograma()
    elif opcion==4:
        contactenos()
    elif opcion==5:
        sys.exit()
    else:
        input("Digite una opcion valida  ")
        menu()
menu()





