
#multiplication table
for i in range (1,13):
   s = ""
   if i == 1:
      s += "  x "
   for j in range (1,13):
      s += '{:3} '.format(i * j)
   print(s)


#returns two dementional list of numbers with 1's
def layered_mult(list):
   new_list = []
   nested = []
   for i in list:
      for j in range(i):
         nested.append(1)
      new_list.append(nested)
      nested = []
   return new_list



#random score generator 60-100
import random
import math
def randomScore():
   num = math.floor(random.random()*40+60)
   print int(num)
randomScore()


##runs 5000 times and generates and counts heads/tails
import random
def coinToss():
   tails = 0
   heads = 0
   num = 0
   for i in range (1, 5001):
      num = round(random.random())
      if num == 0:
         heads += 1
      else:
         tails += 1
   print heads, tails
coinToss()
      
     

#unpaking dictionaries
def dictionary(arr):
   output = ""
   for key,data in arr.iteritems():
      output += "My " + key + " is " + data 
      print output
      output = ""
dictionary({"Name": "Inkar", "Age": "19"})


#output keys and values of list of dictionarys
def names(list):
   for dict in list:
      print dict["first_name"] +" "+ dict["last_name"]
def names2(dict):
   for key, data in dict.items():
      print
      print key
      for i in range(len(data)):
         print i+1,(data[i])["first_name"] +" "+ (data[i])["last_name"], len((data[i])["first_name"])+len((data[i])["last_name"])
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
names2(users)


# takes dict returns list of tuples
def tupleList(dict):
   return dict.items()
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
print tupleList(my_dict)


#takes two lists and outputs dictionary
def make_dict(list1, list2):
   if len(list1)<len(list2):
      return dict(zip(list2,list1))
   return dict(zip(list1,list2))
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
print make_dict(name,favorite_animal)


#bike class with three functions
class Bike(object):
   def __init__(self, price, max_speed):
   	self.price = price
   	self.max_speed	= int(max_speed)
   	self.miles = 0
   def displayInfo(self):
   	print	"price",	self.price, "max speed", self.max_speed, "miles", self.miles
      
   def ride(self):
      self.miles += 10
      print "riding"
      return self
   def reverse(self):
      if  self.miles == 0:
         return self
      self.miles -= 5
      print "reversing"
      return self

bike1 = Bike(200, "25")
bike1.ride().ride().ride().reverse().displayInfo()


# car class
class Car():
   def __init__(self, price, speed, fuel, mileage):
      if price > 10000:
         self.tax = 0.15
      else:
         self.tax = 0.12
      self.price = price
      self.speed = speed
      self.fuel = fuel
      self.mileage = mileage
      self.display()
   def display(self):
      print "Price:", self.price
      print "Speed:", self.speed
      print "Fuel:", self.fuel
      print "Mileage:", self.mileage
      print "Tax:", self.tax
      print ""
   
car = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(2000, "5mph", "Not Full", "105mpg")
car3 = Car(20000, "25mph", "Full", "25mpg")
car4 = Car(2000, "45mph", "Empty", "25mpg")


#product class
class Product():
   def __init__(price, name, weight, brand):
      self.price = price
      self.name = name
      self.weight = weight
      self.brand = brand
      self.status = "for sale"
   def sell(self):
      self.status = "sold"
      return self
   def tax(self, tax):
      return self.price * (1 + ( tax/100 ))
   def returnItem(self, reason):
      if reason == "defective":
         self.price = 0
      elif reason == "like new":
         self.status = "for sale"
      elif reason == "opened":
         self.reasom = "used"
         self.price *= 0.8
      return self
      def display(self):
         print self.price, self.name, self.weight, self.brand, self.status


# Animal super class. Dog and Dragon child classes. Inheritance
class Animal(object):
   def __init__(self, name, health):
      self.name = name
      self.health = health
   def walk(self):
      self.health -= 1
      return self
   def run(self):
      self.health -= 5
      return self
   def display(self):
      print self.name
      print self.health
animal = Animal("Animal", 30)
animal.walk().walk().run().run().display()

class Dog(Animal):
   def __init__(self, name):
      super(Dog, self).__init__(name, 150)
   def pet(self):
      self.health += 5
      return self
dog = Dog("Dog")
dog.walk().walk().run().run().pet().display()

class Dragon(Animal):
   def __init__(self):
      super(Dragon, self)
      self.health = 170
      self.name = "Dragon"
   def fly(self):
      self.health += 10
      return self
   def display(self):
      super(Dragon, self).display()
      print "Im a dragon!"
dragon = Dragon()
dragon.walk().walk().run().run().fly().display()


#MyMath class with own methods. Multiple Arguments: asterisk or splat (*) with args paramenter.
class MyMath(object):
   def __init__(self, val = 0):
      self.result = val
   def add(self, *args):
      for i in args:
         self.result += i
      return self
   def subtract(self, *args):
      for i in args:
         self.result -= i
      return self
      
mm = MyMath(3)
mm.add(2).add(2,5).subtract(3,2)
print mm.result


# Call and Call center class
class Call():
   def __init__(self, id, name, number, time, reason):
      self.id = id
      self.name = name
      self.number = number
      self.time = time
      self.reason = reason
   def display(self):
      print id, name, time, reason
class CallCenter():
   def __init__(self, calls):
      self.calls = calls
      self.queue = len(calls)
   def add(self, call):
      self.calls.append(call)
      return self
   def remove(self, number = 0):
      if number == 0:
         self.calls.pop(0)
      else:
         for call in self.calls:
            if call.number == number:
               self.calls.remove(call)
      return self
   def info(self):
      for call in self.calls:
         print call.number, call.name, self.queue

   
call1 = Call(1, "call1", 111, "1am", "any")
call2 = Call(2, "call2", 222, "2am", "none")
call3 = Call(3, "call3", 333, "3am", "none")
center = CallCenter([call1, call2, call3])
center.remove()
#center.sort()
center.info()



## Hospital class and Patient class. Put patiens to hostital and assign beds
class Patient():
   def __init__(self, id, name, allergies):
      self.id = id
      self.name = name
      self.allergies = allergies
      self.bed = None
class Hospital():
   def __init__(self, name, capacity):
      self.patients = []
      self.name = name
      self.capacity = capacity
   def add(self, patient, bed):
      if self.capacity <= len(self.patients):
         print "Sorry hospital is full"
      else:
         patient.bed = bed
         self.patients.append(patient)
         print "Patient is admitted"
      return self
   def remove(self, patient):
      self.patients.remove(patient)
      print patient.name, "is gone"
      patient.bed = None
      print patient1.name, "bed number is", patient1.bed
      return self
   def display(self):
      for i in self.patients:
         print "id:", i.id, "; name:", i.name, "; allergies:", i.allergies, "; bed:", i.bed
hospital = Hospital("swedish", 2)
patient1 = Patient(1, "anna", "none")
patient2 = Patient(2, "bob", "none")
patient3 = Patient(3, "jack", "some")
patient4 = Patient(4, "smith", "lots")
hospital.add(patient1, 1)
hospital.add(patient2, 2)
hospital.add(patient3, 3)
hospital.remove(patient1)
hospital.add(patient4, 4)
hospital.display()

# sort array of Student objects by specific attribute
class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'B', 10),
]
bob = sorted(student_objects, key=lambda (x): x.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print bob
student_objects.sort(student_objects, key=lambda (x): x.age) 
print student_objects