import math
class Vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def norme(self):
        n= math.sqrt(self.x**2+self.y**2)
    
        return n
    def somme(self,t):
        self.x+=t.x
        self.y+=t.y

v1 = Vecteur(4,3)
v2 = Vecteur(3,4)
v1.somme(v2)
print(v1.x)
print(v1.y)
