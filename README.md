| Type   | Ordered 	| Mutable 	| Allows Duplicates 	| Example            |
| ------ | ------- 	| ------- 	| ----------------- 	| ------------------ |
| List   | ✅       | ✅       | ✅                 	| `[1, 2, 3]`        |
| Tuple  | ✅       | ❌       | ✅                 	| `(1, 2, 3)`        |
| Set    | ❌       | ✅       | ❌                 	| `{1, 2, 3}`        |
| Dict   | ✅       | ✅       | Keys ❌, Values ✅		| `{'a': 1, 'b': 2}` |
| String | ✅       | ❌       | ✅                 	| `"hello"`          |


Operations in List
Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "apple", 3.5, True]

Accessing Elements
print(fruits[-1])

Modifying element
fruits[1] = "mango"

adding element
fruits.append("grape") #add at the end
fruits.insert(1, "melon") # add at specific position
fruits.extend("peer", "pineapple") # adding multiple element

Removing elements
fruits.remove("orange")
fruits.pop()
fruits.pop(1)
del fruits[0]
fruits.clear()

Searching & Counting
print("apple" in fruits)
print(fruits.index("cherry"))
print(fruits.count("apple"))

Tuples in Python are immutable sequences, meaning once a tuple i created, its element cannot be changed. However, you can perform several operations on tuple to access, combine and manipulate them in certain ways.

Creating Tuples
t1 = (1, 2, 3)
t2 = ("apple", "banana")
t3 = ()
t4 = (5,) # single element tuple comma is require

Accessing Elements
print(t[0])
print(t[1:4])

tuple concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

tuple repetition
t = (1, 2)
print(t * 3)

Membership test
t = (1, 2, 3)
print(2 in t)
print(5 not in t)

Tuple Length
print(len(t));

Tuple Unpacking
t = (10, 20, 30)
a, b, c = t
print(a, b, c) # 10 20 30

Converting between Tuples & Lists
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)

Set
Creating set
s1 = {1, 2, 3} Note {} will not create empty set instead creates empty dict
s2 = set([3, 4, 5])
s3 = set()

Adding Elements
s = {1, 2}
s.add(3)
s.update([4, 5]) # Add multiple elements

Removing Elements
s.remove(3) #Removes 3, raises keyError if not found
s.discard(4) #Removes 4, does not raise error if not found
s.pop() # Remove and returns a random element
s.clear() # Removes all elements

Set Operations
Union: print(s1 | s2)
Intersection: print(s1 & s2)

Dictionary
| Method                 | Description               | Example                                      |
| ---------------------- | ------------------------- | -------------------------------------------- |
| `d.keys()`             | Returns all keys          | `dict_keys(['name', 'age'])`                 |
| `d.values()`           | Returns all values        | `dict_values(['Suraj', 25])`                 |
| `d.items()`            | Returns key-value pairs   | `dict_items([('name','Suraj'), ('age',25)])` |
| `d.copy()`             | Returns a shallow copy    |                                              |
| `d.update(other_dict)` | Merges another dictionary |                                              |
