import numpy as np
import random

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, idx):
        if idx == 0: return self.x
        elif idx == 1: return self.y
        else:
            raise IndexError('Index out of bound')
    def __setitem__(self, idx, other):
        if idx == 0: self.x = other
        elif idx == 1: self.y = other
        else:
            raise IndexError('Index out of bound')            

    def __add__(self, other: "Vector | int | float") -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        
        elif isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        
        else:
            raise TypeError('Summation is only allowed between vectors, or vector and scaler')
        
    def __radd__(self, other: "Vector | int | float") -> 'Vector':
        return self.__add__(other)
    

    def __sub__(self, other: "Vector | int | float") -> 'Vector':

        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        
        elif isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        
        else:
            raise TypeError('Subtraction is only allowed between vectors, or vector and scalar')
        
    def __rsub__(self, other: "Vector | int | float") -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(other - self.x, other - self.y)
        
        elif isinstance(other, Vector):
            return Vector(other.x - self.x, other.y - self.y)
        
        else:
            raise TypeError('Subtraction is only allowed between vectors, or vector and scalar')      
        

    def __mul__(self, other: 'Vector | int | float') -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            raise TypeError('Multiplication is only allowed between vectors, or vector and scalar')

    def __rmul__(self, other: 'Vector | int | float') -> 'Vector':
        return self.__mul__(other)
    

    def __matmul__(self, other: 'Vector') -> float:
        if not isinstance(other, Vector):
            raise TypeError('Dot product is only allowed between vectors')
        return self.x * other.x + self.y * other.y


    def __truediv__(self, other: 'Vector | int | float') -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        elif isinstance(other, Vector):
            return Vector(self.x / other.x, self.y / other.y)
        else:
            raise TypeError('Multiplication is only allowed between vectors, or vector and scalar')

    def __rtruediv__(self, other: 'Vector | int | float') -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector(other / self.x , other / self.y)
        elif isinstance(other, Vector):
            return Vector(other.x / self.x, other.y / self.y)
        else:
            raise TypeError('Multiplication is only allowed between vectors, or vector and scalar')


    def __pow__(self, other):
        return Vector(self.x ** other, self.y ** other)

    
    def __eq__(self, other: 'Vector | int | float') -> bool:
        if not isinstance(other, Vector):
            return False
        
        return self.x == other.x and self.y == other.y

    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
    

    def sum(self):
        return self.x + self.y


    def magnitude(self) -> float:
        return np.sqrt(self.x**2 + self.y**2)
    
    def setMagnitude(self, mag):
        return self.normalize() * mag
    

    def limit(self, limit):
        mag = self.magnitude()
        if mag > limit:
            self.setMagnitude(limit)
        else:
            pass    
    
    
    def normalize(self) -> 'Vector':
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        
        return Vector(self.x / mag, self.y / mag)
    

    def angle_with(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Angle can only be calculated between vectors.')
        
        magnitudes = self.magnitude() * other.magnitude()

        if magnitudes == 0:
            raise ValueError("Cannot calculate angle with a zero vector")
        
        dot_product = self @ other

        return np.acos(dot_product / magnitudes)
    

    def cross_product(self, other: 'Vector') -> float:
        if not isinstance(other, Vector):
            raise TypeError('Cross product is only allowed between vectors')
        return self.x * other.y - self.y * other.x
    
    
    def distance_to(self, other: 'Vector') -> float:
        if not isinstance(other, Vector):
            raise TypeError('Cannot calculate Distance between Vector Object and None Vector Object')

        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


    @classmethod
    def randomVector(cls):
        angle = np.random.uniform(0, 2 * np.pi)
        random_vector = Vector(np.cos(angle), np.sin(angle)) 
        return random_vector
    

    @staticmethod
    def zero():
        return Vector(0, 0)

    @staticmethod
    def unit_x() -> 'Vector':
        return Vector(1, 0)

    @staticmethod
    def unit_y() -> 'Vector':
        return Vector(0, 1)
    
    @property
    def items(self) -> list:
        return [self.x, self.y]
    
    @classmethod
    def translate(cls, WIDTH, HEIGHT):
        cls._origin_x -= WIDTH // 2
        cls._origin_y -= HEIGHT // 2