import random
import math
from typing import Self
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Person:
    MaxDistance = 1.
    MaxIllDistance = 0.1
    
    def __init__(self, x: float, y: float, status: str) -> None:
        self.x = x
        self.y = y
        self.status = status
    
    def move(self) -> None:
        angle = random.uniform(0, 2*math.pi)
        if self.status == "ill":
            distance = random.uniform(0, self.MaxIllDistance)
        else:
            distance = random.uniform(0, self.MaxDistance)
        
        self.x += distance*math.cos(angle)
        self.y += distance*math.sin(angle)

        #trzeba jeszcze ograniczenia na x i y
    
    def info(self) -> str:
        return f"status = {self.status}, position = ({self.x}, {self.y})"
    
    def __str__(self):
        return self.info()
    
    def distance(self, other: Self):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Population:
    InfectionProbability = 0.2
    InfectionDistance = 1.
    
    def __init__(self, count: int, w: float = 100., h: float = 100., ):
        self.people = []
        self.w = w
        self.h = h

        for _ in range(count):
            x = random.uniform(0, w)
            y = random.uniform(0, h)

            if random.random() > self.InfectionProbability:
                status = "healthy"
            elif random.random > 0.5:
                status = "carrier"
            else:
                status = "ill"
            
            self.people.append(Person(x, y, status))
    
    def move(self):
        for person in self.people:
            person.move()
            while person.x > self.w:
                person.x -= self.w
            while person.x < 0:
                person.x += self.w
            while person.y > self.h:
                person.y -= self.h
            while person.y < 0:
                person.y += self.h
        
        for person1 in self.people:
            for person2 in self.people:
                if person1 is not person2 and person1.distance(person2)<self.InfectionDistance:
                    if person1.status != "healthy":
                        if random.random() > 0.5:
                            person2.status = "carrier"
                        else:
                            person2.status = "ill"
    
    def paint(self):
