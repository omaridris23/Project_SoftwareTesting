import pickle, hashlib

a = []
a.append(a)

data = pickle.dumps(a)
print(hashlib.sha256(data).hexdigest())