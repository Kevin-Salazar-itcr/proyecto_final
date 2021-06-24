"Proyecto programado 3"
"""
Integrantes del grupo:
    KEVIN SALAZAR
    KEINGELL MOODIE
"""
#------------tkinter------------#
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
#-------------time--------------#
import time
#------------pygame------------#
import pygame
#-------------random------------#
import random
#-------Archivos externos-------#
from Funciones_Auxiliares import funciones
#===============================================================
pygame.mixer.init() #Activacion de los efectos de sonido de pygame
def programa():
    inicio=tk.Tk()
    inicio.state("zoomed") #Maximiza el tamaño de la pantalla, sin modificar sus dimensiones
    intro=tk.PhotoImage(file="Fondo.png")
    label=tk.Label(inicio, image=intro).pack()
    pygame.mixer.music.load("viento.mp3")
    pygame.mixer.music.play(-1) #-1 para qiue el audio se reproduzca indefinidamente
    def on_closing2():
        pygame.mixer.music.stop()
        inicio.destroy()
    inicio.protocol("WM_DELETE_WINDOW", on_closing2)
                    
    def salir():
        a=pygame.mixer.Sound("click.mp3")
        a.play()
        inicio.destroy()
        pygame.mixer.music.stop()
        return print("programa()")

    def creditos():
        inicio.destroy()
        pantallaCreditos=tk.Tk()
        pantallaCreditos.state("zoomed")
        pantallaCreditos.config(bg="Black")
        logos=tk.PhotoImage(file="Logo (2).png")
        logotipo=tk.Label(pantallaCreditos, bg="black", image=logos).pack(pady=50)
        label=tk.Label(pantallaCreditos,
                       text="Torneo - Kuzu Productions\n@2020-2021. Derechos reservados\nCreadores\nKevin Salazar Valles\nKeingell Moodie Jaenkstche\nEste juego ha sido desarrollado con fines didácticos\nCualquier parecido con algún juego de la realidad es mera coincidencia",
                          font=("Times New Roman", 11), bg="black", fg="white").pack(pady=20)
        def iniciojuego():
            pantallaCreditos.destroy()
            juegoInicio=tk.Tk()
            juegoInicio.state("zoomed")
            juegoInicio.title("Torneo")
            imagen=tk.PhotoImage(file="fondo inicio.png")
            fondodelJuego=tk.Label(juegoInicio, image=imagen)
            fondodelJuego.pack()
            #----------------------------------------------------------------------------------------------------
            def keingell():
                pygame.mixer.music.load("drama.mp3")
                pygame.mixer.music.play(-1)
                class MenuPrincipal():
                    def __init__(self):
                        self.forma="menu"
                    def menuKeingell(self):
                        ventana = tk.Toplevel()
                        ventana.state("zoomed")
                        imagenVentana = tk.PhotoImage(file="FondoPelea.png")
                        fondoVentana = tk.Label(ventana, image=imagenVentana).place(x=0, y=0)
                        def on_closing():
                            pygame.mixer.music.stop()
                            ventana.destroy()
                        ventana.protocol("WM_DELETE_WINDOW", on_closing)
                        ventana.title("El gran Torneo")
                        ventana.config(bg="Black")
                        ventana.config(relief="groove")
                        ventana.config(bd=8)
                        label = tk.Label(ventana, text="Bienvenido porfavor elija una opcion", font=("TimesNewRoman", 20), bg="red",
                                         relief="groove").pack()
                        Personaje = tk.Button(ventana, text="Personajes", font=("TimesNewRoman", 14), bd=8, bg="red", width="23",
                                              height="1", relief="groove", cursor="hand2", command=crearPersonajes).place(x=244, y=200)
                        Cliente = tk.Button(ventana, text="CrearTorneo", font=("TimesNewRoman", 14), bd=8, bg="red", width="23", height="1",
                                            relief="groove", cursor="hand2", command=makeTorneo).place(x=544, y=200)
                        Salir = tk.Button(ventana, text="Jugar Torneo", font=("TimesNewRoman", 14), bd=8, bg="red", width="23", height="1",
                                          relief="groove", cursor="hand2", command=empezarPeleas).place(x=844, y=200)
                        ventana.mainloop()

                def pruebita():
                    n = random.randint(1,2)
                    return (n)

                def crearPersonajes():
                    clic=pygame.mixer.Sound("click.mp3")
                    clic.play()
                    ventana.withdraw()
                    def crearPersonaje_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        return tipoPersonaje()
                    def crearPersonaje_auxVolver():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                    
                        Venpersonaje.withdraw()
                        a=MenuPrincipal()
                        return a.menuKeingell()
                    def crearPersonaje_auxBorrar():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        return crearPersonaje_auxBorrar_aux()

                    Venpersonaje = tk.Toplevel()
                    imagenVentana = tk.PhotoImage(file="CivilWar1.png")
                    fondoVentana = tk.Label(Venpersonaje, image=imagenVentana).place(x=0, y=0)
                    Venpersonaje.state("zoomed")
                    Venpersonaje.title("Gran Torneo")
                    Venpersonaje.config(bg="Black")
                    Venpersonaje.config(relief="groove")
                    Venpersonaje.config(bd=8)
                    def on_closing():
                        pygame.mixer.music.stop()
                        Venpersonaje.destroy()
                    Venpersonaje.protocol("WM_DELETE_WINDOW", on_closing)
                    label = tk.Label(Venpersonaje, text="Porfavor Ingrese la siguiente información", font=("TimesNewRoman", 20), bg="red",
                                     relief="groove").pack()
                    confirmar = tk.Button(Venpersonaje, text="Comenzar", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                          width="30", height="1", cursor="hand2", command=crearPersonaje_aux).place(x=520, y=250)
                    volver = tk.Button(Venpersonaje, text="Volver", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                       width="30", height="1", cursor="hand2", command=crearPersonaje_auxVolver).place(x=220, y=250)
                    Eliminar = tk.Button(Venpersonaje, text="Eliminar", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                       width="30", height="1", cursor="hand2", command=crearPersonaje_auxBorrar).place(x=820, y=250)

                    Venpersonaje.mainloop()

                def crearPersonaje_auxBorrar_aux():
                    def crearPersonaje_auxBorrar_auxV1():
                        Borrar.withdraw()

                        if(cajaBorrar.get() == ""):
                            Alerta = mb.showerror(title="Error", message="Porfavor ingrese si desea que sea Heroe o villano.")
                            return crearPersonaje_auxBorrar_aux()
                        else:
                            return eliminarPersonaje(cajaBorrar.get())
                    Borrar = tk.Toplevel()
                    Borrar.title("Gran Torneo")
                    imagenVentana = tk.PhotoImage(file="CivilWar2.png")
                    fondoVentana = tk.Label(Borrar, image=imagenVentana).place(x=0, y=0)
                    alto=200
                    ancho=400
                    x_ventana=Borrar.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=Borrar.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    Borrar.geometry(posicion)
                    Borrar.config(bg="Black")
                    Borrar.config(relief="groove")
                    Borrar.config(bd = 8)
                    def on_closing():
                        mensaje=mg.showError(message="Procure no salir hasta terminar")
                    Borrar.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    label = tk.Label(Borrar, text="Ingrese el alterEgo del personaje\n que quiere borrar.", font=("TimesNewRoman", 14),
                                     bg="gray",bd=8,
                                     relief="groove").pack()
                    cajaBorrar = tk.Entry(Borrar, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    cajaBorrar.pack()
                    confirmar = tk.Button(Borrar, text="Continuar", font=("TimesNewRoman", 10), bd=8, bg="gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=crearPersonaje_auxBorrar_auxV1).pack()
                    Borrar.mainloop()


                def eliminarPersonaje(identif):
                    f = open("Luchadores.txt", "r")
                    lineas = f.readlines()
                    f.close()

                    f = open("Luchadores.txt", "w")
                    for linea in lineas:
                        if identif not in linea:
                            f.write(linea)
                    f.close()

                    f = open("MostrarPersonajes.txt", "r")
                    lineas = f.readlines()
                    f.close()

                    f = open("MostrarPersonajes.txt", "w")
                    for linea in lineas:
                        if identif not in linea:
                            f.write(linea)
                    f.close()
                    Alerta = mb.showinfo(title="Listo", message="Su Luchador fue eliminado con exito")


                def tipoPersonaje():
                    def tipoPersonaje_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        tipo.withdraw()
                        tipo1 = cajatipo.get()
                        if(tipo == ""):
                            Alerta = mb.showerror(title="Error", message="Porfavor ingrese si desea que sea Heroe o villano.")
                            return tipoPersonaje()
                        if (tipo1 == "H") or (tipo1 == "V"):
                            return sexoPersonaje(tipo1)
                        else:
                            Alerta = mb.showerror(title="Error", message="El caracter ingresado es incorrecto.")
                            return tipoPersonaje()
                    tipo = tk.Toplevel()
                    tipo.title("Gran Torneo")
                    imagenVentana = tk.PhotoImage(file="CivilWar2.png")
                    fondoVentana = tk.Label(tipo, image=imagenVentana).place(x=0, y=0)
                    alto=150
                    ancho=350
                    x_ventana=tipo.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=tipo.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    tipo.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    tipo.geometry(posicion)
                    tipo.config(bg="Black")
                    tipo.config(relief="groove")
                    tipo.config(bd = 8)
                    label = tk.Label(tipo, text="Tipo de personaje (Heroe o villano)\n Solo poner H o V", font=("TimesNewRoman", 14),
                                     bg="gray",bd=8,
                                     relief="groove").pack()
                    cajatipo = tk.Entry(tipo, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    cajatipo.pack()
                    confirmar = tk.Button(tipo, text="Continuar", font=("TimesNewRoman", 10), bd=8, bg="gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=tipoPersonaje_aux).pack()
                    tipo.mainloop()

                def sexoPersonaje(tipo):
                    def sexoPersonaje_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                    
                        sexo.withdraw()
                        sexo1 = cajasexo.get()
                        if(sexo == ""):
                            Alerta = mb.showerror(title="Error", message="Porfavor ingrese si desea que sea Heroe o villano.")
                            return sexoPersonaje(tipo)
                        if (sexo1 == "H") or (sexo1 == "M"):
                            return nombrePersonaje(tipo,sexo1)
                        else:
                            Alerta = mb.showerror(title="Error", message="El caracter ingresado es incorrecto.")
                            return sexoPersonaje(tipo)
                    sexo = tk.Toplevel()
                    sexo.title("Gran Torneo")
                    alto=150
                    ancho=350
                    x_ventana=sexo.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=sexo.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    sexo.geometry(posicion)
                    imagenVentana = tk.PhotoImage(file="CivilWar2.png")
                    fondoVentana = tk.Label(sexo, image=imagenVentana).place(x=0, y=0)
                    sexo.config(bg="Black")
                    sexo.config(relief="groove")
                    sexo.config(bd=8)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    sexo.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    label = tk.Label(sexo, text="Sexo de personaje (Hombre o Mujer)\n Solo poner H o M", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    cajasexo = tk.Entry(sexo, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    cajasexo.pack()
                    confirmar = tk.Button(sexo, text="Continuar", font=("TimesNewRoman", 12), bd=8, bg="gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=sexoPersonaje_aux).pack()
                    sexo.mainloop()

                def nombrePersonaje(tipo,sexo):
                    def nombrePersonaje_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                    
                        nombre.withdraw()
                        nombre1 = cajanombre.get()
                        if(nombre == ""):
                            Alerta = mb.showerror(title="Error", message="Porfavor ingrese el nombre de su personaje.")
                            return nombrePersonaje_aux(tipo,sexo)
                        if nombre != "":
                            return alteregoPersonaje(tipo,sexo,nombre1)
                        else:
                            Alerta = mb.showerror(title="Error", message="El caracter ingresado es incorrecto.")
                            return nombrePersonaje_aux(tipo,sexo)
                    nombre = tk.Toplevel()
                    nombre.title("Gran Torneo")
                    ancho=350
                    alto=150
                    x_ventana=nombre.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=nombre.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    nombre.geometry(posicion)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    nombre.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    imagenVentana = tk.PhotoImage(file="CivilWar2.png")
                    fondoVentana = tk.Label(nombre, image=imagenVentana).place(x=0, y=0)
                    nombre.config(bg="Black")
                    nombre.config(relief="groove")
                    nombre.config(bd=8)
                    label = tk.Label(nombre, text="Ingrese el nombre de su personaje.", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    cajanombre = tk.Entry(nombre, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    cajanombre.pack()
                    confirmar = tk.Button(nombre, text="Continuar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=nombrePersonaje_aux).pack()
                    nombre.mainloop()


                def alteregoPersonaje(tipo,sexo,nombre):
                    def alterEgoPersonaje_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                    
                        alter.withdraw()
                        alter1 = cajaalter.get()
                        if(alter == ""):
                            Alerta = mb.showerror(title="Error", message="Porfavor ingrese el Alter Ego de su personaje.")
                            return alterEgoPersonaje(tipo,sexo,nombre)
                        if alter != "":
                            return statsPersonaje(tipo,sexo,nombre,alter1)
                        else:
                            Alerta = mb.showerror(title="Error", message="El caracter ingresado es incorrecto.")
                            return alterEgoPersonaje(tipo,sexo,nombre)
                    alter = tk.Toplevel()
                    alter.title("Gran Torneo")
                    alto=150
                    ancho=350
                    x_ventana=alter.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=alter.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    alter.geometry(posicion)
                    imagenVentana = tk.PhotoImage(file="CivilWar2.png")
                    fondoVentana = tk.Label(alter, image=imagenVentana).place(x=0, y=0)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    alter.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    alter.config(bg="Black")
                    alter.config(relief="groove")
                    alter.config(bd=8)
                    label = tk.Label(alter, text="Ingrese el alterEgo de su personaje", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    cajaalter = tk.Entry(alter, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    cajaalter.pack()
                    confirmar = tk.Button(alter, text="Continuar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=alterEgoPersonaje_aux).pack()
                    alter.mainloop()

                def statsPersonaje(tipo,sexo,nombre,alterEgo):
                    tipo = str(tipo)
                    sexo = str(sexo)
                    nombre = str(nombre)
                    alterEgo = str(alterEgo)
                    def statsPersonaje_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                    
                        stats.withdraw()
                        velocidad = int(cajaVelocidad.get())
                        fuerza = int(cajaFuerza.get())
                        inteligencia = int(cajaIntelligencia.get())
                        defensa = int(cajaDefensa.get())
                        magia = int(cajaMagia.get())
                        telepatia = int(cajaTelepatia.get())
                        estratega = int(cajaEstrategia.get())
                        volar = int(cajaVolar.get())
                        elasticidad = int(cajaElasticidad.get())
                        regeneracion = int(cajaRegeneracion.get())
                        Total = velocidad + fuerza + inteligencia + defensa + magia + telepatia + estratega + volar + elasticidad + regeneracion
                        if (Total == 100):
                            return crearPersonaje(tipo,sexo,nombre,alterEgo,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estratega,volar,elasticidad,regeneracion)
                        else:
                            Alerta = mb.showerror(title="Error", message="La suma de sus estadisticas no llega a 100")
                            return statsPersonaje(tipo,sexo,nombre,alterEgo)
                    stats = tk.Toplevel()
                    stats.title("Gran Torneo")
                    imagenVentana = tk.PhotoImage(file="CivilWar3.png")
                    fondoVentana = tk.Label(stats, image=imagenVentana).place(x=0, y=0)
                    stats.config(bg="Black")
                    stats.config(relief="groove")
                    stats.config(bd=8)
                    def on_closing():
                        noCierre=mb.showerror(message="Procure no salir hasta terminar el proceso")
                    stats.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    x=tk.IntVar()
                    label = tk.Label(stats, text="Ingrese las estadisticas de su personaje, la suma de ellas debe dar 100", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    label = tk.Label(stats, text="         Velocidad         ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    cajaVelocidad = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=x)
                    cajaVelocidad.pack()
                    label = tk.Label(stats, text="           Fuerza             ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     
                                     relief="groove").pack()
                    a=tk.IntVar()
                    cajaFuerza = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=a)
                    cajaFuerza.pack()
                    label = tk.Label(stats, text="        Intelligencia        ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    b=tk.IntVar()
                    cajaIntelligencia = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=b)
                    cajaIntelligencia.pack()
                    label = tk.Label(stats, text="  Denfensa Personal  ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    c=tk.IntVar()
                    cajaDefensa = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=c)
                    cajaDefensa.pack()
                    label = tk.Label(stats, text="               Magia           ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    d=tk.IntVar()
                    cajaMagia = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=d)
                    cajaMagia.pack()
                    label = tk.Label(stats, text="            Telepatiá        ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    e=tk.IntVar()
                    cajaTelepatia = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=e)
                    cajaTelepatia.pack()
                    label = tk.Label(stats, text="           Estrategia       ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    g=tk.IntVar()
                    cajaEstrategia = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=g)
                    cajaEstrategia.pack()
                    label = tk.Label(stats, text="                Volar            ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    h=tk.IntVar()
                    cajaVolar = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=h)
                    cajaVolar.pack()
                    label = tk.Label(stats, text="           Elasticidad       ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    i=tk.IntVar()
                    cajaElasticidad = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=i)
                    cajaElasticidad.pack()
                    label = tk.Label(stats, text="       Regeneracion     ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    j=tk.IntVar()
                    cajaRegeneracion = tk.Entry(stats, font=("TimesNewRoman", 12), bg="white", relief="groove", textvariable=j)
                    cajaRegeneracion.pack()
                    confirmar = tk.Button(stats, text="Continuar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="18", height="1", cursor="hand2", command=statsPersonaje_aux).pack()

                    stats.mainloop()

                def crearPersonaje(tipo,sexo,nombre,alterEgo,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estratega,volar,elasticidad,regeneracion):

                    NuevoPlayer = Players(tipo,sexo,nombre,alterEgo,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estratega,volar,elasticidad,regeneracion)
                    NuevoPlayer.crearPersonaje()
                    Alerta = mb.showinfo(title="Listo", message="Su personaje ha sido almacenado con exito.")
                    a=MenuPrincipal()
                    return a.menuKeingell()


                class Players:
                    def __init__(self,tipo,sexo,nombre,alterEgo,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estratega,volar,elasticidad,regeneracion):
                        self.tipo = tipo
                        self.sexo = sexo
                        self.nombre = nombre
                        self.alter = alterEgo
                        self.velocidad = velocidad
                        self.fuerza = fuerza
                        self.inteligencia = inteligencia
                        self.defensa = defensa
                        self.magia = magia
                        self.telepatia = telepatia
                        self.estrategia = estratega
                        self.volar = volar
                        self.elasticidad = elasticidad
                        self.regeneracion = regeneracion

                    def crearPersonaje(self):
                        info = "Tipo: "+ str(self.tipo) + " | "
                        info += "Genero: "+str(self.sexo)+ " | "
                        info += "Nombre: " + str(self.nombre) + " | "
                        info += "Alter Ego: " + str(self.alter) + " | "
                        info += "Estadisticas: "
                        info += ","+str(self.velocidad)
                        info += ","+str(self.fuerza)
                        info += ","+str(self.inteligencia)
                        info += ","+str(self.defensa)
                        info += ","+str(self.magia)
                        info += ","+str(self.telepatia)
                        info += ","+str(self.estrategia)
                        info += ","+str(self.volar)
                        info += ","+str(self.elasticidad)
                        info += ","+str(self.regeneracion)
                        f = open("Luchadores.txt", 'a')
                        f.write((info+"\n"))
                        f.close()
                        f = open("CantidadesPersonajes.txt", "r")
                        mensaje = f.readlines()
                        try:
                            creados = mensaje[0]
                            creados = int(creados) + 1
                            f.close()
                        except:
                            creados=1
                        f = open("CantidadesPersonajes.txt", "w+")
                        f.write(str(creados))
                        f.close()
                        f = open("MostrarPersonajes.txt", "a+")
                        f.write(str(self.alter) + "\n")
                        f.close()

                        f = open(str(self.alter) + ".txt","a+")
                        f.write(str(self.alter) + "\n"+"0\n"+"0")
                        if (self.tipo == "H"):
                            f = open("Heroes.txt","a+")
                            f.write (str(self.alter) + "\n")
                            f.close()
                        else:
                            f = open("Villanos.txt", "a+")
                            f.write(str(self.alter) + "\n")
                            f.close()

                def mostrarPersonajes():
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    info = ""
                    contador = 1
                    for personaje in mensaje:
                        info += str(contador)+". " + personaje
                        contador += 1
                    return info

                def makeTorneo():
                    ventana.withdraw()
                    def makeTorneo_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        return nombreTorneo()
                    def makeTorneo_auxVolver():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        torneo.withdraw()
                        a=MenuPrincipal()
                        return a.menuKeingell()

                    def verTorneosV1_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        return RegistroPeleas_aux()
                    torneo = tk.Toplevel()
                    imagenVentana = tk.PhotoImage(file="CivilWar4.png")
                    fondoVentana = tk.Label(torneo, image=imagenVentana).place(x=0, y=0)
                    torneo.state("zoomed")
                    torneo.title("Gran Torneo")
                    torneo.config(bg="Black")
                    torneo.config(relief="groove")
                    def on_closing():
                        pygame.mixer.music.stop()
                        torneo.destroy()
                    torneo.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    torneo.config(bd=8)
                    label = tk.Label(torneo, text="Porfavor Ingrese la siguiente información", font=("TimesNewRoman", 20), bg="red",
                                     relief="groove").pack()
                    confirmar = tk.Button(torneo, text="Comenzar", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                          width="30", height="1", cursor="hand2", command=makeTorneo_aux).place(x=520, y=250)
                    Volver = tk.Button(torneo, text="Volver", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                          width="30", height="1", cursor="hand2", command=makeTorneo_auxVolver).place(x=220, y=250)
                    Ver = tk.Button(torneo, text="Ver Torneos", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                       width="30", height="1", cursor="hand2", command=verTorneosV1_aux).place(x=820, y=250)
                    torneo.mainloop()

                def nombreTorneo():
                    def nombreTorneoV1():
                        ventanaNombre.withdraw()
                        return fechaTorneo(nombre.get())
                    ventanaNombre = tk.Toplevel()
                    alto=150
                    ancho=350
                    x_ventana=ventanaNombre.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=pantallaRegistro.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    ventanaNombre.geometry(posicion)
                    imagenVentana = tk.PhotoImage(file="CivilWar5.png")
                    fondoVentana = tk.Label(ventanaNombre, image=imagenVentana).place(x=0, y=0)
                    ventanaNombre.title("GoldenLines")
                    ventanaNombre.config(bg="Black")
                    ventanaNombre.config(relief="groove")
                    ventanaNombre.config(bd=8)
                    def on_closing():
                        Error=mb.showerror(message="Procure no salir hasta terminar el proceso")
                    ventanaNombre.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    label = tk.Label(ventanaNombre, text="Ingrese el nombre de su Torneo ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    nombre = tk.Entry(ventanaNombre, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    nombre.pack()
                    confirmar = tk.Button(ventanaNombre, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=nombreTorneoV1).pack()
                    ventanaNombre.mainloop()

                def fechaTorneo(nombre):
                    def fechaTorneoV1():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaFecha.withdraw()
                        return lugarTorneo(nombre,fecha.get())
                    ventanaFecha = tk.Toplevel()
                    ventanaFecha.geometry("350x150")
                    imagenVentana = tk.PhotoImage(file="CivilWar5.png")
                    fondoVentana = tk.Label(ventanaFecha, image=imagenVentana).place(x=0, y=0)
                    ventanaFecha.title("GoldenLines")
                    ventanaFecha.config(bg="Black")
                    ventanaFecha.config(relief="groove")
                    ventanaFecha.config(bd=8)
                    label = tk.Label(ventanaFecha, text="Ingrese la fecha de su Torneo ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    fecha = tk.Entry(ventanaFecha, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    fecha.pack()
                    confirmar = tk.Button(ventanaFecha, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=fechaTorneoV1).pack()
                    ventanaFecha.mainloop()

                def lugarTorneo(nombre,fecha):
                    def lugarTorneoV1():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanalugar.withdraw()
                        return tipodeTorneo(nombre,fecha,lugar.get())
                    ventanalugar = tk.Toplevel()
                    imagenVentana = tk.PhotoImage(file="CivilWar5.png")
                    fondoVentana = tk.Label(ventanalugar, image=imagenVentana).place(x=0, y=0)
                    alto=150
                    ancho=350
                    x_ventana=ventanalugar.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=ventanalugar.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    ventanalugar.geometry(posicion)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    ventanalugar.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    ventanalugar.title("GoldenLines")
                    ventanalugar.config(bg="Black")
                    ventanalugar.config(relief="groove")
                    ventanalugar.config(bd=8)
                    label = tk.Label(ventanalugar, text="Ingrese el lugar de su Torneo ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    lugar = tk.Entry(ventanalugar, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    lugar.pack()
                    confirmar = tk.Button(ventanalugar, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=lugarTorneoV1).pack()
                    ventanalugar.mainloop()


                def tipodeTorneo(nombre,fecha,lugar):
                    def tipodeTorneoV1Manual():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaTipo.withdraw()
                        return Torneomanual(nombre,fecha,lugar,"Manual")
                    def tipodeTorneoV1PvE():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaTipo.withdraw()
                        return Torneomanual(nombre,fecha,lugar,"PvE")
                    def tipodeTorneoV1EvE():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaTipo.withdraw()
                        return Torneomanual(nombre,fecha,lugar,"EvE")
                    ventanaTipo = tk.Toplevel()
                    alto=150
                    ancho=350
                    x_ventana=ventanaTipo.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=ventanaTipo.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    ventanaTipo.geometry(posicion)
                    imagenVentana = tk.PhotoImage(file="CivilWar6.png")
                    fondoVentana = tk.Label(ventanaTipo, image=imagenVentana).place(x=0, y=0)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    ventanaTipo.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    ventanaTipo.title("GoldenLines")
                    ventanaTipo.config(bg="Black")
                    ventanaTipo.config(relief="groove")
                    ventanaTipo.config(bd=8)
                    label = tk.Label(ventanaTipo, text="  Modo de seleción.  ",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    confirmar = tk.Button(ventanaTipo, text="Manual", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="20", height="1", cursor="hand2", command=tipodeTorneoV1Manual).pack()
                    confirmar = tk.Button(ventanaTipo, text="PvE", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="20", height="1", cursor="hand2", command=tipodeTorneoV1PvE).pack()
                    confirmar = tk.Button(ventanaTipo, text="EvE", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="20", height="1", cursor="hand2", command=tipodeTorneoV1EvE).pack()
                    ventanaTipo.mainloop()

                def Torneomanual(nombre,fecha,lugar,tipo):
                    def TorneomanualV1():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaRounds.withdraw()
                        cantidadRounds = rounds.get()
                        if (int(cantidadRounds)>0) and (int(cantidadRounds)<6):
                            return equipo1V1(nombre,fecha,lugar,tipo,rounds.get(),1,[])
                        else:
                            Alerta = mb.showerror(title="Error", message="El valor ingresado esta fuera de los limites")
                            return Torneomanual(nombre,fecha,lugar,tipo)

                    personajes = mostrarPersonajes()
                    mostrar = tk.Toplevel()
                    mostrar.title("GoldenLines")
                    mostrar.config(bg="Black")
                    mostrar.config(relief="groove")
                    mostrar.config(bd=8)
                    label = tk.Label(mostrar,
                                     text=personajes,
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()

                    ventanaRounds = tk.Toplevel()
                    ventanaRounds.title("GoldenLines")
                    alto=150
                    ancho=350
                    x_ventana=ventanaRounds.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=ventanaRounds.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    ventanaRounds.geometry(posicion)
                    imagenVentana = tk.PhotoImage(file="CivilWar5.png")
                    fondoVentana = tk.Label(ventanaRounds, image=imagenVentana).place(x=0, y=0)
                    ventanaRounds.config(bg="Black")
                    ventanaRounds.config(relief="groove")
                    ventanaRounds.config(bd=8)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    ventanaRounds.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    label = tk.Label(ventanaRounds,
                                     text="Ingrese la cantidad de rounds (Entre 1 y 5).",
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    rounds = tk.Entry(ventanaRounds, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    rounds.pack()
                    confirmar = tk.Button(ventanaRounds, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=TorneomanualV1).pack()
                    ventanaRounds.mainloop()


                def crearEquipo():
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    seleccion = []
                    contador = 0
                    luchas = 5
                    for personaje in mensaje:
                        seleccion += [personaje]

                def equipo1V1(nombre,fecha,lugar,tipo,luchas,numero,equipo):
                    if (tipo == "EvE"):
                        return equipoEvE(nombre,fecha,lugar,tipo,luchas)
                    def retornarequipo1():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaEquipo.withdraw()
                        return equipo1(nombre,fecha,lugar,tipo,luchas,numero,personaje.get(),equipo)
                    ventanaEquipo = tk.Toplevel()
                    ventanaEquipo.title("GoldenLines")
                    alto=150
                    ancho=350
                    x_ventana=ventanaEquipo.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=ventanaEquipo.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    ventanaEquipo.geometry(posicion)
                    imagenVentana = tk.PhotoImage(file="CivilWar5.png")
                    fondoVentana = tk.Label(ventanaEquipo, image=imagenVentana).place(x=0, y=0)
                    ventanaEquipo.config(bg="Black")
                    ventanaEquipo.config(relief="groove")
                    ventanaEquipo.config(bd=8)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    ventanaEquipo.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    label = tk.Label(ventanaEquipo, text="Ingrese el personaje numero " + str(numero)+" de su equipo 1.", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    personaje = tk.Entry(ventanaEquipo, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    personaje.pack()
                    confirmar = tk.Button(ventanaEquipo, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=retornarequipo1).pack()
                    ventanaEquipo.mainloop()

                def equipo1(nombre,fecha,lugar,tipo,luchas,numero,personaje,equipo):
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    seleccion = []
                    for heroe in mensaje:
                        seleccion += [heroe]
                    archivo = nombre +"equipo1.txt"
                    equipo += seleccion[int(personaje)]
                    numero += 1
                    f = open(archivo, 'a+')
                    f.write( seleccion[int(personaje)] + "\n")
                    f.close()
                    if (tipo == "Manual"):
                        if (numero - 1 < int(luchas)):
                            return equipo1V1(nombre,fecha,lugar,tipo,luchas,numero,equipo)
                        if (numero >= int(luchas)):
                            return equipo2V2(nombre,fecha,lugar,tipo,luchas,1,equipo,[])
                    if (tipo == "PvE"):
                        if (numero - 1 < int(luchas)):
                            return equipo1V1(nombre,fecha,lugar,tipo,luchas,numero,equipo)
                        if (numero >= int(luchas)):
                            return equipoPvE(nombre,fecha,lugar,tipo,luchas,equipo,[])

                def equipoPvE(nombre,fecha,lugar,tipo,luchas,equipo,equipo2):
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    lista = sample(mensaje,int(luchas))
                    equipo2 = lista
                    archivo = nombre + "equipo2.txt"
                    f = open(archivo, 'a+')
                    for luchador in equipo2:
                        f.write(luchador + "\n")
                    f.close()
                    return añadirTorneo(nombre,fecha,lugar,tipo,luchas,equipo,equipo2)

                def equipoEvE(nombre,fecha,lugar,tipo,luchas):
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    lista = sample(mensaje, (int(luchas) + int(luchas)))
                    equipo = lista[:int(luchas)]
                    equipo2 = lista[int(luchas):]
                    archivo = nombre + "equipo1.txt"
                    f = open(archivo, 'a+')
                    for luchador in equipo:
                        f.write(luchador + "\n")
                    f.close()

                    archivo2 = nombre + "equipo2.txt"
                    f = open(archivo2, 'a+')
                    for luchador in equipo2:
                        f.write(luchador + "\n")
                    f.close()
                    return añadirTorneo(nombre, fecha, lugar, tipo, luchas, equipo, equipo2)

                def equipo2V2(nombre,fecha,lugar,tipo,luchas,numero,equipo,equipo2):
                    def retornarequipo2():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaEquipo2.withdraw()
                        return equipo22(nombre,fecha,lugar,tipo,luchas,numero,personaje.get(),equipo,equipo2)
                    ventanaEquipo2 = tk.Toplevel()
                    ventanaEquipo2.title("GoldenLines")
                    alto=150
                    ancho=350
                    x_ventana=ventanaEquipo2.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=ventanaEquipo2.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    ventanaEquipo.geometry(posicion)
                    ventanaEquipo2.config(bg="Black")
                    ventanaEquipo2.config(relief="groove")
                    ventanaEquipo2.config(bd=8)
                    def on_closing2():
                        Error=mb.showerror(message="Procure no salir hasta termirnar el proceso")
                    ventanaEquipo2.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    label = tk.Label(ventanaEquipo2, text="Ingrese el personaje numero " + str(numero)+" de su equipo 2.", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    personaje = tk.Entry(ventanaEquipo2, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    personaje.pack()
                    confirmar = tk.Button(ventanaEquipo2, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=retornarequipo2).pack()
                    ventanaEquipo2.mainloop()

                def equipo22(nombre,fecha,lugar,tipo,luchas,numero,personaje,equipo,equipo2):
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    seleccion = []
                    for heroe in mensaje:
                        seleccion += [heroe]
                    archivo = nombre +"equipo2.txt"
                    equipo2 += seleccion[int(personaje)]
                    numero += 1
                    f = open(archivo, 'a+')
                    f.write( seleccion[int(personaje)] + "\n")
                    f.close()

                    if (numero-1 < int(luchas)):
                        return equipo2V2(nombre,fecha,lugar,tipo,luchas,numero,equipo,equipo2)
                    if (numero-1 >= int(luchas)):
                        NuevoTorneo = Torneos(nombre,fecha,lugar,tipo,luchas,equipo,equipo2)
                        NuevoTorneo.crearTorneo()
                        Alerta = mb.showinfo(title="Listo", message="Su torneo ha sido registrado correctamente")
                        a=MenuPrincipal()
                        return a.menuKeingell()


                def añadirTorneo(nombre,fecha,lugar,tipo,luchas,equipo,equipo2):
                    NuevoTorneo = Torneos(nombre, fecha, lugar, tipo, luchas, equipo, equipo2)
                    NuevoTorneo.crearTorneo()
                    Alerta = mb.showinfo(title="Listo", message="Su torneo ha sido registrado correctamente")
                    a=MenuPrincipal()
                    return a.menuKeingell()

                def equipos():
                    f = open("MostrarPersonajes.txt")
                    mensaje = f.readlines()
                    f.close()
                    contador = 1
                    info = ""
                    for personajes in mensaje:
                        info += str(contador) + ". " + personajes
                        info += "\n"
                        contador += 1
                    return info

                def mostrarTorneos():
                    f = open("TorneoCreado.txt")
                    mensaje = f.readlines()
                    f.close()
                    print(mensaje)

                class Torneos:
                    def __init__(self,nombre,fecha,lugar,tipo,luchas,equipo1,equipo2):
                        self.nombre = nombre
                        self.fecha = fecha
                        self.lugar = lugar
                        self.tipo = tipo
                        self.luchas = luchas
                        self.equipo1 = equipo1
                        self.equipo2 = equipo2
                        self.ganador = ""

                    def crearTorneo(self):
                        torneo = "Torneo:"
                        torneo += "\nNombre: "+"\n"+str(self.nombre)
                        torneo += "\nFecha: " + str(self.fecha)
                        torneo += "\nLugar: " + str(self.lugar)
                        torneo += "\nTipo: " + str(self.tipo)
                        torneo += "\nCantidad de Luchas: " + str(self.luchas)
                        torneo += "\n\n"
                        f = open("TorneoCreado.txt","a+")
                        f.write(torneo)
                        f.close()
                        f = open("Cantidades1.txt","r")
                        mensaje = f.readlines()
                        creados = mensaje[0]
                        creados = int(creados) + 1
                        f.close()
                        f = open("Cantidades1.txt", "w+")
                        f.write(str(creados))
                        f.close()
                        f = open(str(self.nombre)+"Torneo.txt","a+")
                        f.write(str(self.nombre)+"\n"+str(self.fecha)+"\n"+str(self.lugar)+"\n"+str(self.luchas))

                def empezarPeleas():
                    clic=pygame.mixer.Sound("click.mp3")
                    clic.play()
                    ventana.withdraw()
                    def empezarPeleas_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        return iniciarTorneo()
                    def Zona():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        error = mb.showerror(title="Error", message="Esta zona esta bajo construcion.")

                    peleas = tk.Toplevel()
                    imagenVentana = tk.PhotoImage(file="CivilWar7.png")
                    fondoVentana = tk.Label(peleas, image=imagenVentana).place(x=0, y=0)
                    peleas.state("zoomed")
                    peleas.title("Gran Torneo")
                    peleas.config(bg="Black")
                    peleas.config(relief="groove")
                    peleas.config(bd=8)
                    def on_closing2():
                        pygame.mixer.music.stop()
                        peleas.destroy()
                    peleas.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    label = tk.Label(peleas, text="Porfavor Ingrese la siguiente información", font=("TimesNewRoman", 20), bg="red",
                                     relief="groove").pack()
                    confirmar = tk.Button(peleas, text="Comenzar", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                          width="30", height="1", cursor="hand2", command=empezarPeleas_aux).place(x=520, y=250)
                    volver = tk.Button(peleas, text="Volver", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                          width="30", height="1", cursor="hand2", command=MenuPrincipal).place(x=220, y=250)
                    Registro = tk.Button(peleas, text="Estadisticas", font=("TimesNewRoman", 12), bd=8, bg="red", relief="groove",
                                       width="30", height="1", cursor="hand2", command=Zona).place(x=820, y=250)
                    peleas.mainloop()

                def RegistroPeleas_aux4():
                    f = open("Torneos.txt")
                    mensaje = f.readlines()
                    f.close()

                    return mensaje

                def RegistroPeleas_aux():
                    Torneos = RegistroPeleas_aux4()
                    mostrar = tk.Toplevel()
                    mostrar.title("GoldenLines")
                    mostrar.config(bg="Black")
                    mostrar.config(relief="groove")
                    mostrar.config(bd=8)
                    label = tk.Label(mostrar,
                                     text=Torneos,
                                     font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    mostrar.mainloop()

                def iniciarTorneo():
                    def iniciarTorneo_aux():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        Torneo.withdraw()
                        return jugarTorneo(nombre.get())
                    Torneo = tk.Toplevel()
                    Torneo.title("GoldenLines")
                    Torneo.config(bg="Black")
                    Torneo.config(relief="groove")
                    Torneo.geometry("350x150")
                    Torneo.config(bd=8)
                    label = tk.Label(Torneo, text="Ingrese el nombre del torneo que\n desea jugar.", font=("TimesNewRoman", 14),
                                     bg="gray",
                                     relief="groove").pack()
                    nombre = tk.Entry(Torneo, font=("TimesNewRoman", 12), bd=8, bg="white", relief="groove")
                    nombre.pack()
                    confirmar = tk.Button(Torneo, text="Confirmar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=iniciarTorneo_aux).pack()
                    Torneo.mainloop()

                def jugarTorneo(nombre):
                    f = open("TorneoCreado.txt")
                    mensaje = f.readlines()
                    f.close()
                    return jugarTorneoV2(nombre,mensaje)

                def jugarTorneoV2(nombre,mensaje):
                    if mensaje==[]:
                        error = mb.showerror(title="Error", message="Este torneo no existe")
                        a=MenuPrincipal()
                        return a.menuKeingell()

                    if(nombre not in mensaje[0]):
                        return jugarTorneoV2(nombre, mensaje[1:])
                    else:
                        return jugarTorneoV1(nombre)

                def jugarTorneoV1(nombre):
                    f = open(str(nombre) +"equipo1.txt")
                    equipo1 = f.readlines()
                    f.close()

                    f = open(str(nombre) + "equipo2.txt")
                    equipo2 = f.readlines()
                    f.close()

                    f = open(str(nombre)+"Torneo.txt")
                    torneo = f.readlines()
                    f.close()

                    return jugarTorneo_aux(nombre,equipo1,equipo2,torneo,1,0,0)

                def jugarTorneo_aux(nombre,equipo1,equipo2,torneo,numero,conteo1,conteo2):
                    luchas = torneo[3]
                    if (numero - 1 == int(luchas)):
                        return Ganador(nombre,equipo1,equipo2,torneo,luchas,conteo1,conteo2)
                    def Iniciar():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        ventanaJugar.withdraw()
                        return partida(nombre,equipo1,equipo2,torneo,numero,luchas,conteo1,conteo2)
                    ventanaJugar = tk.Toplevel()
                    imagenVentana = tk.PhotoImage(file="CivilWar8.png")
                    fondoVentana = tk.Label(ventanaJugar, image=imagenVentana).place(x=0, y=0)
                    ventanaJugar.title("GoldenLines")
                    ventanaJugar.state("zoomed")
                    ventanaJugar.config(bg="Black")
                    ventanaJugar.config(relief="groove")
                    ventanaJugar.config(bd=8)
                    def on_closing2():
                        pygame.mixer.music.stop()
                        ventanalugar.destroy()
                    ventanalugar.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                    label = tk.Label(ventanaJugar, text="Round #"+ str(numero), font=("TimesNewRoman", 20),
                                     bg="red",
                                     relief="groove",bd = 8).pack()
                    label = tk.Label(ventanaJugar, text=equipo1[0], font=("TimesNewRoman", 16),
                                     bg="red",
                                     relief="groove",bd = 8).place(x = 430, y = 180)
                    label = tk.Label(ventanaJugar, text= "VS", font=("TimesNewRoman", 16),
                                     bg="red",
                                     relief="groove",bd = 8).place(x = 650, y = 180)
                    label = tk.Label(ventanaJugar, text=equipo2[0], font=("TimesNewRoman", 16),
                                     bg="red",
                                     relief="groove",bd = 8).place(x = 760, y = 180)
                    confirmar = tk.Button(ventanaJugar, text="Iniciar", font=("TimesNewRoman", 12), bd=8, bg="Gray", relief="groove",
                                          width="30", height="1", cursor="hand2", command=Iniciar).pack()
                    ventanaJugar.mainloop()

                def partida(nombre,equipo1,equipo2,torneo,numero,luchas,conteo1,conteo2):
                    suerte = pruebita()
                    if (numero-1 == int(luchas)):
                        return Ganador(nombre,equipo1,equipo2,torneo,luchas,conteo1,conteo2)
                    if (suerte == 1):
                        conteo1 += 1
                        info = "Luchador1: " +equipo1[0] + "Luchador2: " + equipo2[0] +"Round: "+str(numero)+", Ganador: " +equipo1[0]+ ", Torneo: "+str(nombre) + "\n"
                        f = open("Luchas.txt","a+")
                        f.write(info)
                        f.close()

                        f = open(equipo1[0][:-1]+".txt", "r")
                        mensaje = f.readlines()
                        name = mensaje [0]
                        creados = mensaje[1]
                        creados = int(creados) + 1
                        f.close()
                        f = open(equipo1[0][:-1]+".txt", "w+")
                        f.write(str(name) + "\n"+str(creados))
                        f.close()

                        Alerta = mb.showinfo(title="Listo", message="El ganador de este round es: "+equipo1[0])
                        return jugarTorneo_aux(nombre,equipo1,equipo2,torneo,numero + 1,conteo1,conteo2)
                    if (suerte == 2):
                        conteo2 += 1
                        info = equipo1[0] + ", " + equipo2[0] + ", " + "Round: " + str(numero) + ", Ganador: " + equipo2[
                            0] + ", Torneo: " + str(nombre)
                        f = open("Luchas.txt","a+")
                        f.write(info)
                        f.close()
                        Alerta = mb.showinfo(title="Listo", message="El ganador de este round es: " + equipo2[0])
                        return jugarTorneo_aux(nombre, equipo1, equipo2, torneo, numero + 1, conteo1, conteo2)

                def Ganador(nombre,equipo1,equipo2,torneo,luchas,conteo1,conteo2):
                    def VolverGanador():
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        
                        a=MenuPrincipal()
                        return a.menuKeingell()

                    info = "Nombre del Torneo: " + str(nombre) + "Fecha: " + str(torneo[1]) + "Lugar: "+ str(torneo[0]) + ", Numero de luchas: " + str(luchas) + ", Victorias equipo1 = "+str(conteo1) + ", Victorias equipo2 = "+str(conteo2)
                    f = open("Torneos.txt","a+")
                    f.write(info)
                    f.close()
                    if (int(conteo1) > int(conteo2)):
                        ventanaganador = tk.Toplevel()
                        imagenVentana = tk.PhotoImage(file="trofeo.png")
                        fondoVentana = tk.Label(ventanaganador, image=imagenVentana).place(x=0, y=0)
                        ventanaganador.state("zoomed")
                        ventanaganador.title("GoldenLines")
                        ventanaganador.config(bg="Black")
                        ventanaganador.config(relief="groove")
                        ventanaganador.config(bd=8)
                        ventanalugar.protocol("WM_DELETE_WINDOW", on_closing2)
                    
                        label = tk.Label(ventanaganador, text="El ganador de su Torneo fue el equipo 1", font=("TimesNewRoman", 20),
                                         bg="gold",
                                         relief="groove").pack()
                        confirmar = tk.Button(ventanaEquipo, text="Volver", font=("TimesNewRoman", 12), bd=8, bg="Gray",
                                              relief="groove",
                                              width="30", height="1", cursor="hand2", command=VolverGanador).pack()
                        ventanaganador.mainloop()
                    else:
                        ventanaganador = tk.Toplevel()
                        imagenVentana = tk.PhotoImage(file="trofeo.png")
                        fondoVentana = tk.Label(ventanaganador, image=imagenVentana).place(x=0, y=0)
                        ventanaganador.state("zoomed")
                        ventanaganador.title("GoldenLines")
                        ventanaganador.config(bg="Black")
                        ventanaganador.config(relief="groove")
                        ventanaganador.config(bd=8)
                        label = tk.Label(ventanaganador, text="El ganador de su Torneo fue el equipo 2", font=("TimesNewRoman", 20),
                                         bg="gold",
                                         relief="groove").pack()
                        confirmar = tk.Button(ventanaEquipo, text="Volver", font=("TimesNewRoman", 12), bd=8, bg="Gray",
                                              relief="groove",
                                              width="30", height="1", cursor="hand2", command=VolverGanador).pack()
                        ventanaganador.mainloop()

                def Estadisticas():
                    f = open("Cantidades1.txt","r")
                    torneos = f.readlines()
                    f.close()
                    f = open("CantidadesPersonajes.txt", "r")
                    personajes = f.readlines()
                    f.close()

                ventana=tk.Tk()
                ventana.state("zoomed")
                imagenVentana = tk.PhotoImage(file="FondoPelea.png")
                fondoVentana = tk.Label(ventana, image=imagenVentana).place(x=0, y=0)
                ventana.title("El gran Torneo")
                ventana.config(bg="Black")
                ventana.config(relief="groove")
                ventana.config(bd=8)
                def SalirDelJuego():
                    clic=pygame.mixer.Sound("click.mp3")
                    clic.play()
                    
                    mensaje=mb.showinfo(message="Hasta la próxima")
                    pygame.mixer.music.stop()
                    ventana.destroy()
                    return print("programa()")
                label =tk.Label(ventana, text="Bienvenido porfavor elija una opcion", font=("TimesNewRoman", 20), bg="red" ,relief="groove").pack()
                Personaje=tk.Button(ventana, text="Personajes", font=("TimesNewRoman",14),bd=8, bg="red", width="23",height="1",relief="groove", cursor="hand2",command = crearPersonajes).place(x=244,y=200)
                CrearTorneo=tk.Button(ventana, text="CrearTorneo", font=("TimesNewRoman",14),bd=8, bg="red", width="23",height="1",relief="groove", cursor="hand2",command = makeTorneo).place(x=544, y=200)
                Jugar=tk.Button(ventana, text="Jugar Torneo", font=("TimesNewRoman",14),bd=8, bg="red", width="23",height="1",relief="groove", cursor="hand2",command = empezarPeleas).place(x=844, y=200)
                Salir=tk.Button(ventana, text="Salir", font=("TimesNewRoman",14),bd=8, bg="red", width="23",height="1",relief="groove", cursor="hand2",command = SalirDelJuego).place(x=544, y=300)
                ventana.mainloop()

            #----------------------------------------------------------------------------------------------------
            class login: #Clase que encapsula los modulos de inicio de sesion y registro
                def __init__(self):
                    self.tipo="login"
                def acomodar(self): #Funcion que ayudará más tarde
                    fondodelJuego.config(image=imagen)
                    
                def inicioSesion(self):
                    clic=pygame.mixer.Sound("click.mp3")
                    clic.play()
                    
                    fondo=tk.PhotoImage(file="fondo inicio 2.png")
                    fondodelJuego.config(image=fondo)
                    pantallaLogin=tk.Toplevel()
                    pantallaLogin.title("Inicio de sesión")
                    ancho= 400
                    alto= 500
                    x_ventana=pantallaLogin.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=pantallaLogin.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    pantallaLogin.geometry(posicion)
                    pantallaLogin.resizable(0,1)
                    def on_closing(): #Detecta un cierre de ventana
                        pantallaLogin.destroy()
                        x=login()
                        x.acomodar()
                        
                    pantallaLogin.protocol("WM_DELETE_WINDOW", on_closing) #detecta un cierre de ventana mediante boton de sistema
                    #pantallaLogin.iconbitmap("img.ico")
                    def validar(): #Validación de la contaseña
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                    
                        usuario=user.get()
                        entrada=contra.get()
                        b=funciones()
                        if b.SeEncuentra("contraseña.txt", str(usuario+"|"+entrada))==False:
                            Error.config(text="Error: usuario o contraseña incorrectos")
                        else:
                            Error.config(text=" ")
                            permiso=mb.showinfo(title="Info", message="Acceso concedido")
                            pantallaLogin.destroy()
                            juegoInicio.destroy()
                            return keingell()
                    label1=tk.Label(pantallaLogin, text="Acceso restringido", font=("Times New Roman", 14, "italic")).pack()
                    label2=tk.Label(pantallaLogin, text="Continuar al Torneo", font=("Times New Roman", 12, "italic")).pack()
                    label3=tk.Label(pantallaLogin, text="Usuario", font=("Times New Roman", 14)).place(x=160, y=100)
                    user=tk.Entry(pantallaLogin, font=("Helvetica", 12))
                    user.place(x=100, y=130)
                    label4=tk.Label(pantallaLogin, text="Digite su contraseña", font=("Times New Roman", 14)).place(x=100, y=190)
                    contra=tk.Entry(pantallaLogin, font="Helvetica 12", show="*")
                    contra.place(x=100, y=220)
                    Error=tk.Label(pantallaLogin, text=" ", font="Helvetica 10", fg="red")
                    Error.place(x=100, y=240)
                    valid=tk.Button(pantallaLogin, text="Validar contraseña", font=("Times New Roman",14), bg="gray", width="16",height="1",relief="groove", command=validar, cursor="hand2").place(x=100, y=300)
                    pantallaLogin.mainloop()
                """
                Registro de usuario
                permite a un usuario nuevo registrarse en la plataforma
                E: el nombre, el usuario, una contraseña y la confirmacion de la misma
                S: Los campos se guardan en el archivo "contraseña.txt"
                R: Debe ser una contraseña de 8 caracteres
                    Estas no se pueden repetir, tampoco el nombre de usuario
                """
                def Registro(self):
                    clic=pygame.mixer.Sound("click.mp3")
                    clic.play()
                    fondo=tk.PhotoImage(file="fondo inicio 2.png") 
                    fondodelJuego.config(image=fondo) #cambio de fondo a desenfoque
                    pantallaRegistro=tk.Toplevel()
                    pantallaRegistro.title("Registrarse como usuario")
                    ancho= 400
                    alto= 500
                    x_ventana=pantallaRegistro.winfo_screenwidth() // 2 - ancho// 2
                    y_ventana=pantallaRegistro.winfo_screenheight() // 2 - alto// 2
                    posicion=str(ancho)+"x"+str(alto)+"+"+str(x_ventana)+"+"+str(y_ventana)
                    pantallaRegistro.geometry(posicion)
                    pantallaRegistro.resizable(0,1)
                    def on_closing2():
                        pantallaRegistro.destroy()
                        x=login()
                        x.acomodar()
                    pantallaRegistro.protocol("WM_DELETE_WINDOW", on_closing2)
                    def Registrarse(): #Validación de la contaseña
                        clic=pygame.mixer.Sound("click.mp3")
                        clic.play()
                        usuario=user.get()
                        entrada=contra.get()
                        confirmar=contra2.get()
                        f=open("contraseña.txt", "r")
                        codigo=f.read()
                        b=funciones() #Se llama a las funciones del archivo externo previamente importado
                        datos=b.recopilarDatos(codigo)
                        f.close()
                        
                        if usuario in datos:
                            error.config(text="Este usuario ya existe.")
                        else:
                            error.config(text=" ")
                            if b.contarString(entrada)<8:
                                error.config(text="La contraseña debe tener 8 o más caracteres")
                            else:
                                error.config(text=" ")
                                if entrada!=confirmar:
                                    error.config(text="Las contraseñas son diferentes")
                                else:
                                    error.config(text=" ")
                                    f=open("contraseña.txt", "a")
                                    f.write(str(usuario)+"|"+str(entrada)+"\n")
                                    f.close()
                                    permiso=mb.showinfo(title="Info", message="Registro exitoso\nYa puedes iniciar sesión con tu usuario y contraseña")
                                    pantallaRegistro.destroy()
                        
                    label1=tk.Label(pantallaRegistro, text="Empecemos una historia juntos...", font=("Times New Roman", 14, "italic")).pack()
                    label2=tk.Label(pantallaRegistro, text="Continuar al Torneo", font=("Times New Roman", 12, "italic")).pack()
                    label=tk.Label(pantallaRegistro, text="Cuál es tu nombre", font=("Times New Roman", 14)).place(x=115, y=100)
                    nombre=tk.Entry(pantallaRegistro, font=("Helvetica", 12))
                    nombre.place(x=100, y=130)
                    label3=tk.Label(pantallaRegistro, text="Nombre de Usuario", font=("Times New Roman", 14)).place(x=115, y=170)
                    user=tk.Entry(pantallaRegistro, font=("Helvetica", 12))
                    user.place(x=100, y=200)
                    label4=tk.Label(pantallaRegistro, text="Digite su contraseña", font=("Times New Roman", 14)).place(x=115, y=230)
                    contra=tk.Entry(pantallaRegistro, font="Helvetica 12", show="*")
                    contra.place(x=100, y=260)
                    label5=tk.Label(pantallaRegistro, text="Confirmar contraseña", font=("Times New Roman", 14)).place(x=112, y=290)
                    contra2=tk.Entry(pantallaRegistro, font="Helvetica 12", show="*")
                    contra2.place(x=100, y=320)
                    error=tk.Label(pantallaRegistro, text="                                                                      ", font="Helvetica 10", fg="red")
                    error.place(x=100, y=365)
                    Regis=tk.Button(pantallaRegistro, text="Registrarse", font=("Times New Roman",14), bg="gray", width="16",height="1",relief="groove", command=Registrarse, cursor="hand2").place(x=110, y=390)
                    pantallaRegistro.mainloop()
                def salir(self):
                    clic=pygame.mixer.Sound("click.mp3")
                    clic.play()
                    mensaje=mb.showinfo(title="Despedida", message="Hasta la próxima...")
                    juegoInicio.destroy()
                    pygame.mixer.music.stop()
                    return print("programa()")
            pygame.mixer.music.load("re4.mp3")
            pygame.mixer.music.play(loops=10)
            a=login()
            Login=tk.Button(juegoInicio, text="Iniciar sesión", font=("Times New Roman", 12), width=10, bg="grey", relief="groove", cursor="hand2",command=a.inicioSesion).place(x=628, y=450)
            Registro=tk.Button(juegoInicio, text="Regístrate", font=("Times New Roman", 12), width=10, bg="grey", relief="groove", cursor="hand2", command=a.Registro).place(x=628, y=510)
            salida=tk.Button(juegoInicio, text="Salir", font=("Times New Roman", 12), width=10, bg="grey", relief="groove", cursor="hand2", command=a.salir).place(x=628, y=570)
            juegoInicio.mainloop()
            
        def continuarAJuego(event):
            if event.keysym=="Return":
                a=pygame.mixer.Sound("niña.mp3")
                a.play()
                a.set_volume(0.15)
                return iniciojuego()
            else:
                pantallaCreditos.bind("<Return>", continuarAJuego) 
        label2=tk.Label(pantallaCreditos, text="Presione Enter para continuar", font=("Times New Roman", 11), bg="black", fg="white").pack(pady=10)
        pantallaCreditos.bind("<Return>", continuarAJuego)#Funcion que detecta una entrada por teclado
        pantallaCreditos.mainloop()

    def barra():
        a=pygame.mixer.Sound("click.mp3")
        a.play()
        barra=ttk.Progressbar(inicio, orient=tk.HORIZONTAL, length=450, mode="determinate")
        barra.place(x=469, y=600)
        label=tk.Label(inicio, text="Golpear a tus enemigos provoca más daño que no golpearlos", bg="grey", font=("Helvetica",11,"italic")).place(x=487, y=630)
        boton.config(state=tk.DISABLED)
        boton2.config(state=tk.DISABLED) 
        for x in range(5):
            barra["value"]+=20
            inicio.update_idletasks()
            time.sleep(1)
        return creditos()
    
    boton=tk.Button(inicio, text="Iniciar", font="Helvetica 14", width=10, bg="grey", relief="groove", cursor="hand2", command=barra)
    boton.place(x=628, y=550)
    boton2=tk.Button(inicio, text="Salir", font="Helvetica 14", width=10, bg="grey", relief="groove", cursor="hand2", command=salir)
    boton2.place(x=628, y=595)
    inicio.mainloop()
print(programa())
