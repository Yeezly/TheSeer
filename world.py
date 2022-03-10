import random

from room import Room

class world:

    m_rooms = []

    def __init__(self, minX, maxX, minY, maxY, noRooms):
        for i in range(noRooms):
            '''room = Room (random.randint(minX,maxX), random.randint(minY, maxY), 0)'''
            self.m_rooms.append(Room (random.randint(minX,maxX), random.randint(minY, maxY), 0))