class A(object):
       def __init__(self):
              self.__private()
              self.public()
       def __private(self):
              print 'A.__private()'
       def public(self):
              print 'A.public()'
class B(A):
       def __private(self):
              print 'B.__private()'
       def publicc(self):
              print 'B.public()'

b = B()