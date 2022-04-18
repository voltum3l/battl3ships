#Batalla NAVAL

from tkinter import *
from tkinter import messagebox
import random


class BotonesGrilla:
    ubi=[]
    boton=Button()
    clickeado=False
    def __init__(self):
        self.ubi=[]
        self.boton=Button()
        self.clickeado=False
    def EstablecerBoton(self,btn):
        self.boton=btn
    def MostrarBoton(self):
        print(self.boton)
    def EstablecerUbicacion(self,ubicacion):
        self.ubi=ubicacion
    def MostrarUbicacion(self):
        print(self.ubi)
    def DevolverClickeado(self):
        return self.clickeado
    def Clickear(self):
        if self.clickeado==False:
            self.clickeado=True
        else:
            print("El boton ya ha sido clickeado")

class Vehiculos:
    hundido=False
    tamano=0
    ubicacion=[]
    nombre=""
    listasDeBotones=[]
    indiceTocado=0
    def SetName(self,name):
        self.nombre=name
    def DevolverHundido(self):
        return self.hundido
    def TocarVehiculo(self):
        if self.hundido == False:
            self.tamano = self.tamano - 1
            if self.tamano == 0:
                self.hundido=True
                for i in range(len(self.listasDeBotones)):
                    self.listasDeBotones[i].config(text="X")
                    self.listasDeBotones[i].config(bg="red")
            else:
                self.CambiarBotonconX()
    def DevolverUbicacionVehiculo(self):
        return self.ubicacion
    def EstablecerUbicacionVehiculo(self,listaUbicacion):
        self.ubicacion=listaUbicacion
    def AsignarBotonALista(self,boton):
        self.listasDeBotones.append(boton)
    def MostrarListaBotonesEnVehiculo(self):
        print(self.listasDeBotones)
    def CambiarBotonconX(self):
        self.listasDeBotones[self.indiceTocado].config(text="X")
        self.indiceTocado = self.indiceTocado + 1


    def ChequearSiBotonEstaEnLista(self,btn):
        if btn in self.listasDeBotones:
            return True
        else:
            return False

class Submarino(Vehiculos):
    def __init__(self):
        self.listasDeBotones=[]
        self.tamano = 1
        self.ubicacion=[]
        self.indiceTocado = 0
class Destructor(Vehiculos):
    def __init__(self):
        self.listasDeBotones=[]
        self.tamano = 2
        self.ubicacion = []
        self.indiceTocado = 0
class Crucero(Vehiculos):
    def __init__(self):
        self.listasDeBotones=[]
        self.tamano = 3
        self.ubicacion = []
        self.indiceTocado = 0
class Acorazado(Vehiculos):
    def __init__(self):
        self.listasDeBotones=[]
        self.tamano = 4
        self.ubicacion = []
        self.indiceTocado = 0

def CrearVehiculos():
    global submarinos, destructores, cruceros, acorazado
    global grilla

    global submarinosEnemigos, destructoresEnemigos, crucerosEnemigos, acorazadoEnemigos
    global grillaEnemiga

    listaDePosAux=[]
    listaDePosAux.append(PickComplexLocation(2,0))
    acorazado.EstablecerUbicacionVehiculo(listaDePosAux)
    listaDePosAux=[]
    listaDePosAux.append(PickComplexLocation(2,1))
    acorazadoEnemigos.EstablecerUbicacionVehiculo(listaDePosAux)

    for i in range(3):
        destructores.append(Destructor())
        listaDePosAux=[]
        listaDePosAux.append(PickComplexLocation(0,0))
        destructores[i].EstablecerUbicacionVehiculo(listaDePosAux)

    for i in range(3):
        destructoresEnemigos.append(Destructor())
        listaDePosAux=[]
        listaDePosAux.append(PickComplexLocation(0,1))
        destructoresEnemigos[i].EstablecerUbicacionVehiculo(listaDePosAux)

    for i in range(2):
        cruceros.append(Crucero())
        listaDePosAux=[]
        listaDePosAux=PickComplexLocation(1,0)
        cruceros[i].EstablecerUbicacionVehiculo(listaDePosAux)
    for i in range(2):
        crucerosEnemigos.append(Crucero())
        listaDePosAux=[]
        listaDePosAux=PickComplexLocation(1,1)
        crucerosEnemigos[i].EstablecerUbicacionVehiculo(listaDePosAux)

    for i in range(4):
        submarinos.append(Submarino())
        submarinos[i].EstablecerUbicacionVehiculo(PickRandomLocation(0))
        aux=submarinos[i].DevolverUbicacionVehiculo()
        grilla[(aux[0],aux[1])] = True
    for i in range(4):
        submarinosEnemigos.append(Submarino())
        submarinosEnemigos[i].EstablecerUbicacionVehiculo(PickRandomLocation(1))
        aux=submarinosEnemigos[i].DevolverUbicacionVehiculo()
        grillaEnemiga[(aux[0],aux[1])] = True
def GenerarMapa():
    global listaBotones
    global listaBotonesEnemigo

    for x in range(10):
        auxLista = list()
        listaBotones.append(auxLista)

    for x in range(10):
        auxLista2 = list()
        listaBotonesEnemigo.append(auxLista2)

    for x in range(10):
        for y in range(10):
            boton = Button(frame3, width=2, height=1,state=DISABLED)
            boton.grid(row=x, column=y, padx=1, pady=1)
            listaBotones[x].append(boton)
            del (boton)

    for x in range(10):
        for y in range(10):
            botonA = Button(frame8, width=2, height=1)
            botonA.grid(row=x, column=y, padx=1, pady=1)
            listaBotonesEnemigo[x].append(botonA)
            del (botonA)

def FusionGrillaYMapa():
    global listaBotones
    global listaBotonesEnemigo
    global grilla
    global grillaEnemiga

    diccionarioCompleto={}

    listaOrdenada=[]
    for elemento in listaBotones:
        for subElemento in elemento:
         listaOrdenada.append(subElemento)

    contador=0
    for elemento in grilla:
        if contador < 100:
            diccionarioCompleto[elemento]=listaOrdenada[contador]
            contador=contador+1

        if grilla[elemento] == True:
            botonActualizar=diccionarioCompleto[elemento]
            botonActualizar.config(bg="red")
    diccionarioCompleto={}

    listaOrdenada=[]
    for elemento in listaBotonesEnemigo:
        for subElemento in elemento:
         listaOrdenada.append(subElemento)

    contador=0
    for elemento in grillaEnemiga:
        if contador < 100:
            diccionarioCompleto[elemento]=listaOrdenada[contador]
            contador=contador+1

        if grillaEnemiga[elemento] == True:
            botonActualizar=diccionarioCompleto[elemento]
def CompletarDiccionarioGrilla():
    letras=("a","b","c","d","e","f","g","h","i","j")
    global grilla
    global grillaEnemiga
    listaCompleta=list()

    for i in range(100):
        listaCompleta.append("")
    for i in range(100):
        if i < 10:
            listaCompleta[i]=(("a",i))
        elif i < 20:
            listaCompleta[i]=(("b",i-10))
        elif i < 30:
            listaCompleta[i]=(("c",i-20))
        elif i < 40:
            listaCompleta[i]=(("d",i-30))
        elif i < 50:
            listaCompleta[i]=(("e",i-40))
        elif i < 60:
            listaCompleta[i]=(("f",i-50))
        elif i < 70:
            listaCompleta[i]=(("g",i-60))
        elif i < 80:
            listaCompleta[i]=(("h",i-70))
        elif i < 90:
            listaCompleta[i]=(("i",i-80))
        elif i < 100:
            listaCompleta[i]=(("j",i-90))

    for i in range(100):
        grilla[listaCompleta[i]]=False
        grillaEnemiga[listaCompleta[i]]=False
def PickRandomLocation(tipoJugador):
    letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    numbers=[]
    for i in range(10):
        numbers.append(i)
    posicion=(letras[random.randint(0, 9)],random.randint(0, 9))
    condicion=False

    if tipoJugador==0:
        while condicion==False:
            if CheckPosition(posicion,0):
                condicion=True
            else:
                posicion = (letras[random.randint(0, 9)], random.randint(0, 9))
        return posicion
    else:
        while condicion==False:
            if CheckPosition(posicion,1):
                condicion=True
            else:
                posicion = (letras[random.randint(0, 9)], random.randint(0, 9))
        return posicion
def CheckPosition(posicion,tipoJugador):

    global grilla
    global grillaEnemiga

    if tipoJugador==0:
        if grilla[posicion] == False:
            if CheckAdyacentes(posicion,0) == True:
                return True
            else:
                return False
        else:
            return False
    else:
        if grillaEnemiga[posicion] == False:
            if CheckAdyacentes(posicion,1) == True:
                return True
            else:
                return False
        else:
            return False
def CheckAdyacentes(posicion,tipoJugador):

    global grilla
    global grillaEnemiga
    letraAnterior=DevolverAnteriorYPosterior(posicion[0],0)
    letraPosterior=DevolverAnteriorYPosterior(posicion[0],2)

    tupla1=(letraAnterior,posicion[1]-1)
    tupla2=(letraAnterior,posicion[1])
    tupla3=(letraAnterior,posicion[1]+1)
    tupla4=(posicion[0],posicion[1]-1)
    tupla5=(posicion[0],posicion[1]+1)
    tupla6=(letraPosterior,posicion[1]-1)
    tupla7=(letraPosterior,posicion[1])
    tupla8=(letraPosterior,posicion[1]+1)

    listaTuplas=[tupla1,tupla2,tupla3,tupla4,tupla5,tupla6,tupla7,tupla8]
    listaFinal=[]
    for i in range(len(listaTuplas)):
        if listaTuplas[i][0] != "z" and listaTuplas[i][1] != -1 and listaTuplas[i][1] != 10:
            listaFinal.append(listaTuplas[i])

    verificar=True
    if tipoJugador==0:
        for elemento in listaFinal:
            if grilla[elemento] == True:
                verificar=False
    else:
        for elemento in listaFinal:
            if grillaEnemiga[elemento] == True:
                verificar=False

    return verificar
def DevolverAnteriorYPosterior(letra, opcion):
    listaLetras=["a","b","c","d","e","f","g","h","i","j"]
    indice=100
    if letra in listaLetras:
        indice=listaLetras.index(letra)

    if opcion==0:
        if indice != 0 and indice != 100:
            return listaLetras[indice-1]
        else:
            return "z"
    if opcion==2:
        if indice !=9 and indice != 100:
            return listaLetras[indice+1]
        else:
            return "z"
def PickComplexLocation(tipoVehiculo,tipoJugador):

    global grilla
    global grillaEnemiga

    completado=False
    direccion=random.randint(0, 3)
    listaPosiciones=[]
    segPosicion=(0,0)
    terPosicion=(0,0)
    cuarPosicion=(0,0)

    if tipoJugador==0:
        if tipoVehiculo==0:
            while completado == False:
                posicionDePartida = PickRandomLocation(0)
                if VerificarAdyacentesSiguientes(posicionDePartida,direccion,tipoJugador):
                    completado = True
                    listaPosiciones.append(posicionDePartida)
                    grilla[posicionDePartida] = True
                    listaPosiciones.append(TomarDireccionYEstablecerEnGrilla(posicionDePartida,direccion))
                    grilla[TomarDireccionYEstablecerEnGrilla(posicionDePartida,direccion)] = True
        if tipoVehiculo==1:
            while completado == False:
                posicionDePartida = PickRandomLocation(0)
                if VerificarAdyacentesSiguientes(posicionDePartida,direccion,tipoJugador):
                    segPosicion=TomarDireccionYEstablecerEnGrilla(posicionDePartida,direccion)
                    if VerificarAdyacentesSiguientes(segPosicion,direccion,tipoJugador):
                        terPosicion=TomarDireccionYEstablecerEnGrilla(segPosicion,direccion)
                        listaPosiciones.append(posicionDePartida)
                        listaPosiciones.append(segPosicion)
                        listaPosiciones.append(terPosicion)
                        completado = True
                        for elemento in listaPosiciones:
                            grilla[elemento] = True
                del(posicionDePartida)
        if tipoVehiculo==2:
            while completado == False:
                posicionDePartida = PickRandomLocation(0)
                if VerificarAdyacentesSiguientes(posicionDePartida,direccion,tipoJugador):
                    segPosicion=TomarDireccionYEstablecerEnGrilla(posicionDePartida,direccion)
                    if VerificarAdyacentesSiguientes(segPosicion,direccion,tipoJugador):
                        terPosicion=TomarDireccionYEstablecerEnGrilla(segPosicion,direccion)
                        if VerificarAdyacentesSiguientes(terPosicion,direccion,tipoJugador):
                            cuarPosicion=TomarDireccionYEstablecerEnGrilla(terPosicion,direccion)
                            listaPosiciones.append(posicionDePartida)
                            listaPosiciones.append(segPosicion)
                            listaPosiciones.append(terPosicion)
                            listaPosiciones.append(cuarPosicion)
                            completado = True
                            for elemento in listaPosiciones:
                                grilla[elemento] = True

    else:
        if tipoVehiculo == 0:
            while completado == False:
                posicionDePartida = PickRandomLocation(1)
                if VerificarAdyacentesSiguientes(posicionDePartida, direccion,tipoJugador):
                    completado = True
                    listaPosiciones.append(posicionDePartida)
                    grillaEnemiga[posicionDePartida] = True
                    listaPosiciones.append(TomarDireccionYEstablecerEnGrilla(posicionDePartida, direccion))
                    grillaEnemiga[TomarDireccionYEstablecerEnGrilla(posicionDePartida, direccion)] = True
        if tipoVehiculo == 1:
            while completado == False:
                posicionDePartida = PickRandomLocation(1)
                if VerificarAdyacentesSiguientes(posicionDePartida, direccion,tipoJugador):
                    segPosicion = TomarDireccionYEstablecerEnGrilla(posicionDePartida, direccion)
                    if VerificarAdyacentesSiguientes(segPosicion, direccion,tipoJugador):
                        terPosicion = TomarDireccionYEstablecerEnGrilla(segPosicion, direccion)
                        listaPosiciones.append(posicionDePartida)
                        listaPosiciones.append(segPosicion)
                        listaPosiciones.append(terPosicion)
                        completado = True
                        for elemento in listaPosiciones:
                            grillaEnemiga[elemento] = True
        if tipoVehiculo == 2:
            while completado == False:
                posicionDePartida = PickRandomLocation(1)
                if VerificarAdyacentesSiguientes(posicionDePartida, direccion,tipoJugador):
                    segPosicion = TomarDireccionYEstablecerEnGrilla(posicionDePartida, direccion)
                    if VerificarAdyacentesSiguientes(segPosicion, direccion,tipoJugador):
                        terPosicion = TomarDireccionYEstablecerEnGrilla(segPosicion, direccion)
                        if VerificarAdyacentesSiguientes(terPosicion, direccion,tipoJugador):
                            cuarPosicion = TomarDireccionYEstablecerEnGrilla(terPosicion, direccion)
                            listaPosiciones.append(posicionDePartida)
                            listaPosiciones.append(segPosicion)
                            listaPosiciones.append(terPosicion)
                            listaPosiciones.append(cuarPosicion)
                            completado = True
                            for elemento in listaPosiciones:
                                grillaEnemiga[elemento] = True

    return listaPosiciones
def TomarDireccionYEstablecerEnGrilla(tupla,direccion):

    letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    indiceLetras = letras.index(tupla[0])

    if direccion == 0:
        tuplaAuxiliar=(letras[indiceLetras-1],tupla[1])
    if direccion == 1:
        tuplaAuxiliar=(letras[indiceLetras+1],tupla[1])
    if direccion == 2:
        tuplaAuxiliar=(tupla[0],tupla[1]-1)
    if direccion == 3:
        tuplaAuxiliar=(tupla[0],tupla[1]+1)

    return tuplaAuxiliar
def VerificarAdyacentesSiguientes(pos,dir,tipoJugador):

    letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    indiceLetras=letras.index(pos[0])

    retorno=False
    if dir==0:
        if indiceLetras > 0:
            tuplaAux=(letras[indiceLetras-1],pos[1])
            if CheckAdyacentes(tuplaAux,tipoJugador):
                retorno = True

    if dir==1:
        if indiceLetras < 9:
            tuplaAux=(letras[indiceLetras+1],pos[1])
            if CheckAdyacentes(tuplaAux,tipoJugador):
                retorno = True

    if dir==2:
        if pos[1] > 0:
            tuplaAux=(pos[0],pos[1]-1)
            if CheckAdyacentes(tuplaAux,tipoJugador):
                retorno = True

    if dir ==3:
        if pos[1] < 9:
            tuplaAux=(pos[0],pos[1]+1)
            if CheckAdyacentes(tuplaAux,tipoJugador):
                retorno = True

    return retorno

def PasarGrillaEnemigoAGrillaAuxiliar():
    global grillaEnemiga
    global grillaAuxiliar
    global listaBotonesEnemigo

    HacerListaBotonesPlayerBien()
    listaAux=[]
    for elemento in grillaEnemiga:
        grillaAuxiliar.append(elemento)

    for elemento in listaBotonesEnemigo:
        for subelemento in elemento:
            listaAux.append(subelemento)
    listaBotonesEnemigo=listaAux
    for elemento in listaBotonesEnemigo:
        aux2 = grillaAuxiliar.pop(0)
        ClickAGrillaEnemiga(elemento,aux2)
def ClickAGrillaEnemiga(a1,a2):
    a1.config(command=lambda:CheckMe(a1,a2))

def CheckMe(boton,posicionTiro):
    global grillaAuxiliar
    global tirosEjecutadosPorEnemigo
    global tirosEjecutadosPorJugador
    global submarinosEnemigos, crucerosEnemigos, destructoresEnemigos, acorazadoEnemigos
    global listaBotonesEnemigo
    global turnoJugador
    global grilla
    global grillaEnemiga

    if turnoJugador:
        listaVehiculos=[]
        for elemento in submarinosEnemigos:
            listaVehiculos.append(elemento)
        for elemento in crucerosEnemigos:
            listaVehiculos.append(elemento)
        for elemento in destructoresEnemigos:
            listaVehiculos.append(elemento)
        listaVehiculos.append(acorazadoEnemigos)

        if posicionTiro in tirosEjecutadosPorJugador:
            print("ese tiro ya se ha realizado.")
        else:
            tirosEjecutadosPorJugador.append(posicionTiro)
            if grillaEnemiga[posicionTiro]==True:
                GolpearVehiculo(posicionTiro,0)
                boton.config(text="X",bg="red",state=DISABLED)
            else:
                boton.config(text="0",bg="light blue",state=DISABLED)
            turnoJugador=False
            ActualizarBotones()
    else:
        MaquinaEligiendoDondeGolpear()

def GolpearVehiculo(posicion,opcion):

    global submarinosEnemigos, destructoresEnemigos, crucerosEnemigos, acorazadoEnemigos
    global submarinos, destructores, cruceros, acorazado
    global golpeEfectivo

    global vehiculosHundidosPorJugador
    global vehiculosHundidosPorJugador


    if opcion == 0:
        for elemento in submarinosEnemigos:
            lista1=elemento.DevolverUbicacionVehiculo()
            if posicion == lista1:
                elemento.TocarVehiculo()
                vehiculosHundidosPorJugador.append(1)

        for elemento in destructoresEnemigos:
            lista2=elemento.DevolverUbicacionVehiculo()
            for subelemento in lista2:
                if posicion in subelemento:
                    elemento.TocarVehiculo()
                    if elemento.DevolverHundido():
                        vehiculosHundidosPorJugador.append(1)

        for elemento in crucerosEnemigos:
            lista3=elemento.DevolverUbicacionVehiculo()
            if posicion in lista3:
                elemento.TocarVehiculo()
                if elemento.DevolverHundido():
                    vehiculosHundidosPorJugador.append(1)

        lista4=acorazadoEnemigos.DevolverUbicacionVehiculo()
        for elemento in lista4:
            if posicion in elemento:
                acorazadoEnemigos.TocarVehiculo()
                if acorazadoEnemigos.DevolverHundido():
                    vehiculosHundidosPorJugador.append(1)

    else:
        for elemento in submarinos:
            lista1 = elemento.DevolverUbicacionVehiculo()
            if posicion == lista1:
                elemento.TocarVehiculo()
                vehiculosHundidosPorMaquina.append(1)
                golpeEfectivo=False

        for elemento in destructores:
            lista2 = elemento.DevolverUbicacionVehiculo()
            for subelemento in lista2:
                if posicion in subelemento:
                    elemento.TocarVehiculo()
                    if elemento.DevolverHundido():
                        vehiculosHundidosPorMaquina.append(1)
                        golpeEfectivo = False

        for elemento in cruceros:
            lista3 = elemento.DevolverUbicacionVehiculo()
            if posicion in lista3:
                elemento.TocarVehiculo()
                if elemento.DevolverHundido():
                    vehiculosHundidosPorMaquina.append(1)
                    golpeEfectivo = False

        lista4 = acorazado.DevolverUbicacionVehiculo()
        for elemento in lista4:
            if posicion in elemento:
                acorazado.TocarVehiculo()
                if acorazado.DevolverHundido():
                    vehiculosHundidosPorMaquina.append(1)
                    golpeEfectivo=False

    ChequearFinalJuego()
    
def HacerListaBotonesPlayerBien():
    global listaBotonesPlayer
    global listaBotones
    global grilla
    global posANDbotones

    for elemento in listaBotones:
        for subelemento in elemento:
            listaBotonesPlayer.append(subelemento)

    posANDbotones=dict(zip(grilla.keys(),listaBotonesPlayer))
def MaquinaEligiendoDondeGolpear():
    global tirosEjecutadosPorEnemigo
    global posANDbotones
    global grilla
    global submarinos,cruceros,destructores,acorazado
    global turnoJugador
    global golpeEfectivo
    global listaParaHundir

    letras=["a","b","c","d","e","f","g","h","i","j"]


    if golpeEfectivo:
        posicionRandom=HastaHundir()
    else:
        BorrarListasYDatos()
        posicionRandom = (letras[random.randint(0, 9)], random.randint(0, 9))

    if posicionRandom not in tirosEjecutadosPorEnemigo:
        tirosEjecutadosPorEnemigo.append(posicionRandom)
        btn=posANDbotones[posicionRandom]
        if grilla[posicionRandom] == True:
            golpeEfectivo = True
            GolpearVehiculo(posicionRandom,1)
            listaParaHundir.append(posicionRandom)
            btn.config(text="X",bg="black",fg="white",state=DISABLED)

        else:
            btn.config(text="X",bg="light blue",state=DISABLED)
        turnoJugador=True
        ActualizarBotones()
    else:
        MaquinaEligiendoDondeGolpear()
def PressingButtons(num):
    global turnoJugador
    if num==0:
        messagebox.showinfo(message="Tiene que elegir una casilla donde hacer el tiro.", title="Mensaje")
    if num==1:
        MaquinaEligiendoDondeGolpear()

    ActualizarBotones()
def ActualizarBotones():
    global botonTurnoMaquina,botonTurnoJugador
    if turnoJugador:
        botonTurnoJugador.config(state=NORMAL)
        botonTurnoMaquina.config(state=DISABLED)
    else:
        botonTurnoJugador.config(state=DISABLED)
        botonTurnoMaquina.config(state=NORMAL)
def BorrarListasYDatos():
    global listaParaHundir
    global listaDirecciones

    listaParaHundir=[]
    listaDirecciones=[]
def HastaHundir():
    global tirosEjecutadosPorEnemigo
    global listaParaHundir
    global listaDirecciones
    global grilla

    ultimaPosicionCorrecta=listaParaHundir[-1]
    posicionOriginal=listaParaHundir[0]

    if len(listaDirecciones) == 0:
        while len(listaDirecciones) != 4:
            num = random.randint(0, 3)
            if num not in listaDirecciones:
                listaDirecciones.append(num)

    direccion=listaDirecciones[0]

    if ChequearSiSePuedeEnEsaDireccion(ultimaPosicionCorrecta,direccion) == False:
        listaDirecciones.pop(0)
        direccion=listaDirecciones[0]

    nuevaPosicion=TomarDireccionYEstablecerEnGrilla(ultimaPosicionCorrecta,direccion)

    if grilla[nuevaPosicion] == False:
        listaDirecciones.pop(0)
        listaParaHundir.append(posicionOriginal)

    return(nuevaPosicion)
def ChequearSiSePuedeEnEsaDireccion(posicion,direccion):
    verificar=True
    if direccion==0:
        if posicion[0] == "a":
            verificar=False
    if direccion==1:
        if posicion[0] == "j":
            verificar=False
    if direccion==2:
        if posicion[1] == 0:
            verificar=False
    if direccion==3:
        if posicion[1] == 9:
            verificar=False
    return verificar

def ChequearFinalJuego():
    global vehiculosHundidosPorJugador
    global vehiculosHundidosPorJugador

    if len(vehiculosHundidosPorJugador) == 10:
        messagebox.showinfo(title="Juego TERMINADO", message="El JUGADOR ha ganado")

    if len(vehiculosHundidosPorMaquina) == 10:
        messagebox.showinfo(title="Juego TERMINADO", message="El JUGADOR ha ganado")


#Creación Variables Globales
submarinos=[]
destructores=[]
cruceros=[]
acorazado=Acorazado()

submarinosEnemigos=[]
destructoresEnemigos=[]
crucerosEnemigos=[]
acorazadoEnemigos=Acorazado()


botoneraParaEnemigos=[]
listaBotones=list()
listaBotonesPlayer=list()
listaBotonesEnemigo=list()
posANDbotones={}
colocacionVehiculos= {}
grilla={}
grillaEnemiga={}
grillaAuxiliar=[]

tirosEjecutadosPorEnemigo=[]
tirosEjecutadosPorJugador=[]
turnoJugador=True
golpeEfectivo=False
listaParaHundir=[]
listaDirecciones=[]
vehiculosHundidosPorJugador=[]
vehiculosHundidosPorMaquina=[]

CompletarDiccionarioGrilla()
CrearVehiculos()

#Fin Creacion Variables Globales

root = Tk()
root.title("Batalla Naval")
root.config(bg="blue")

#Frame1 - Numeros
frame1=Frame(root)
frame1.config(width="400",height="10",bg="green")
frame1.grid(row=0,column=1,sticky=S)
for x in range(10):
    boton=Button(frame1,text=x+1,width=2,height=1,fg="yellow",bg="black")
    boton.grid(row=0,column=x,padx=1,sticky=S)

#Frame2 - Letras
frame2=Frame(root)
frame2.config(width="10",height="400",bg="green")
frame2.grid(row=1,column=0,stick=E)

letrasAux = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
for x in range(10):
    botonb=Button(frame2,text=letrasAux[x],fg="yellow",bg="black",width=2,height=1)
    botonb.grid(row=x,column=0,pady=1,sticky=E)

#Frame3 -> Contiene los casilleros.
frame3=Frame(root)
frame3.config(width="400",height="450",bg="black")
frame3.grid(row=1,column=1)

#Frame4 -> Informacion sobre MIS BARCOS
frame4=Frame(root)
frame4.config(width="400",height="250",bg="blue")
frame4.grid(row=1,column=3,padx=10)
labelJugador=Label(frame4, text="JUGADOR",fg="white",bg="green",font=40)
labelJugador.grid(row=0,column=0,sticky=W)
labelEspacio=Label(frame4,text="            ",bg="blue")
labelEspacio.grid(row=1,column=0,sticky=W)
labelSubmarinos=Label(frame4,text="Submarinos",fg="yellow",bg="red",font=15)
labelSubmarinos.grid(row=2,column=0,sticky=NSEW,padx=3)
labelDestructores=Label(frame4,text="Destructores",fg="yellow",bg="red",font=15)
labelDestructores.grid(row=3,column=0,sticky=NSEW,padx=3)
labelCruceros=Label(frame4,text="Cruceros",fg="yellow",bg="red",font=15)
labelCruceros.grid(row=4,column=0,sticky=NSEW,padx=3)
labelAcorazado=Label(frame4,text="Acorazado",fg="yellow",bg="red",font=15)
labelAcorazado.grid(row=5,column=0,sticky=NSEW,padx=3)

#Frame5 -> Separador
frame5=Frame(root)
frame5=Frame(root)
frame5.config(width="400",height="8",bg="orange")
frame5.grid(row=6,column=0,columnspan=4,pady=12)

#Frame6 - Numeros Enemigos
frame6=Frame(root)
frame6.config(width="400",height="10",bg="green")
frame6.grid(row=8,column=1,sticky=S)
for x in range(10):
    botonx=Button(frame6,text=x+1,width=2,height=1,fg="yellow",bg="black")
    botonx.grid(row=0,column=x,padx=1,sticky=S)

#Frame7 - Letras Enemigas
frame7=Frame(root)
frame7.config(width="10",height="400",bg="green")
frame7.grid(row=9,column=0,stick=E)

letrasAux = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
for x in range(10):
    botonc=Button(frame7,text=letrasAux[x],fg="yellow",bg="black",width=2,height=1)
    botonc.grid(row=x,column=0,pady=1,sticky=E)

#Frame8 - Grilla Enemiga
frame8=Frame(root)
frame8.config(width="400",height="450",bg="green")
frame8.grid(row=9,column=1)

#Frame9 -> Informacion sobre BARCOS ENEMIGOS
frame9=Frame(root)
frame9.config(width="400",height="250",bg="blue")
frame9.grid(row=9,column=3,padx=10)
labelMaquina=Label(frame9, text="MAQUINA",fg="white",bg="green",font=40)
labelMaquina.grid(row=0,column=0,sticky=W)
labelEspacio2=Label(frame9,text="            ",bg="blue")
labelEspacio2.grid(row=1,column=0,sticky=W)
labelEnemigosSubmarinos=Label(frame9,text="Submarinos",fg="yellow",bg="red",font=15)
labelEnemigosSubmarinos.grid(row=2,column=0,sticky=NSEW,padx=3)
labelEnemigoDestructores=Label(frame9,text="Destructores",fg="yellow",bg="red",font=15)
labelEnemigoDestructores.grid(row=3,column=0,sticky=NSEW,padx=3)
labelEnemigoCruceros=Label(frame9,text="Cruceros",fg="yellow",bg="red",font=15)
labelEnemigoCruceros.grid(row=4,column=0,sticky=NSEW,padx=3)
labelEnemigoAcorazado=Label(frame9,text="Acorazado",fg="yellow",bg="red",font=15)
labelEnemigoAcorazado.grid(row=5,column=0,sticky=NSEW,padx=3)

#Frame10 -> Separador
frame10=Frame(root)
frame10.config(width="400",height="8",bg="orange")
frame10.grid(row=10,column=0,columnspan=4,pady=12)

#Frame10 -> NEXT TURN
frame11=Frame(root)
frame11.config(width="200",height="800",bg="blue")
frame11.grid(row=12,column=0,columnspan=8,pady=5)

botonTurnoJugador=Button(frame11,text="Turno Jugador",fg="yellow",bg="black", width=14,height=5,font=13,state=NORMAL)
botonTurnoJugador.config(command=lambda:PressingButtons(0))
botonTurnoJugador.grid(row=0,column=0,padx=10,sticky=E)
botonTurnoMaquina=Button(frame11,text="Turno Maquina",fg="white",bg="black", width=14,height=5,font=13,state=DISABLED)
botonTurnoMaquina.config(command=lambda:PressingButtons(1))
botonTurnoMaquina.grid(row=0,column=1,padx=10,sticky=W)

randomTurnoInicial=random.randint(0, 1)
if randomTurnoInicial==0:
    turnoJugador=True
else:
    turnoJugador=False
ActualizarBotones()


###################################################################################
#SUBMARINOS -> 7 espacios (1-x-1-x-1-x-1)
botonesPlayerSubmarinos=[]
for i in range(7):
    boton=Button(frame4,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=2,column=i+1)
    botonesPlayerSubmarinos.append(boton)
    del (boton)
contadorSubmarinos=0
for i in range(7):
    if i % 2 != 0:
        botonesPlayerSubmarinos[i].config(bg="blue")
        contadorSubmarinos=contadorSubmarinos+1
    else:
        submarinos[contadorSubmarinos].AsignarBotonALista(botonesPlayerSubmarinos[i])
#DESTRUCTORES -> 8 espacios (1-1-x-1-1-x-1-1)
botonesPlayerDestructores=[]
for i in range(8):
    boton=Button(frame4,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=3,column=i+1)
    botonesPlayerDestructores.append(boton)
    del(boton)
contador=0
contadorDestructores=0
for i in range(8):
    if contador==2:
        botonesPlayerDestructores[i].config(bg="blue")
        contadorDestructores=contadorDestructores+1
        contador=0
    else:
        contador=contador+1
        destructores[contadorDestructores].AsignarBotonALista(botonesPlayerDestructores[i])
#CRUCEROS -> 7 espacios (1-1-1-x-1-1-1)
botonesPlayerCruceros=[]
for i in range(7):
    boton=Button(frame4,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=4,column=i+1)
    botonesPlayerCruceros.append(boton)
    del(boton)
contador=0
contadorCruceros=0
for i in range(7):
    if contador==3:
        botonesPlayerCruceros[i].config(bg="blue")
        contador=0
        contadorCruceros=contadorCruceros+1
    else:
        contador=contador+1
        cruceros[contadorCruceros].AsignarBotonALista(botonesPlayerCruceros[i])

#ACORAZADO -> 4 espacios
botonPlayerAcorazado=[]
for i in range(4):
    boton=Button(frame4,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=5,column=i+1)
    botonPlayerAcorazado.append(boton)
    acorazado.AsignarBotonALista(boton)
    del(boton)


GenerarMapa()
FusionGrillaYMapa()

#Botones ENEMIGOS
botonesEnemigoSubmarinos=[]
for i in range(7):
    boton=Button(frame9,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=2,column=i+1)
    botonesEnemigoSubmarinos.append(boton)
    del (boton)
contadorSubmarinos=0
for i in range(7):
    if i % 2 != 0:
        botonesEnemigoSubmarinos[i].config(bg="blue")
        contadorSubmarinos=contadorSubmarinos+1
    else:
        submarinosEnemigos[contadorSubmarinos].AsignarBotonALista(botonesEnemigoSubmarinos[i])

botonesEnemigoDestructores=[]
for i in range(8):
    boton=Button(frame9,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=3,column=i+1)
    botonesEnemigoDestructores.append(boton)
    del(boton)
contador=0
contadorDestructores=0
for i in range(8):
    if contador==2:
        botonesEnemigoDestructores[i].config(bg="blue")
        contadorDestructores=contadorDestructores+1
        contador=0
    else:
        contador=contador+1
        destructoresEnemigos[contadorDestructores].AsignarBotonALista(botonesEnemigoDestructores[i])
botonesEnemigoCruceros=[]
for i in range(7):
    boton=Button(frame9,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=4,column=i+1)
    botonesEnemigoCruceros.append(boton)
    del(boton)
contador=0
contadorCruceros=0
for i in range(7):
    if contador==3:
        botonesEnemigoCruceros[i].config(bg="blue")
        contador=0
        contadorCruceros=contadorCruceros+1
    else:
        contador=contador+1
        crucerosEnemigos[contadorCruceros].AsignarBotonALista(botonesEnemigoCruceros[i])
botonEnemigoAcorazado=[]
for i in range(4):
    boton=Button(frame9,fg="grey",width=2,height=1,state=DISABLED)
    boton.grid(row=5,column=i+1)
    botonEnemigoAcorazado.append(boton)
    acorazadoEnemigos.AsignarBotonALista(boton)
    del(boton)

PasarGrillaEnemigoAGrillaAuxiliar()

root.mainloop()

