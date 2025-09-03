marks = {
    "math": 90,
    "science": 85,
    "english": 88,
}
d = {} # empty dictionary

"""
print(marks.items())  # this will print {    dict_items([('math', 90), ('science', 85), ('english', 88)])    }

print(marks.keys())  # this will print dict_keys(['math', 'science', 'english'])

print(marks.values())  # this will print dict_values([90, 85, 88])  

"""
"""
marks.update({"math": 92, "social science": 95})  # this will update the value of math to 92 and add a new key social science with value 95
print(marks)  # this will print {'math': 92, 'science': 85, 'english': 88, 'social science': 95}

"""

# print(marks.get("math"))  # this will print 90

# print(marks.get("cse")) # this will print None because cse is not a key in the dictionary
# print(marks["cse"])  # this will raise a KeyError because cse is not a key in the dictionary

print(len(marks))  # this will print 3 because there are 3 key-value pairs in the dictionary