

1. Control Statement (if-else)
Example of if-else:
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

2. break Statement
for i in range(5):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)


3. pass Statement
for i in range(5):
    if i == 3:
        pass  # Do nothing when i equals 3
    else:
        print(i)

4. Condition
number = 20
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

5. Data Structure: List
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(my_list[2])  # Accessing an element by index (Output: 3)

# Loop through the list
for item in my_list:
    print(item)

Modifying a list:
my_list.append(6)  # Adding an element to the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.remove(3)  # Removing an element from the list
print(my_list)  # Output: [1, 2, 4, 5, 6]








Here's a detailed explanation with examples for each of the mentioned data structures in Python:

1. List
An ordered, mutable collection that can store elements of different types.
# Creating a list
my_list = [1, 2, 3, 4, 5]
# Accessing elements
print(my_list[0])  # Output: 1
# Modifying elements
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3, 4, 5]
# Adding elements
my_list.append(6)
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]
# Removing elements
my_list.remove(3)
print(my_list)  # Output: [1, 10, 4, 5, 6]

2. Tuple
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
# Accessing elements
print(my_tuple[0])  # Output: 1
# Attempting to modify elements (will cause an error)
# my_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment
# Slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)

3. Dictionary
An unordered collection of key-value pairs.
# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# Accessing values
print(my_dict["name"])  # Output: Alice
# Modifying values
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
# Adding key-value pairs
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
# Removing key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

4. Set
An unordered collection of unique elements.
# Creating a set
my_set = {1, 2, 3, 4, 5}
# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
# Set operations
another_set = {4, 5, 6, 7}
print(my_set.union(another_set))  # Output: {1, 2, 4, 5, 6, 7}
print(my_set.intersection(another_set))  # Output: {4, 5, 6}


5. Queue (using deque from collections)
A First-In-First-Out (FIFO) data structure.

from collections import deque

# Creating a queue
queue = deque(["Alice", "Bob", "Charlie"])
# Adding elements
queue.append("David")
print(queue)  # Output: deque(['Alice', 'Bob', 'Charlie', 'David'])
# Removing elements
queue.popleft()  # Removes 'Alice'
print(queue)  # Output: deque(['Bob', 'Charlie', 'David'])

6. Stack (using lists or deque)
A Last-In-First-Out (LIFO) data structure.
# Using a list as a stack
stack = []
# Adding elements (push)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # Output: [10, 20, 30]
# Removing elements (pop)
stack.pop()  # Removes 30
print(stack)  # Output: [10, 20]
# Using deque as a stack
from collections import deque
stack = deque()
stack.append(100)
stack.append(200)
print(stack)  # Output: deque([100, 200])
stack.pop()  # Removes 200
print(stack)  # Output: deque([100])
