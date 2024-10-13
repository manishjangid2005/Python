# Write a python program to fill in a letter template given below with name and date

# a = input("Enter your name: ")
# b = input("Enter the current date: ")

# print(f"\nName: {a}")
# print(f"Date: {b}")

# OR

letter = ''' Dear <|Name|> 
    You are selected to receive a scholarship.
<|Date|>'''

print(letter.replace("<|Name|>", "Manish Jangid").replace("<|Date|>", "June 17, 2024"))
