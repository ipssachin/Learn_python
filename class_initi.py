#Defining class
class Person:
    # def re(name,age):
    #     na = name
    #     ag = age
    #     return
#initializing class function which takes 3 arguments
#self is used with __ini__ to use arguments as variables
  def __init__(self, name, age, Gender):
    self.name = name
    self.age = age
    self.Gender = Gender
#defined another function
  def ds():
#assigned string to aa
      aa= "internal function of class person"
#return aa to ds function
      return aa
# assigned Person class to p1 variable and values passed to the class as an Arguments
p1 = Person("John", 36, 'M')
#assigned ds function in the class Person to p2
p2 = Person.ds()

#printed p2
print(p2)
#printed name,age and gender variables used in the Person class
print(p1.name)
print(p1.age)
print(p1.Gender)
