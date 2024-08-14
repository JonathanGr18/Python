from ClaseParticula import Particula
import json 

class Laboratorio:
    def __init__(self):
        self.__particulas=[]

    def agregarFinal(self, particula:Particula):
        self.__particulas.append(particula)#self realiza que el atributo sea privado de la clase y no sea  un atributo global
    
    def agregarInicio(self, particula:Particula): #vuelo:Vuelo fora que solo entre objetos de tipo vuelo 
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for v in self.__particulas:
            print(v)
        
    def ordID (self):
        self.__particulas.sort(key=lambda particula:particula.fid)
        return self.__particulas

    def ordDist(self):
        self.__particulas.sort(key=lambda particula:particula.fdistancia, reverse=True)
        return self.__particulas

    def ordVel(self):
        self.__particulas.sort(key=lambda particula:particula.fvelocidad)
        return self.__particulas

    def __str__(self)-> str:#Sobrecargar str
        return "".join(str(v)+"\n" for v in self.__particulas)
    
    def __len__(self):#Sobrecargar len
        return(
            len(self.__particulas)
        )
    
    def __iter__(self):
        self.cont=0
        return self
    
    def __next__(self):
        if self.cont<len(self.__particulas):
            parti=self.__particulas[self.cont]
            self.cont+=1
            return parti
        else:#si llega al final
            raise StopIteration#lanzar exepcion para parar for en ventanaProcesos

    def guardarArchivo(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista=[particulas.to_dict() for particulas in self.__particulas]
                json.dump(lista, archivo, indent=4)
                return 1
        except:
            return 0

    def abrirArchivo(self,ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista=json.load(archivo)
                self.__particulas=[Particula(**particula) for particula in lista] #** Relaciona el id con el valor de id (ejemplo)
                return 1    
        except:
            return 0