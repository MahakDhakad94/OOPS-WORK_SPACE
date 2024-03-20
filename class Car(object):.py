class Car(object):
 def __init__(self, w, d):
 self.wheels = w
 self.doors = d
 self.color = ""
----------------------------------

(A)    def get_wheels():
 return wheels

(B)    def get_wheels():
 return self.wheels

(C)    def get_wheels(self):
 return wheels

(D)    def get_wheels(self):
 return self.wheels

 def get_wheels():
 def get_wheels():
 def get_wheels(self):
 def get_wheels(self):