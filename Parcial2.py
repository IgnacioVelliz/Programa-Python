import os
os.system('cls')

from math import sqrt

from functools import reduce

class chofer():
    def __init__(self, nombreCompleto):
        
        self.__nombreCompleto = nombreCompleto
    
    def getNombreCompleto(self):
        return self.__nombreCompleto

class camion():
    def __init__(self, patente, litrosDisponibles, ciudadActual, kmLitro, velMaxima):
        
        self.__patente= patente
        self.__litrosDiposnibles= litrosDisponibles
        self.__ciudadActual = ciudadActual
        self.__kmLitro =kmLitro
        self.__velMaxima = velMaxima
    
    def getPatente(self):
        return self.__patente
    
    def getVelMaxima(self):
        return self.__velMaxima
    
    def getCiudadActual(self):
        return self.__ciudadActual
    def setCiudadActual(self, AC):
        self.__ciudadActual = AC
    CiudadActual = property (getCiudadActual, setCiudadActual)
    
    def getLitrosDisponibles(self):
        return self.__litrosDiposnibles
    def setLitrosDisponibles(self, LD):
        self.__litrosDiposnibles = LD
    LitrosDisponibles = property (getLitrosDisponibles, setLitrosDisponibles)
    
    def getKmLitros(self):
        return self.__kmLitro
    
Juan = chofer("Juan Mari")
Martin = chofer("Martin Torres")
Agustin = chofer ("Agustin De Luca")

camion1=camion ("ARG123",60,"Lomas",3, 60)
camion2=camion ("BRZ456",60,"Lanus", 5, 80)
camion3=camion ("URG678",60,"Escalada", 4,60)

def decorador(funcion):
    def nuevaFuncion(*args):
        print("ARCHIVO ABIERTO")
        funcion(*args)
        print("ARCHIVO CERRADO")
    return nuevaFuncion

def cargarRecorrido():  
    destino=[]
    while True:
        ciudades=["Lanus", "Lomas", "Escalada", "Banfield"]
        print("seleccionar ciudades")
        print(f"1= {ciudades[0]}")
        print(f"2= {ciudades[1]}")
        print(f"3= {ciudades[2]}")
        print(f"4= {ciudades[3]}")
        print("0= terminar carga ")
        x=int(input())
        if(x!=0):
            x=x-1
            destino.append(ciudades[x])
            print(destino)
        else:
            break
    return destino

def sumar(x,y):
    return x+y

@decorador
def guardar(estimacion):
    archivo = "ArchivoParcial2.txt"
    while True: 
        try: 
            with open (archivo, "a") as a: 
                a.write(f"\n{estimacion}")  
                print("VIAJE GUARDADO")
                break
        except:
            print("Error al intentar abrir")
            print (f"No se encuentra el archivo {archivo}, especifique su nombre correctamente:")
            archivo = (input("Nombre de archivo:"))
 
@decorador
def leer():   
    archivo = "ArchivoParcial2.txt"
    while True: 
        try: 
            with open (archivo, "r") as a: 
                contenido = a.read()  
                print(contenido)
                break
        except:
            print("Error al intentar abrir")
            print (f"No se encuentra el archivo {archivo}, especifique su nombre correctamente:")
            archivo = (input("Nombre de archivo:"))
            
def estimarViaje(camion, recorrido, chofer):
    
    estimado=["","","","","",""]
    estimado[0]=camion.getPatente()
    estimado[5]=chofer.getNombreCompleto()
    
    d = {
    "Lanus": (40,30),
    "Lomas": (20,10),
    "Banfield": (12,30),
    "Escalada": (10, 34) }
    
    km=[]

    for x in recorrido:
        
        x1=d[camion.CiudadActual][0]
        x2=d[x][0]
        y1=d[camion.CiudadActual][1]
        y2=d[x][1]
        
        resultado= sqrt((x2-x1)**2 + (y2-y1)**2)
        km.append(resultado)
        camion.CiudadActual=x
        

    kmTotal= reduce(sumar, km)
    print(f"total de kilometros: {kmTotal}")
    estimado[1]= f"{kmTotal} kmTotal"
    
    tiempoEstimado= int((kmTotal/camion.getVelMaxima()))
    print(f"tiempo estimado: {tiempoEstimado} hora/s")
    
    paradas=len(recorrido)
    tiempoTotal=tiempoEstimado+paradas
    print(f"tiempo estimado mas paradas: {tiempoTotal} hora/s")
    estimado[2]=f"{tiempoTotal} hora/s"
    
    consumo=int((kmTotal*camion.getKmLitros())/1)
    print("consumo: "+str(consumo))
    
    if(consumo >= camion.LitrosDisponibles):
        print("se requieren mas litros")
        camion.LitrosDisponibles+=1000
        print("se cargaron 1000 litros al camion")
        camion.LitrosDisponibles= camion.LitrosDisponibles-consumo
        estimado[3]="Si Se cargo el tanque"
    else:
        print("no se necesito cargar el tanque")
        camion.LitrosDisponibles= camion.LitrosDisponibles-consumo
        estimado[3]="NO se cargo el tanque"
    
    if(kmTotal>=1000):
        estimado[4]="Si supero los 1000km"    
    else:
        estimado[4]="NO supero los 1000km"
    
    guardar(estimado)        

while True:
    print("seleccione camion")
    print(f"1= {camion1.getPatente()}")
    print(f"2= {camion2.getPatente()}")
    print(f"3= {camion3.getPatente()}")
    print("4= leer resumen")
    print("0= EXIT")
    x = int(input())
    if(x==1):
        print(f"seleccionaste a {camion1.getPatente()}")
        recorrido = cargarRecorrido()
        print (recorrido)
        estimarViaje(camion1, recorrido, Juan)
    elif(x==2):
        print(f"seleccionaste a {camion2.getPatente()}")
        recorrido = cargarRecorrido()
        estimarViaje(camion2,recorrido, Martin)
    elif(x==3):
        print(f"seleccionaste a {camion3.getPatente()}")
        recorrido = cargarRecorrido()
        estimarViaje(camion3, recorrido, Agustin)
    elif(x==4):
        leer()
    elif(x==0):
        break
    else:
        print("valor incorrecto") 
