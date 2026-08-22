import pickle
import hashlib
import unittest
import struct

def get_hash(obj, protocol=pickle.DEFAULT_PROTOCOL):
    sdata = pickle.dumps(obj, protocol=protocol)
    return hashlib.sha256(sdata).hexdigest()

class TestPickle(unittest.TestCase):

    def test_basic_types(self):
        #Req4
        data = [1, 2, "Omar", 4.5]
        hash1 = get_hash(data, protocol=4)
        hash2 = get_hash(data, protocol=4)
        self.assertEqual(hash1, hash2)

    def test_protocol(self):
        #Req1
        data = {"project": "Software Testing", "grade": "Pass"}
        hp3 = get_hash(data, protocol=3)
        hp4 = get_hash(data, protocol=4)

        self.assertNotEqual(hp3, hp4)

        obj3 = pickle.loads(pickle.dumps(data, protocol=3))
        obj4 = pickle.loads(pickle.dumps(data, protocol=4))
        self.assertEqual(obj3, obj4)

    def test_floatings(self):
        #Req2
        val1 = 0.1 + 0.2
        val2 = 0.3

        hash1 = get_hash(val1, protocol=4)
        hash2 = get_hash(val2, protocol=4)

        self.assertNotEqual(hash1, hash2)

        self.assertEqual(get_hash(0.3, protocol=4), get_hash(0.3, protocol=4))

        self.assertIn(struct.pack(">d", 0.3), pickle.dumps(0.3, protocol=4))

    def test_recursion(self):
        #Req3
        a = [1, 2, 3]
        a.append(a)

        hash1 = get_hash(a, protocol=4)
        hash2 = get_hash(a, protocol=4)
        self.assertEqual(hash1, hash2)

        b=[1,2,3]
        b.append(b)
        self.assertEqual(get_hash(a,protocol=4),get_hash(b,protocol=4))
        r= pickle.loads(pickle.dumps(a,protocol=4))
        self.assertIs(r[3],r)

    def test_set_dict(self):
        #Req5
        s1 = {1, 2, "a", "b", 3}
        s2 = {"a", "b", 3, 2, 1}
        self.assertEqual(s1,s2)
        self.assertEqual(get_hash(s1,protocol=4),get_hash(s2,protocol=4))

        d1 = {"a":1,"b":2}
        d2 = {"b":2,"a":1}
        self.assertEqual(d1,d2)
        self.assertNotEqual(get_hash(d1,protocol=4),get_hash(d2,protocol=4))

if __name__ == '__main__':
    unittest.main(verbosity=2)
