import pickle, hashlib

class Person:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age

person: Person = Person("Liam", {0,1,2,3,4})

data = pickle.dumps(person, protocol=4)

h = hashlib.sha256(data).hexdigest()

run_id = 4

with open("hash_log.txt", "a") as f:
    f.write(f"determinism test run {run_id}: {h}\n")

print(f"run {run_id}:", h)