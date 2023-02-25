'''
Swap out two variables without using a temp varibale.
'''

# a = int(input("Enter the first variable: "))
# b = int(input("Enter the second variable: "))

a, b = 4, 5
print(f"a: {a}, b: {b}")

b = a + b
a =  b - a
b = b - a

print(f"a: {a}, b: {b}")