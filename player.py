class Player:
    m_position = 0
    m_life = 0
    m_inventory = 0
    m_room = 0
    def __init__(self):
        self.player_pos = [0, 0]
    def takedamage (self, enemy):
        pass 
#rooms es el lugar donde estas y direction la dirección/comando
    def move(self, rooms, direction):
        
        print ("el jugador se mueve hacia arriba")
    def useitem(self, type):
        pass
    def takeitem (self, rooms):
        pass