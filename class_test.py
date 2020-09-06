import random

class Unit:
  def __init__(self, name):
      self.name = name
      rating= random.randint(1, 5)
      self.rating = rating
      

r= Unit('rachel')
s= Unit('Stanky')

print(r.name, r.rating) 
print(s.name, s.rating)

class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def gender(self):
        try:
            # If it has been defined for the instance, simply return the gender
            return self._gender
        except AttributeError:
            # If it's not defined yet, define it, and then return it
            self._gender = random.choice(['male', 'female'])
            return self._gender

r = Person('rachel')
s = Person('Stanky')
print(r.gender)
print(s.gender)