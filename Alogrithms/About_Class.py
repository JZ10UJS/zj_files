#!/usr/bin/python
# coding: utf-8


class Person(object):
    is_alive = True
    deadday = 'not die yet'
    
    def __init__(self, name, birthday, gender, bloodtype):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.bloodtype = bloodtype

    def dying(self, deadday):
        self.is_alive = False
        self.deadday = deadday


class Programer(Person):
    def __init__(self,name,program_years,gender,bloodtype,birthday):
        super(Programer, self).__init__(name, birthday, gender, bloodtype)
        self.program_years = program_years


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<%s, %s>' % (self.getX(), self.getY())
    
    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False
    
    def __repr__(self):
        return 'Coordinate(%d, %d)' % (self.getX(),self.getY())
        

if __name__ == '__main__':
    a = Coordinate(4, 5)
