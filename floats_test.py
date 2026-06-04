import pickle, hashlib

a = 0.1 + 0.2
data = pickle.dumps(a)
print(hashlib.sha256(data).hexdigest())