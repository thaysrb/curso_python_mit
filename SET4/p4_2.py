# Thays Rodrigues 
# SET 4 - Problema 4_2

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle:
    def __init__(self, p_a, p_b, p_c):
        self.p_a = p_a
        self.p_b = p_b
        self.p_c = p_c

    def side_lengths(self):
        lado_a = self.p_a.euclidean_distance(self.p_b)
        lado_b = self.p_a.euclidean_distance(self.p_c)
        lado_c = self.p_b.euclidean_distance(self.p_c)
        
        return (lado_a, lado_b, lado_c) 

    def side_classification(self):
        
        if not math.isclose(self.side_lengths()[0], self.side_lengths()[1]) and not math.isclose(self.side_lengths()[0], self.side_lengths()[2]) and not math.isclose(self.side_lengths()[1], self.side_lengths()[2]):
            return 'scalene'
        elif math.isclose(self.side_lengths()[0], self.side_lengths()[1]) and math.isclose(self.side_lengths()[0], self.side_lengths()[2]) and math.isclose(self.side_lengths()[1], self.side_lengths()[2]):
            return 'equilateral'
        else:
            return 'isosceles'

    def area(self):
        return (self.perimeter() / 2 
        * ((self.perimeter() / 2) - self.side_lengths()[0]) 
        * ((self.perimeter() / 2) - self.side_lengths()[1]) 
        * ((self.perimeter() / 2) - self.side_lengths()[2])) ** 0.5

    def perimeter(self):
        return sum(self.side_lengths())

    def angles(self):
        angulo_ac = self.p_a.angle_between(self.p_c)
        angulo_cb = self.p_c.angle_between(self.p_b)
        angulo_ab = self.p_a.angle_between(self.p_b)

        return [abs(angulo_ab - angulo_cb), abs(angulo_ac - angulo_ab), (math.pi - (abs(angulo_ab - angulo_cb) + abs(angulo_ac - angulo_ab)))]

    def angle_classification(self):
        if self.is_right():
            return 'right'
        
        if math.isclose(self.angles()[1], math.pi/3) and math.isclose(self.angles()[2], math.pi/3) and math.isclose(self.angles()[0], math.pi/3) :
            return 'equiangular'
        elif self.angles()[0] < (math.pi/2) and self.angles()[1] < (math.pi/2) and self.angles()[2] < (math.pi/2):
            return 'acute'
        elif self.angles()[0] > (math.pi/2) or self.angles()[1] > (math.pi/2) or self.angles()[2] > (math.pi/2):
            return 'obtuse'

    def is_right(self):
        angulos = self.angles()
        for angulo in angulos:
            if angulo == math.pi/2:
                return True
        return False