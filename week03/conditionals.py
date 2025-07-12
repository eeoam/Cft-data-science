if True:
    print("Condition was True")

if False:
    print("Condition was True")

dist = "Poisson"
if dist == "Poisson":
    print("Poisson distribution")
elif dist == "Binomial":
    print("Binomial distribution")
elif dist == "Normal":
    print("Normal distribution")
else:
    print("Distribution unknown")

# not
unknown = 1
if not (unknown > 0):
    print("Unknown unsuitable")
else:
    print("Unknown suitable")

# and
prior = "uniform"

if prior == "uniform" and unknown > 0:
    print("prior uniform with unknown > 0")
else:
    print("Conditions not met")

# or
if prior == "uniform" or prior == "exponential" or prior == "gamma":
    print("Suitable prior for poisson likelihood")
else:
    print("not suitable for poisson likelihood")

# Object identity
a = [1,2,3]
b = [1,2,3]


print(a == b) # True
print(a is b) # False
print(id(a) == id(b)) # False

c = a
print(a == c) # True
print(a is c) # True
print(id(a) == id(c)) # True