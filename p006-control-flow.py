# if statement
x = 5
if x < 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")

# while loop
x = 0
while x < 5:
    print(x)
    x += 1

# for loop
for x in range(5):
    print(x)

# continue statement
for x in range(5):
    if x == 2:
        continue
    print(x)

# break statement
x = 0
while True:
    print(x)
    x += 1
    if x == 5:
        break