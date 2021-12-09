import math
class Vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def norme(self):
        n= math.sqrt(self.x**2+self.y**2)
    
        return n