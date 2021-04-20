import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__+ ' in not JSON serializable')

def decode_who(w):
    return Who(w['name'], w['age'])

some_man = Who('John Doe', 42)
json_string = json.dumps(some_man, default=encode_who)
print(json.dumps(some_man, default=encode_who))
new_man = json.loads(json_string, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)

# JSONEncoder method, raise not needed

# overload json.JSONEncoder class default method
class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)

print(json.dumps(some_man, cls=MyEncoder))
json_string = json.dumps(some_man, default=encode_who)
new_man = json.loads(json_string, cls=MyDecoder)
print(type(new_man))
print(new_man.__dict__)



# from JSON to python
# strings
jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
comics = json.loads(jstr)
print(type(comics))
print(comics)
# numbers
jstr = '16021766189.98'
electron = json.loads(jstr)
print(type(electron))
print(electron)
# lists
jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)
print(type(my_list))
print(my_list)
# dictionaries
json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
my_dict = json.loads(json_str)
print(type(my_dict))
print(my_dict)
