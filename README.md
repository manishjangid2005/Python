# =============================================================================
#                          Python Programming: From Basics to Advanced
#                         Including Data Structures and Algorithms (DSA)
# =============================================================================

# -----------------------------
# 🐍 Python Basics  
# -----------------------------

# 1. Variables and Data Types
# Definition: Variables are containers for storing data values. Python has dynamic typing, 
# allowing you to declare variables without explicitly specifying their type.

name = "Alice"  # String: A sequence of characters
age = 30        # Integer: A whole number
height = 5.5    # Float: A decimal number
is_student = False  # Boolean: Represents True or False values

print(f"Name: {name}, Age: {age}, Height: {height}, Is student: {is_student}")


# 2. Control Flow (Conditionals and Loops)
# Definition: Control flow refers to the order in which individual statements, 
# instructions, or function calls are executed.

# Conditional statement
if age >= 18:
    print("You're an adult.")  # Executes if the condition is true
else:
    print("You're a minor.")   # Executes if the condition is false

# For loop (Iterating through a range of numbers)
for i in range(5):
    print(f"Loop iteration {i}")


# 3. Functions
# Definition: A function is a block of code that only runs when it is called. 
# Functions can take parameters and can return results.

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"  # Return the greeting string

# Calling the function
greeting = greet("Alice")
print(greeting)


# 4. Lists, Tuples, and Dictionaries
# Definition: Python provides several built-in data structures:
# - Lists: Ordered and mutable collections
# - Tuples: Ordered and immutable collections
# - Dictionaries: Unordered collections of key-value pairs

# List
fruits = ['apple', 'banana', 'cherry']
print(f"First fruit: {fruits[0]}")  # Accessing the first element

# Dictionary
person = {"name": "Alice", "age": 30}
print(f"Person's name: {person['name']}")  # Accessing value by key


# -----------------------------
# ⚙️ Intermediate Python
# -----------------------------

# 1. Object-Oriented Programming (OOP)
# Definition: OOP is a programming paradigm based on "objects", which can contain data (attributes) and code (methods).

class Dog:
    """A class representing a dog."""
    
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed

    def bark(self):
        """Method for making the dog bark."""
        print(f"{self.name} is barking!")  # Accessing class attributes

# Creating an object (instance of the class)
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Calling the method


# 2. Exception Handling
# Definition: Exception handling in Python uses `try`, `except`, and `finally` keywords to manage errors during program execution.

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")  # Handling the specific error


# 3. Modules and Packages
# Definition: A module is a file containing Python definitions and statements. Packages are collections of modules.

import math  # Importing the built-in math module
print(f"Square root of 16: {math.sqrt(16)}")  # Using the math module


# -----------------------------
# 🔥 Advanced Python
# -----------------------------

# 1. Decorators
# Definition: A decorator is a function that modifies the behavior of another function.

def log(func):
    """A decorator to log function calls."""
    
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)  # Call the original function
    return wrapper

@log  # Applying the decorator
def say_hello():
    """A simple function to say hello."""
    print("Hello!")

say_hello()  # Calling the decorated function


# 2. Generators
# Definition: A generator is a function that returns an iterator, allowing you to iterate over a sequence of values one at a time.

def countdown(num):
    """A generator function for counting down from a number."""
    while num > 0:
        yield num  # Yield the value and resume from here the next time
        num -= 1

print("Countdown from 5:")
for count in countdown(5):  # Iterating through the generator
    print(count)


# 3. Context Managers
# Definition: A context manager allows for the safe acquisition and release of resources, 
# such as files or database connections, using the `with` statement.

try:
    with open('file.txt', 'r') as file:
        content = file.read()  # Automatically opens and closes the file safely
        print(f"File content: {content}")
except FileNotFoundError:
    print("file.txt not found, skipping file reading example.")


# 4. Asynchronous Programming
# Definition: Asynchronous programming enables concurrent execution of code, particularly useful for I/O-bound tasks.

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)  # Simulates a delay
    print("World")

asyncio.run(main())  # Running the asynchronous function


# -----------------------------
# 📚 Data Structures and Algorithms (DSA)
# -----------------------------

# 1. Arrays (Lists in Python)
# Definition: An array (or list) is a data structure containing a collection of elements, 
# typically of the same data type, arranged in sequential order.

arr = [1, 2, 3, 4, 5]
for element in arr:
    print(f"Array element: {element}")


# 2. Linked List
# Definition: A linked list is a linear data structure where elements (nodes) are linked using pointers. 
# Each node contains data and a reference (pointer) to the next node.

class Node:
    """A node in a linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    """Class to represent the linked list."""
    
    def __init__(self):
        self.head = None  # The first node in the linked list

    def insert(self, new_data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """Print the entire linked list."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

llist = LinkedList()
llist.insert(3)
llist.insert(2)
llist.insert(1)
print("Linked List:")
llist.print_list()


# 3. Stack
# Definition: A stack is a linear data structure that follows the Last In First Out (LIFO) principle. 
# Elements are added and removed from one end (the top).

stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

# Pop an element off the stack
print(f"Popped from stack: {stack.pop()}")


# 4. Queue
# Definition: A queue is a linear data structure that follows the First In First Out (FIFO) principle. 
# Elements are added at one end (the rear) and removed from the other end (the front).

from collections import deque  # Importing deque for implementing queue

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue an element
print(f"Dequeued from queue: {queue.popleft()}")


# 5. Binary Tree
# Definition: A binary tree is a tree data structure where each node has at most two children, 
# referred to as the left and right child.

class TreeNode:
    """A node in a binary tree."""
    
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.value = key

def inorder_traversal(root):
    """In-order traversal of the binary tree."""
    if root:
        inorder_traversal(root.left)  # Traverse left subtree
        print(root.value)  # Print root value
        inorder_traversal(root.right)  # Traverse right subtree

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order traversal of binary tree:")
inorder_traversal(root)


# 6. Bubble Sort
# Definition: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
# compares adjacent elements, and swaps them if they are in the wrong order.

def bubble_sort(arr):
    """Perform bubble sort on an array."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(f"Sorted array using Bubble Sort: {arr}")


# 7. Merge Sort
# Definition: Merge sort is a divide-and-conquer algorithm that splits the list into halves, recursively sorts each half,
# and then merges the sorted halves back together.

def merge_sort(arr):
    """Perform merge sort on an array."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(f"Sorted array using Merge Sort: {arr}")


# 8. Graph (BFS)
# Definition: A graph is a non-linear data structure consisting of nodes (vertices) connected by edges. 
# Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures level by level.

from collections import defaultdict

class Graph:
    """Class to represent a graph using adjacency list."""
    def __init__(self):
        self.graph = defaultdict(list)  # Dictionary to store graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        self.graph[u].append(v)

    def bfs(self, start):
        """Perform BFS starting from a given node."""
        visited = set()  # Set to track visited nodes
        queue = [start]  # Initialize the queue
        visited.add(start)

        while queue:
            node = queue.pop(0)  # Remove the front of the queue
            print(node, end=" ")  # Process the current node

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Enqueue the neighbor
                    visited.add(neighbor)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("\nBFS traversal starting from vertex 2:")
g.bfs(2)

# -----------------------------
# 📚 End of Program
# -----------------------------
