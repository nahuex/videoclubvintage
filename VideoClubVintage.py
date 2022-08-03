#! /usr/bin/env python
#-*- coding: utf-8 -*-

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ MODULOS IMPORTADOS ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

import os

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ FUNCION CONSULTAR PELICULA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

def consultar_estado_pelicula(codigo_de_barras): #Creamos la funcion "consultar_estado_pelicula" y declaramos las variables que utilizara la funcion, en este caso pondremos el codigo de barras.
    with open("peliculas.txt", "r") as jArchi: #Abrimos el archivo peliculas.txt en modo "read", lo que nos permite leer informacion y lo alojamos en nuestra varible jArchi.
        with open("clientes.txt", "r") as xArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer informacion y lo alojamos en nuestra varible xArchi.
            linea1 = jArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea1"
            linea2 = xArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea2"
            while linea1 != "" and linea2 != "": #Creamos un bucle while dentro de la varible "linea1" y "linea2", mientras los archivos no esten vacios.
                renglon1 = linea1.split(',') #Separamos la informacion de la linea1 con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon1".
                renglon2 = linea2.split(',') #Separamos la informacion de la linea2 con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon2".
                if codigo_de_barras == renglon1[0] and renglon1[3] == "Disponible": #Creamos una condicion con if donde la variable "codigo_de_barras" debe ser igual a informacion alojada en el espacio renglon1[0] del arhivo abierto y a la informacion en renglon1[3] e igual a "Disponible"
                    jArchi.close() #Cerramos el archivo abierto
                    print("Pelicula:", renglon1[1]) #Imprimimos el nombre de la pelicula que esta alojada en el renglon1[1]
                    print("Estado: DISPONIBLE") #Imprimimos "Estado: DISPONIBLE"
                    print() #Dejamos espacio
                    return '\033[1m' + "¡ESTA PELICULA SE PUEDE ALQUILAR!" + '\033[0m' #Si se cumple la condicion se retornara si es posible alquilar la pelicula.
                elif codigo_de_barras == renglon2[5]: #Sino si codigo_de_barras es igual al renglon2[5]
                    xArchi.close() #Cerramos el archivo abierto
                    print("Pelicula:", renglon1[1]) #Imprimimos el nombre de la pelicula que esta alojada en el renglon1[1]
                    print("Estado: ALQUILADA") #Imprimimos el estado "ALQUILADA"
                    print("DNI del Cliente:", renglon2[0]) #Imprimimos el DNI del Cliente.
                    print("Nombre y Apellido del Cliente:", renglon2[1]) #imprimimos el nombre y el apellido del clinte.
                    print() #Dejamos espacio.
                    return '\033[1m' + "¡ESTA PELICULA NO SE PUEDE ALQUILAR!" + '\033[0m' #Si se cumple la condicion se retornara que la pelicula no esta disponible.
                linea2 = xArchi.readline() #Leemos una vez mas el archivo
                linea1 = jArchi.readline() #Leemos una vez mas el archivo
            xArchi.close() #Cerramos el archivo abierto
            jArchi.close() #Cerramos el archivo abierto
            return '\033[1m' + "¡La Pelicula ingresada, no existe en la Base De Datos!" + '\033[0m' #En caso de que la condicion if no se cumpla, se retornara "¡La Pelicula ingresada, no existe en la Base De Datos!".

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ FUNCIONES GESTION DE CLIENTE ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

# FUNCION AGREGAR CLIENTE

def agregar_cliente(documento, nombre, apellido, telefono, direccion): #Creamos la funcion "agregar_cliente" y declaramos las variables que utilizara la funcion, en este caso pondremos los datos del cliente.
    with open("clientes.txt", "a") as jArchi: #Abrimos el archivo clientes.txt en modo "appen", lo que nos permite agregar informacion y lo alojamos en nuestra varible jArchi.
        jArchi.write(documento + "," + (nombre.lower().capitalize()) + " " + (apellido.lower().capitalize()) + "," + telefono + "," + (direccion.lower().capitalize()) + "," + "Activo" + "," + "0" + "," + "\n") #Escribimos el arhivo abierto con ".write" y la informacion solicitada del nuevo cliente.
        jArchi.close() #Cerramos el archivo abierto.
        return '\033[1m' + "¡Se agrego correctamente un Nuevo Cliente!" + '\033[0m' #Retornamos una respuesta si los datos se guardaron correctamente.

# FUNCION CONSULTAR CLIENTE

def consultar_cliente(documento): #Creamos la funcion "consultar_cliente" y le declaramos las variables que utilizara la funcion, en este caso pondremos el Documento del cliente.
    with open("clientes.txt", "r") as jArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible jArchi.
        linea = jArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
        while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
            renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
            if documento == renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser igual a informacion alojada en el espacio [0] del arhivo abierto.
                jArchi.close() #Cerramos el archivo abierto.
                print('\033[1m' + "¡Cliente Encontrado!" + '\033[0m') #Imprimimos "¡Cliente Encontrado!"
                print()
                print('\033[1m' + "Nombre:" + '\033[0m', renglon[1])
                return renglon[4] #Si se cumple la condicion se retornara el Estado del Cliente.
            linea = jArchi.readline() #Leemos una vez mas el archivo.
        jArchi.close() #Cerramos de nuevo el archivo.
        return '\033[1m' + "¡No existe el Cliente en la Base de Datos!" + '\033[0m' #En caso de que la condicion if no se cumpla, se retornara "¡No existe el Cliente en la Base de Datos!".


# FUNCION MODIFICAR TELEFONO CLIENTE

def modificar_cliente_telefono(documento, telefono): #Creamos la funcion "modificar_cliente_telefono" y le declaramos las variables que utilizara la funcion, en este caso pondremos el Documento y Telefono del cliente.
    with open("clientes.txt", "r") as rArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("clientescpy.txt", "w") as wArchi: #Abrimos el archivo clientescpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if documento == renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser igual a informacion alojada en el espacio [0] del arhivo abierto.
                    wArchi.writelines(renglon[0] + "," + renglon[1] + "," + telefono + "," + renglon[3] + "," + renglon[4] + "," + renglon[5] + "," + "\n") #Sustituimos el numero de telefono del cliente.
                else:
                    wArchi.write(linea) #Se copiaran las lineas del arhivo clientes.txt en el archivo clientescpy.txt con la condicion dada.
                linea = rArchi.readline() #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos de nuevo el archivo.
        rArchi.close() #Cerramos de nuevo el archivo.
    with open("clientescpy.txt", "r") as fcopia: #Abrimos el archivo clientescpy.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible fcopia.
        with open("clientes.txt", "w") as foriginal: #Abrimos el archivo clientes.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos de nuevo el archivo.
        foriginal.close() #Cerramos de nuevo el archivo.
        return '\033[1m' + "¡Se modifico el Telefono correctamente!" + '\033[0m' #Si se cumple la condicion se retornara que el telefono se pudo modificar.

# FUNCION MODIFICAR DIRECCION CLIENTE

def modificar_cliente_direccion(direccion): #Creamos la funcion "modificar_cliente_direccion" y le declaramos las variables que utilizara la funcion, en este caso pondremos el Documento del cliente.
    with open("clientes.txt", "r") as rArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("clientescpy.txt", "w") as wArchi: #Abrimos el archivo clientescpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if documento == renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser igual a informacion alojada en el espacio [0] del arhivo abierto.
                    wArchi.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + (direccion.lower().capitalize()) + "," + renglon[4] + "," +  renglon[5] + "," + "\n") #Sustituimos la direccion del cliente.
                else: #Si no se cumple la condicion de if
                    wArchi.write(linea) #Se copiaran las lineas del arhivo clientes.txt en el archivo clientescpy.txt con la condicion dada.
                linea = rArchi.readline() #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos de nuevo el archivo.
        rArchi.close() #Cerramos de nuevo el archivo.
    with open("clientescpy.txt", "r") as fcopia: #Abrimos el archivo clientescpy.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible fcopia.
        with open("clientes.txt", "w") as foriginal: #Abrimos el archivo clientes.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos de nuevo el archivo.
        foriginal.close() #Cerramos de nuevo el archivo.
        return '\033[1m' + "¡Se modifico la Direccion correctamente!" + '\033[0m' #Si se cumple la condicion se retornara que la direccion se pudo modificar.


# FUNCION BORRAR CLIENTE

def borrar_cliente(documento): #Creamos la funcion "borrar_cliente" y le declaramos la variable "documento" del cliente.
    with open("clientes.txt", "r") as rArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("clientescpy.txt", "w") as wArchi: #Abrimos el archivo clientescpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "":  #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if documento != renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser distinta a informacion alojada en el espacio [0] del arhivo abierto.
                    wArchi.write(linea) #Se copiarlas las lineas del arhivo clientes.txt en el archivo clientescpy.txt con la condicion dada.
                linea = rArchi.readline() #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos de nuevo el archivo.
        rArchi.close() #Cerramos de nuevo el archivo.
    with open("clientescpy.txt", "r") as fcopia: #Abrimos el arhivo clientescpy.txt en modo "read" y lo alojamos en la variable "fcopia"
        with open("clientes.txt", "w") as foriginal: #Abrimos el arhivo clientes.txt en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        return '\033[1m' + "¡Se Elimino el Cliente correctamente!" + '\033[0m' #Retornamos "¡Se Elimino el Cliente correctamente!".

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ FUNCIONES GESTION DE PELICULAS ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

# FUNCION AGREGAR PELICULA

def agregar_pelicula(codigo_de_barra, nombre_pelicula, categoria): #Creamos la funcion "agregar_pelicula" y le declaramos la variables que necesitamos para agregar una pelicula.
    with open("peliculas.txt", "a") as jArchi: #Abrimos el archivo "peliculas.txt" en modo "appen", lo que nos permite agregar informacion y lo alojamos en nuestra varible jArchi.
        jArchi.write(codigo_de_barra + "," + (nombre_pelicula.lower().capitalize()) + "," + (categoria.lower().capitalize()) + "," + "Disponible" + "," + "0" + "," + "\n") #Escribimos el arhivo abierto con ".write" y la informacion solicitada de la nueva pelicula.
        jArchi.close() #Cerramos el archivo.
        return '\033[1m' + "¡Se agrego correctamente una Nueva Pelicula!" + '\033[0m' #Retornamos "¡Se agrego correctamente una Nueva Pelicula!".

# FUNCION CONSULTAR PELICULA

def consultar_pelicula(codigo_de_barras): #Creamos la funcion "consultar_pelicula" y le declaramos la variable "codigo_de_barras".
    with open("peliculas.txt", "r") as kArchi:  #Abrimos el archivo peliculas.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible kArchi.
        linea = kArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
        while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
            renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
            if codigo_de_barras == renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser igual a informacion alojada en el espacio [0] del arhivo abierto.
                print() #Espacio
                print("Codigo de Barras: ", renglon[0]) #Imprimimos "Codigo de Barras: " y el valor alojado en el estacion "renglon[0]". 
                print("Nombre: ", renglon[1])  #Imprimimos "Nombre: " y el valor alojado en el espacio "renglon[1]". 
                print("Categoria: ", renglon[2]) #Imprimimos "Categoria: " y el valor alojado en el espacio "renglon[2]". 
                print("Estado: ", renglon[3]) #Imprimimos "Estado: " y el valor alojado en el espacio "renglon[3]". 
                print("Cliente: ", renglon[4]) #Imprimimos "Cliente: " y el valor alojado en el espacio "renglon[4]". 
                print() #Espacio
                return '\033[1m' + "¡Pelicula Encontrada!" + '\033[0m' #Retornamos "¡Pelicula Encontrada!". 
            linea = kArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
        kArchi.close() #Cerramos el archivo.
        return '\033[1m' + "!No existe la Pelicula en la Base de Datos!" + '\033[0m' #Retornamos "!No existe la Pelicula en la Base de Datos!".

# FUNCION MODIFICAR PELICULA

def modificar_pelicula(codigo_de_barras, nombre, categoria, estado, cliente): #Creamos la funcion "consultar_pelicula" y le declaramos la variables con los datos de la pelicula a modificar.
    with open("peliculas.txt", "r") as rArchi: #Abrimos el archivo "peliculas.txt" en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible kArchi.
        with open("peliculascpy.txt", "w") as wArchi: #Abrimos el archivo "peliculascpy.txt" en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if codigo_de_barras == renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser igual a informacion alojada en el espacio [0] del arhivo abierto.
                    wArchi.writelines(codigo_de_barras + "," + (nombre.lower().capitalize()) + "," + (categoria.lower().capitalize()) + "," + (estado.lower().capitalize()) + "," + cliente + "," + "\n") #Escribimos el arhivo abierto con ".write" y la informacion solicitada de la pelicula a modificar.
                else: #Si no se cumple la condicion de if
                    wArchi.write(linea) #Se copiaran las lineas del arhivo peliculas.txt en el archivo peliculascpy.txt con la condicion dada.
                linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            wArchi.close() #Cerramos el archivo.
        rArchi.close() #Cerramos el archivo.
    with open("peliculascpy.txt", "r") as fcopia: #Abrimos el arhivo "peliculascpy.txt" en modo "read" y lo alojamos en la variable "fcopia"
        with open("peliculas.txt", "w") as foriginal: #Abrimos el arhivo  "peliculas.txt" en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        return '\033[1m' + "¡Se modificaron TODOS los Datos correctamente!" + '\033[0m' #Retornamos "¡Se modificaron TODOS los Datos correctamente!"

# FUNCION BORRAR PELICULA

def borrar_pelicula(codigo_de_barra): #Creamos la funcion "borrar_pelicula" y le declaramos la variable "codigo_de_barra" de la pelicula.
    with open("peliculas.txt", "r") as rArchi: #Abrimos el archivo "peliculas.txt" en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("peliculascpy.txt", "w") as wArchi: #Abrimos el archivo "peliculascpy.txt" en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if codigo_de_barra != renglon[0]: #Creamos una condicion con if donde la variable "documento" debe ser distinto a informacion alojada en el espacio [0] del arhivo abierto.
                    wArchi.write(linea) #Se copiaran las lineas del arhivo "peliculas.txt" en el archivo "peliculascpy.txt" con la condicion dada.
                linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            wArchi.close() #Cerramos el archivo.
        rArchi.close() #Cerramos el archivo.
    with open("peliculascpy.txt", "r") as fcopia: #Abrimos el arhivo "peliculascpy.txt" en modo "read" y lo alojamos en la variable "fcopia"
        with open("peliculas.txt", "w") as foriginal: #Abrimos el arhivo "peliculas.txt" en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia:  #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        return '\033[1m' + "¡Se Elimino la Pelicula correctamente!" + '\033[0m' #Retornamos "¡Se Elimino la Pelicula correctamente!"

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ FUNCIONES PRESTAMO PELICULA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

# FUNCION CONSULTAR PELICULAS DISPONIBLES

def consultar_peliculas_disponibles(): #Creamos la funcion "consultar_peliculas_disponibles"
    with open("peliculas.txt", "r") as kArchi: #Abrimos el archivo peliculas.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible kArchi.
        print('\033[1m' + "*************************************************************** PELICULAS DISPONIBLES ***************************************************************" + '\033[0m') #Imprimimos un titulo
        print() #Espacio
        print("{:^30}{:^1}{:^30}{:^1}{:^30}{:^1}{:^30}{:^1}{:^30}".format("CODIGO DE BARRAS", "|", "NOMBRE", "|", "CATEGORIA", "|", "ESTADO", "|", "CLIENTE")) #Imprimimos una forma de tabla.
        linea = kArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
        estado = "Disponible" #Variable de estado "Disponible"
        while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
            renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
            if estado == renglon[3]: #Si el estado es igual al renglon[3]
                print("{:^30}{:^1}{:^30}{:^1}{:^30}{:^1}{:^30}{:^1}{:^30}".format(renglon[0], "|", renglon[1], "|", renglon[2], "|", renglon[3], "|", renglon[4])) #Imprimimos
            linea = kArchi.readline() #Leemos una vez mas el archivo.
        kArchi.close() #Cerramos el archivo.
        print() #Espacio
        return '\033[1m' + "*******************************************************************************************************************************************************" + '\033[0m' #Imprimimos deco.

# FUNCION REGISTRAR ALQUILER PELICULA

def registrar_alquiler_dni(codigo_de_barras, documento): #Creamos la funcion "registrar_alquiler_dni" y le declaramos la variable "documento" del cliente y "codigo_de_barras" de la pelicula.
    with open("peliculas.txt", "r") as rArchi:  #Abrimos el archivo peliculas.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("peliculascpy.txt", "w") as wArchi: #Abrimos el archivo peliculascpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if codigo_de_barras == renglon[0]: #Si el codigo_de_barras es igual al renglon[0]
                    wArchi.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + "Alquilada" + "," + documento + "," + "\n") #Se copiaran la informacion nueva en el archivo "peliculascpy.txt" en el archivo si la condicion se da.
                else: #Si no
                    wArchi.write(linea) #Se copiarlas las lineas del arhivo "peliculas.txt" en el archivo "peliculascpy".txt con la condicion dada.
                linea = rArchi.readline() #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos el archivo.
        rArchi.close() #Cerramos el archivo.
    with open("peliculascpy.txt", "r") as fcopia: #Abrimos el arhivo peliculascpy.txt en modo "read" y lo alojamos en la variable "fcopia"
        with open("peliculas.txt", "w") as foriginal: #Abrimos el arhivo peliculas.txt en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        print('\033[1m' + "La Pelicula Codigo de Barras:" + '\033[0m', codigo_de_barras) #Imprimimos el codigo de barras
        print()
        return '\033[1m' + "Se registro al Cliente DNI:" + '\033[0m' #Imprimimos el DNI del cliente que se llevo la pelicula.

def registrar_alquiler_codigo(codigo_de_barras, documento): #Creamos la funcion "registrar_alquiler_codigo" y le declaramos la variable "documento" del cliente y "codigo_de_barras" de la pelicula.
    with open("clientes.txt", "r") as rArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("clientescpy.txt", "w") as wArchi: #Abrimos el archivo clientescpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if documento == renglon[0]: #Si el documento es igual al renglon[0]
                    wArchi.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + renglon[3] + "," + renglon[4] + "," + codigo_de_barras + "," + "\n") #Sustituimos el codigo de barras.
                else:
                    wArchi.write(linea) #Se copian las lineas del arhivo clientes.txt en el archivo clientescpy.txt con la condicion dada.
                linea = rArchi.readline()  #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos el archivo.
        rArchi.close() #Cerramos el archivo.
    with open("clientescpy.txt", "r") as fcopia: #Abrimos el arhivo clientescpy.txt en modo "read" y lo alojamos en la variable "fcopia"
        with open("clientes.txt", "w") as foriginal: #Abrimos el arhivo clientes.txt en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        return documento #Retornamos el documento

# FUNCION REGISTRAR DEVOLUCION PELICULA

def registrar_devolucion_dni(codigo_de_barras, documento): #Creamos la funcion "registrar_devolucion_dni" y le declaramos la variable "documento" del cliente y "codigo_de_barras" de la pelicula.
    with open("peliculas.txt", "r") as rArchi: #Abrimos el archivo peliculas.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("peliculascpy.txt", "w") as wArchi: #Abrimos el archivo peliculascpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if codigo_de_barras == renglon[0]: #Si el documento es igual al renglon[0]
                    wArchi.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + "Disponible" + "," + "0" + "," + "\n") #Se copiaran la informacion nueva en el archivo "peliculascpy.txt" en el archivo si la condicion se da.
                else:
                    wArchi.write(linea) #Se copian las lineas del arhivo peliculas.txt en el archivo peliculascpy.txt con la condicion dada.
                linea = rArchi.readline() #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos el archivo.
        rArchi.close() #Cerramos el archivo.
    with open("peliculascpy.txt", "r") as fcopia: #Abrimos el arhivo peliculascpy.txt en modo "read" y lo alojamos en la variable "fcopia"
        with open("peliculas.txt", "w") as foriginal: #Abrimos el arhivo peliculas.txt en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        print('\033[1m' + "El Cliente DNI:" + '\033[0m', documento) #Imprimimos el DNI del cliente
        print('\033[1m' + "Ya NO tiene Alquilada la Pelicula:" + '\033[0m') #El estado actual de la peli
        return '\033[1m' + "Codigo de Barras:" + '\033[0m' #Retornamos el codigo de barras.

def registrar_devolucion_codigo(codigo_de_barras, documento): #Creamos la funcion "registrar_devolucion_codigo" y le declaramos la variable "documento" del cliente y "codigo_de_barras" de la pelicula.
    with open("clientes.txt", "r") as rArchi: #Abrimos el archivo clientes.txt en modo "read", lo que nos permite leer la informacion y lo alojamos en nuestra varible rArchi.
        with open("clientescpy.txt", "w") as wArchi: #Abrimos el archivo clientescpy.txt en modo "write", lo que nos permite sustituir la informacion y lo alojamos en nuestra varible wArchi.
            linea = rArchi.readline() #Leemos el arhivo abierto con ".readline" y lo alojamos en la variable "linea".
            while linea != "": #Creamos un bucle while dentro de la varible "linea", mientras el archivo no este vacio.
                renglon = linea.split(',') #Separamos la informacion de la linea con ".split" y le decimos que lo haga con ",". La informacion separada se alojara en la variable "renglon".
                if documento == renglon[0]: #Si el documento es igual al renglon[0]
                    wArchi.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + renglon[3] + "," + renglon[4] + "," + "0" + "," + "\n") #<--------------------?
                else:
                    wArchi.write(linea) #Se copian las lineas del arhivo clientes.txt en el archivo clientescpy.txt con la condicion dada.
                linea = rArchi.readline() #Leemos una vez mas el archivo.
            wArchi.close() #Cerramos el archivo.
        rArchi.close() #Cerramos el archivo.
    with open("clientescpy.txt", "r") as fcopia: #Abrimos el arhivo clientescpy.txt en modo "read" y lo alojamos en la variable "fcopia"
        with open("clientes.txt", "w") as foriginal: #Abrimos el arhivo clientes.txt en modo "write" y lo alojamos en la variable "foriginal"
            for registro in fcopia: #Alojamos el contenido de la variable "fcopia" en la variable "registro".
                foriginal.write(registro) #Copiamos la informacion de la variable "registro" en el achivo original alojado en la variable "foriginal".
            fcopia.close() #Cerramos el archivo.
        foriginal.close() #Cerramos el archivo.
        return codigo_de_barras #Retornamos el codigo de barras.

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ FUNCIONES MENUES ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

# FUNCION LIMPIAR PANTALLA

def limpioPantalla(): #Creamos la funcion "lipioPantalla" 
    sisOper = os.name #Creamos la variable "sisOper" que es igual al sistema operativo que se esta ejecutando el ahivo .py
    if sisOper == "posix":  # si fuera UNIX, mac para Apple, java para maquina virtual Java
        os.system("clear") #Limpiamos pantalla
    elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
        os.system("cls") #Limpiamos pantalla

# FUNCION MUESTRO MENU

def muestroMenu(): #Creamos la funcion "muestroMenu" 
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ VIDEO CLUB VINTAGE ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄") #Imprimimos Titulo
    print() #Espacio
    print("                        >> MENU PRINCIPAL <<") #Imprimimos Titulo
    print(''' 
    0 - Consultar Disponibilidad Pelicula
    1 - Gestion de Clientes
    2 - Gestion de Peliculas
    3 - Prestamo de Pelicula
    4 - Limpiar Pantalla
    5 - Salir
    
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ''') #Imprimimos Menues

# FUNCION SUB MENU PRESTAMO PELICULA

def SubMenu_Prestamo_Pelicula(): #Creamos la funcion "SubMenu_Prestamo_Pelicula" 
    print('''
    0 - Consultar Peliculas Disponibles
    1 - Registrar Alquiler
    2 - Registrar Devolucion
    3 - Volver al Menu Principal
    ''') #Imprimimos Menues

# FUNCION SUB MENU GESTION DE CLIENTES

def SubMenu_Gestion_Clientes(): #Creamos la funcion "SubMenu_Gestion_Clientes" 
    print('''
    0 - Alta de Cliente
    1 - Consultar Estado de Cliente
    2 - Modificar Telefono o Direccion de Cliente
    3 - Eliminar Cliente
    4 - Volver al Menu Principal
    ''') #Imprimimos Menues

# FUNCION SUB MENU GESTION DE PELICULAS

def SubMenu_Gestion_Peliculas(): #Creamos la funcion "SubMenu_Gestion_Peliculas" 
    print('''
    0 - Alta de Pelicula
    1 - Consultar Pelicula
    2 - Modificar Pelicula
    3 - Eliminar Pelicula
    4 - Volver al Menu Principal
    ''') #Imprimimos Menues

# FUNCION SUB MENU MODIFICAR CLIENTES

def SubMenu_Modificar_Cliente(): #Creamos la funcion "SubMenu_Modificar_Cliente" 
    print('''
    0 - Modificar Telefono
    1 - Modificar Direccion
    2 - Volver al Menu Principal
    ''') #Imprimimos Menues

# ARMADO DE MENU INTERACTIVO
opc = 0 #Establecemos la variable "opc" con valor 0
while opc != 7: #Creamos un bucle while donde "opc" sea distinto de 7
    muestroMenu()  # Menu Principal
    opcion = int(input('\033[1m' + "Elija la opción deseada: " + '\033[0m')) #Creamos la variable "opcion" con un input
    if opcion == 0: #Consultar Estado Pelicula #Creamos la condicion if si "opcion" es igual a 0
        print() #Espacio
        print('\033[1m' + "¿Que pelicula desea buscar?" + '\033[0m') #Imprimimos "¿Que pelicula desea buscar?"
        print() #Espacio
        codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
        print() #Espacio
        print(consultar_estado_pelicula(codigo_de_barras)) #Imprimimos la funcion "consultar_estado_pelicula"
    elif opcion == 1:  # SubMenu Gestion de Clientes #Creamos la condicion elif si "opcion" es igual a 1
        SubMenu_Gestion_Clientes()  # SubMenu Gestion de Clientes #Imprimimos la funcion "SubMenu_Gestion_Clientes"
        opcion = int(input('\033[1m' + "Elija la opción deseada: " + '\033[0m')) #Creamos la variable "opcion" con un input
        if opcion == 0:  # Alta Nuevo Cliente #Creamos la condicion if si "opcion" es igual a 0
            print('\033[1m' + "¡Se dara de Alta un Nuevo Cliente!" + '\033[0m') #Imprimimos la funcion "¡Se dara de Alta un Nuevo Cliente!"
            print() #Espacio 
            documento = input("Ingrese el DNI: ") #Creamos la variable "documento" con un input
            nombre = input("Ingrese el Nombre: ") #Creamos la variable "nombre" con un input
            apellido = input("Ingrese el Apellido: ") #Creamos la variable "apellido" con un input
            telefono = input("Ingrese el Teléfono: ") #Creamos la variable "telefono" con un input
            direccion = input("Ingrese la Direccion: ") #Creamos la variable "direccion" con un input
            print() #Espacio 
            print(agregar_cliente(documento, nombre, apellido, telefono, direccion)) #Imprimimos la funcion "agregar_clientes"
        elif opcion == 1:  # Consultar Estado Cliente #Creamos la condicion elif si "opcion" es igual a 1
            print('\033[1m' + "¿Que Cliente desea buscar?" + '\033[0m') #Imprimimos  "¿Que Cliente desea buscar?"
            print() #Espacio 
            nombre = input("Ingrese el DNI: ") #Creamos la variable "nombre" con un input
            print() #Espacio 
            print('\033[1m' + "Estado: " + '\033[0m', consultar_cliente(nombre)) #Imprimimos la funcion "consultar_cliente"
        elif opcion == 2:  # Modificar Datos Cliente #Creamos la condicion elif si "opcion" es igual a 2
            SubMenu_Modificar_Cliente()  # SubMenu Modificar Cliente #Imprimimos la funcion "SubMenu_Modificar_Cliente"
            opcion = int(input('\033[1m' + "Elija la opción deseada: " + '\033[0m')) #Creamos la variable "opcion" con un input
            if opcion == 0: #Creamos la condicion if si "opcion" es igual a 0
                print('\033[1m' + "¡Se modificará el Teléfono del Cliente!" + '\033[0m') #Imprimimos "¿Que Cliente desea buscar?"
                print() #Espacio 
                documento = input("Ingrese el DNI: ") #Creamos la variable "documento" con un input
                telefono = input("Ingrese el Nuevo Telefono: ") #Creamos la variable "telefono" con un input
                print() #Espacio
                print(modificar_cliente_telefono(documento, telefono))
            elif opcion == 1: #Creamos la condicion elif si "opcion" es igual a 1
                print('\033[1m' + "¡Se modificará la Direccion del Cliente!" + '\033[0m') #Imprimimos "¡Se modificará la Direccion del Cliente!" 
                print() #Espacio
                documento = input("Ingrese el DNI: ") #Creamos la variable "documento" con un input
                direccion = input("Ingrese la Nueva Direccion: ") #Creamos la variable "direccion" con un input
                print() #Espacio
                print(modificar_cliente_direccion(direccion)) #Imprimimos la funcion "modificar_cliente_direccion"
            elif opcion == 2: #Creamos la condicion elif si "opcion" es igual a 2
                limpioPantalla() #Imprimimos la funcion "limpioPantalla"
        elif opcion == 3:  # Eliminar Cliente #Creamos la condicion elif si "opcion" es igual a 3
            print('\033[1m' + "¡Se Eliminará un Cliente!" + '\033[0m') #Imprimimos "¡Se Eliminará un Cliente!"
            print() #Espacio
            documento = input("Ingrese el DNI: ") #Creamos la variable "documento" con un input
            print() #Espacio
            print(borrar_cliente(documento)) #Imprimimos la funcion "borrar_cliente"
        elif opcion == 4: #Creamos la condicion elif si "opcion" es igual a 4
            limpioPantalla() #Imprimimos la funcion "limpioPantalla"
    elif opcion == 2:  # SubMenu Gestion de Peliculas #Creamos la condicion elif si "opcion" es igual a 2
        SubMenu_Gestion_Peliculas()  # SubMenu Gestion de Peliculas #Imprimimos la funcion "SubMenu_Gestion_Peliculas"
        opcion = int(input('\033[1m' + "Elija la opción deseada: " + '\033[0m')) #Creamos la variable "opcion" con un input
        if opcion == 0:  # Alta de Pelicula  #Creamos la condicion if si "opcion" es igual a 0
            print('\033[1m' + "¡Se dara de Alta una Nueva Pelicula!" + '\033[0m') #Imprimimos "¡Se dara de Alta una Nueva Pelicula!"
            print() #Espacio
            codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
            nombre_pelicula = input("Ingrese el Nombre: ") #Creamos la variable "nombre_pelicula" con un input
            categoria = input("Ingrese la Categoria: ") #Creamos la variable "categoria" con un input
            print() #Espacio
            print(agregar_pelicula(codigo_de_barras, nombre_pelicula, categoria)) #Imprimimos la funcion "agregar_pelicula"
        elif opcion == 1:  # Consultar Pelicula #Creamos la condicion elif si "opcion" es igual a 1
            print('\033[1m' + "¿Que Pelicula desea buscar?" + '\033[0m') #Imprimimos "¿Que Pelicula desea buscar?"
            print() #Espacio
            codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
            print() #Espacio
            print(consultar_pelicula(codigo_de_barras)) #Imprimimos la funcion "consultar_pelicula"
        elif opcion == 2:  #Modificar Datos Pelicula #Creamos la condicion elif si "opcion" es igual a 2
            print('\033[1m' + "¡Se modificarán todos los Datos de la Pelicula!" + '\033[0m') #Imprimimos "¡Se modificarán todos los Datos de la Pelicula!"
            print() #Espacio
            codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
            nombre = input("Ingrese el Nombre: ") #Creamos la variable "nombre" con un input
            categoria = input("Ingrese la Categoria: ") #Creamos la variable "categoria" con un input
            estado = input("Ingrese el Estado: ") #Creamos la variable "estado" con un input
            cliente = input("Ingrese DNI del Cliente: ") #Creamos la variable "cliente" con un input
            print() #Espacio
            print(modificar_pelicula(codigo_de_barras, nombre, categoria, estado, cliente)) #Imprimimos la funcion "modificar_pelicula"
        elif opcion == 3:  # Eliminar Peliculas #Creamos la condicion elif si "opcion" es igual a 3
            print('\033[1m' + "¡Se eliminará una Pelicula!" + '\033[0m') #Imprimimos "¡Se eliminará una Pelicula!"
            print() #Espacio
            codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
            print() #Espacio
            print(borrar_pelicula(codigo_de_barras)) #Imprimimos la funcion "borrar_pelicula"
    elif opcion == 3:  # Menu Prestamo Pelicula #Creamos la condicion elif si "opcion" es igual a 3
        SubMenu_Prestamo_Pelicula()  # SubMenu Prestamo Pelicula #Imprimimos la funcion "SubMenu_Prestamo_Peliculas"
        opcion = int(input('\033[1m' + "Elija la opción deseada:" + '\033[0m')) #Creamos la variable "opcion" con un input
        if opcion == 0: #Peliculas Disponibles #Creamos la condicion if si "opcion" es igual a 0
            print() #Espacio
            print(consultar_peliculas_disponibles()) #Imprimimos la funcion "consultar_peliculas_disponibles"
        elif opcion == 1: #Alquilar Pelicula #Menu Prestamo Pelicula #Creamos la condicion elif si "opcion" es igual a 1
            print('\033[1m' + "¿Que Pelicula desea Alquilar?" + '\033[0m') #Imprimimos "¿Que Pelicula desea Alquilar?"
            print() #Espacio
            codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
            print() #Espacio 
            print('\033[1m' + "¿A que Cliente?" + '\033[0m') #Imprimimos "¿A que Cliente?" 
            print() #Espacio 
            documento = input("Ingrese el DNI: ") #Creamos la variable "documento" con un input
            print() #Espacio
            print(registrar_alquiler_dni(codigo_de_barras,documento), registrar_alquiler_codigo(codigo_de_barras,documento)) #Imprimimos la funcion "registrar_alquiler_dni" y "registrar_alquiler_codigo"
        elif opcion == 2: #Devolver Pelicula # Menu Prestamo Pelicula #Creamos la condicion elif si "opcion" es igual a 2
            print('\033[1m' + "¿Que Pelicula desea devolver?" + '\033[0m') #Imprimimos "¿Que Pelicula desea devolver?"
            print() #Espacio
            codigo_de_barras = input("Ingrese el Codigo de Barras: ") #Creamos la variable "codigo_de_barras" con un input
            documento = input("Ingrese el DNI: ") #Creamos la variable "documento" con un input
            print() #Espacio
            print(registrar_devolucion_dni(codigo_de_barras,documento), registrar_devolucion_codigo(codigo_de_barras,documento)) #Imprimimos la funcion "registrar_alquiler_dni" y "registrar_alquiler_codigo"
    elif opcion == 4: #Creamos la condicion elif si "opcion" es igual a 4
        limpioPantalla() #Imprimimos funcion "limpioPantalla"
    else: #Si no
        opc = opcion #Ejecutamos variable opo