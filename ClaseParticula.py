from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id="",origen_x=0,origen_y=0,destino_x=0,destino_y=0,velocidad=0,red=0,green=0,blue=0,distancia=0):#Utilizacion del constructor
        #Iniciar todos los atributo
        self.__id=id
        self.__origenX=origen_x
        self.__origenY=origen_y
        self.__destinoX = destino_x 
        self.__destinoY= destino_y
        self.__velocidad= velocidad
        self.__red= red
        self.__green=green
        self.__blue=blue
        self.__distancia=distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):#retorna una cadena, Es un constructor 
        return(
            "ID: "+self.__id+"\n"+
            "Origen X: "+str(self.__origenX)+"\n"+
            "Origen Y: "+str(self.__origenY)+"\n"+
            "Destino X: "+str(self.__destinoX)+"\n"+
            "Destino Y: "+str(self.__destinoY)+"\n"+
            "Velocidad: "+str(self.__velocidad)+"\n"+
            "Red: "+str(self.__red)+"\n"+
            "Green: "+str(self.__green)+"\n"+
            "Blue: "+str(self.__blue)+"\n"+
            "Distancia: "+str(self.__distancia)+"\n"
        )   
    
    def to_dict(self):
        return{
            "id":self.__id,
            "origen_x":self.__origenX,
            "origen_y":self.__origenY,
            "destino_x":self.__destinoX,
            "destino_y":self.__destinoY,
            "velocidad":self.__velocidad,
            "red":self.__red,
            "green":self.__green,
            "blue":self.__blue,
            "distancia":self.__distancia
        }
    
    @property
    def fid(self): #Getters
        return self.__id
    @property
    def forigenX(self): #Getters
        return self.__origenX
    @property
    def forigenY(self): #Getters
        return self.__origenY
    @property
    def fdestinoX(self): #Getters
        return self.__destinoX
    @property
    def fdestinoY(self): #Getters
        return self.__destinoY
    @property
    def fvelocidad(self): #Getters
        return self.__velocidad
    @property
    def fred(self): #Getters
        return self.__red
    @property
    def fgreen(self): #Getters
        return self.__green
    @property
    def fblue(self): #Getters
        return self.__blue
    @property
    def fdistancia(self): #Getters
        return self.__distancia