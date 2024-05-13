from Particulas import particulas 
import json 
class funciones: 
    def __init__(self):
        self.__particulas=[]

    def agregar_final(self, particula:particulas):
        self.__particulas.append(particula)
        
    def agregar_inicio(self, particula:particulas):
        self.__particulas.insert(0,particula)
 
    def mostrar(self):
        for p in self.__particulas:
            print(p)
            
    def __str__(self): 
        return "".join(
             str(i) + "\n" for i in self.__particulas)
   
    def guardar(self, ubicacion):
        try: 
            with open(ubicacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista,archivo, indent=5) 
                return 1 
        except:
            return 0
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                if 'ID' in lista[0]:  # Verifica si el archivo tiene el primer formato
                    self.__particulas= [particulas(
                        ID=particula['ID'],
                        OrigenX=particula['OrigenX'],
                        DestinoX=particula['DestinoX'],
                        OrigenY=particula['OrigenY'],
                        DestinoY=particula['DestinoY'],
                        velocidad=particula['velocidad'],
                        green=particula['green'],
                        red=particula['red'],
                        blue=particula['blue']
                    ) for particula in lista]
                elif 'id' in lista[0] and 'origen' in lista[0]:  # Verifica si el archivo tiene el segundo formato
                    self.__particulas= [particulas(
                        ID=particula['id'],
                        OrigenX=particula['origen']['x'],
                        DestinoX=particula['destino']['x'],
                        OrigenY=particula['origen']['y'],
                        DestinoY=particula['destino']['y'],
                        velocidad=particula['velocidad'],
                        green=particula['color']['green'],
                        red=particula['color']['red'],
                        blue=particula['color']['blue']
                    ) for particula in lista]
                else:  # Si no es ninguno de los dos formatos anteriores, asume que es el tercer formato
                    self.__particulas= [particulas(
                        ID=particula['id'],
                        OrigenX=particula['origen_x'],
                        DestinoX=particula['destino_x'],
                        OrigenY=particula['origen_y'],
                        DestinoY=particula['destino_y'],
                        velocidad=particula['velocidad'],
                        green=particula['green'],
                        red=particula['red'],
                        blue=particula['blue']
                    ) for particula in lista]
                return 1
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            return 0

        
    def __len__(self):
        return(
            len(self.__particulas)
        )
    
    def __iter__(self):
        self.cont = 0
        
        return self
        
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont] 
            self.cont +=1
            return particula
        else:
            raise StopIteration 
    
    def sort_by_id(self): 
        self.__particulas.sort(key=lambda particula: int(particula.id))
    def sort_by_distancia(self):
        self.__particulas.sort(key= lambda particula: particula.distancia, reverse=True)

    def sort_by_velocidad(self):
        self.__particulas.sort(key= lambda particula: particula.velocidad)