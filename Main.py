from DHT import *
from HCR import *
from PIR import *
from File import *
import os
import time
newDHT = DHT()
newHCR = HCR()
newPIR = PIR()
newFile = File()
array = []
newFile.readData("Respaldo")
try:
    while True:
        if os.path.isfile("Respaldo2.txt"):
            #print("Existe")
            file = open("Respaldo2.txt","a")
        else:
            #print("No existe")
            file = open("Respaldo2.txt","w")
        newDHT.leerTemperatura()
        newDHT.guardarDatosSQL()
        newDHT.guardarDatosMongo()
        #print(newDHT.retornarDatos())
        newPIR.leerPrescencia()
        newPIR.guardarDatosPIRSQL()
        newPIR.guardarDatosPIRMongo()
        #print(newPIR.retornarDatosPIR())
        newHCR.leerDistancia()
        newHCR.guardarDatosSQL()
        newHCR.guardarDatosMongo()
        #print("Distancia:",newHCR.retornarDistancia(),"cm")
        lista = (newDHT.retornarDatos(),newPIR.retornarDatosPIR(),newHCR.retornarDistancia())
        #file = open("Respaldo2.txt","w")
        file.write(str(lista)+os.linesep)
        array.append(lista)
        for x in array:
            print(x)
        newFile.saveData(x, "Respaldo")
except KeyboardInterrupt:
    print("adios")



