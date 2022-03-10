import random

class Room:

    m_terrain = [] #matriz
    room = []
                                    #valores en celdas
    def __init__(self, sizeX, sizeY, value):
        m_terrain = [[value for i in range(sizeX)] for j in range(sizeY)]
        '''m_counter = 0
        m_randomize = random.randint(5,10)
        m_size = [0] * m_randomize
        for i in range(m_randomize):
            m_size[i] = [0] * m_randomize
        print (m_size)'''