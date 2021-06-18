# Thays Rodrigues 
# SET 4 - Problema 4_2

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
    
    def to_float(self):
        return float(self.numerator/self.denominator)
    
    def reciprocal(self):
        return Rational(self.denominator,self.numerator)

    def reduce(self):
        
        valor_1 = self.numerator
        valor_2 = self.denominator
        # Operação máximo divisor comum 
        while valor_2:
            valor_1, valor_2 = valor_2, valor_1 % valor_2

        return Rational(self.numerator/valor_1, self.denominator/valor_1)
    
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational((self.numerator * other.denominator) + (other.numerator * self.denominator),
             self.denominator * other.denominator).reduce()
        
        elif isinstance(other, int):
            return Rational(self.numerator + (other.numerator * self.denominator), self.denominator).reduce()
        
        elif isinstance(other, float):
            return ((self.numerator/self.denominator) + other)
    
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        
        elif isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)
        
        elif isinstance(other, float):
            return ((self.numerator * other)/self.denominator) 
        
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        
        elif isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)
        
        elif isinstance(other, float):
            return ((self.numerator / self.denominator) / other)  
        
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational((self.numerator * other.denominator) - (other.numerator * self.denominator),
             self.denominator * other.denominator).reduce()
        
        elif isinstance(other, int):
            return Rational(self.numerator - (other * self.denominator), self.denominator).reduce()
        
        elif isinstance(other, float):
            return ((self.numerator/self.denominator) - other)
        
        else:
            return None
