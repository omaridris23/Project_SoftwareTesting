#test
import pickle, hashlib

class Person:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
    
    def describe_person(self):
        print(self.name, self.age, sep=": ")

person: Person = Person("Liam", 0)
person.describe_person()

# with open('data.pickle', 'wb') as file:
#     data = pickle.dump(person, file)

# with open('data.pickle', 'rb') as file:
#     data = file.read()

#h = hashlib.sha256(data).hexdigest()
#print(h)
# Return the pickled representation of the object as a bytes object.

# The optional protocol argument tells the pickler to use the given
# protocol; supported protocols are 0, 1, 2, 3, 4 and 5. The default
# protocol is 4. It was introduced in Python 3.4, and is incompatible
# with previous versions.
for protocol in range(6):
    data = pickle.dumps(person, protocol= protocol)
    h = hashlib.sha256(data).hexdigest()
    print(f"Protocol {protocol} : {h}")
