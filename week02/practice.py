# Declaring a variable.
message = "Hello, me"

print(message)

# Multiline string. change calculating insurance
message1 = """Bobby's world was a good
cartoon on the 1990s"""
print(message1)

# Length of a string
n = len(message)
print(n)

# Indexing into a string
print(message[0])

# Slicing
print(message[0:5])

# Methods
print(message.lower())
print(message.upper())
print(message.count("Hello"))
print (message.find("me"))
print(message.replace("me", "kosmos"))

greeting = "Hello"
name = "me"
message = greeting + ", " + name
print(message)

message = "{}, {}. Welcome!".format(greeting, name)
print(message)

message = f"{greeting}, {name} - Welcome!"
print(message)

print(f"{greeting}, {name.upper()} - welcome!")

print(dir(name))
# print(help(str))
# print(help(str.lower))

# Numerics
x = 3
print(type(x))

y = 3.14
print(type(y))

a = 3
b = 2
print(a + b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
print(a * b + 1)
print(a * (b + 1))

x += y
print(x)

print(abs(-3))
print(round(3.75, 1))

a = int("100")
b = int("200")
print(a + b)