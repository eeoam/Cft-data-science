
nums = [1, 2, 3, 4, 5]

# for loop
for num in nums:
    print(num)

# break
for num in nums:
    if num == 3:
        print("Three")
        break
    print(num)

# continue
for num in nums:
    if num == 3:
        print("Three")
        continue
    print(num)

# nested for
for num in nums:
    for letter in "abc":
        print(num, letter)

# range
for i in range(0, 10):
    print(i)

# while
x = 0
while x < 10:
    print(x)
    x += 1

# infinite loop
x = 0
while True:
    if x == 10: 
        print(x)
        x += 1
    else:
         break

# pass
for i in range(0, 3):
    pass


# for loops with range()
# while loops and infinite loop handling
# break ,continue, pass

# incorporate everything from numbers and strings juptyer files



# 01-Numbers
# 1. What would happen if you add a float and an integer?
# 2. What would happen if you cast a float as an integer?
# 3. What would happen if you cast an integer as a float?
# 4. What would happen if you cast a string "Hello" as a float or an integer?