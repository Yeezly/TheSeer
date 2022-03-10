from player import Player
from world import world

class App:

    m_player = Player()
    m_world = world (5, 10, 5, 10, 22)

    def __init__(self):
        self.m_comand = ''

    def run(self):
        while 1:
            m_comand = str.lower(input("'w' arriba, 'a' izquierda, 's' abajo, 'd' derecha, 'o' abrir el inventario, 'k' cerrar el inventario: "))
            if m_comand == "w" or m_comand == "a" or m_comand == "s" or m_comand == "d":
                self.m_player.move (self.m_world.m_rooms, self.m_comand)
            elif m_comand == "o":
                print ("el inventario se ha abierto")
            elif m_comand == "k":
                print ("el inventario se ha cerrado")
            
