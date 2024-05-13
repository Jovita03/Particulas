from Algoritmos import distancia_euclastina
class particulas:
    def __init__(self, ID=0, OrigenX=0, DestinoX=0,OrigenY=0, DestinoY=0, velocidad=0, green=0, red =0, blue=0  ):
        self.__id = ID
        self.__OrigenX = OrigenX
        self.__DestinoX = DestinoX
        self.__OrigenY = OrigenY
        self.__DestinoY = DestinoY
        self.__Distancia = distancia_euclastina(OrigenX, OrigenY, DestinoX,DestinoY)
        self.__velocidad = velocidad
        self.__green = green
        self.__red = red
        self.__blue = blue
    
    def __str__(self):
        return(
            "ID: " + str(self.__id) + '\n' +
            "Origen X: " + str(self.__OrigenX) + '\n' +
            "Destino X: " + str(self.__DestinoX) + '\n' +
            "Origen Y: " + str(self.__OrigenY) + '\n' +
            "Destino Y: " + str(self.__DestinoY) + '\n' +
            "Distancia: " + str(self.__Distancia) + '\n' +
            "Velocidad: " + str(self.__velocidad) + '\n' +
            "Green: " + str(self.__green) + '\n' +
            "Red: " + str(self.__red) + '\n' + 
            "Blue: " + str(self.__blue) + '\n'
        )
    
    def to_dict(self):
        return{
            "ID": self.__id,
            "OrigenX": self.__OrigenX,
            "DestinoX": self.__DestinoX,
            "OrigenY": self.__OrigenY,
            "DestinoY": self.__DestinoY,
            "velocidad": self.__velocidad,
            "green": self.__green,
            "red": self.__red,
            "blue": self.__blue
        }
    
    @property#se utiliza para crear atributos de clase,permite definir métodos 
    #para manipular el acceso, la modificación y la eliminación de los atributos de una clase
    def id(self):
        return str(self.__id)
    
    @property
    def origenx(self):
        return self.__OrigenX
    
    @property
    def destinox(self):
        return self.__DestinoX
    
    @property
    def origeny(self):
        return self.__OrigenY
    
    @property
    def destinoy(self):
        return self.__DestinoY
    
    @property
    def distancia(self):
        return self.__Distancia    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def green(self):
        return self.__green
    
    @property
    def red(self):
        return self.__red
    
    @property
    def blue(self):
        return self.__blue