93600

a = "Yeah right, now just wait for some 93.6k mins, \n you are in for a treat : ) "

b = []
for i in a:
    b.append(ord(i))
    
#print(b)


for i in [89, 101, 97, 104, 32, 114, 105, 103, 104, 116, 44, 32, 110, 111, 119, 32, 106, 117, 115, 116, 32, 119, 97, 105, 116, 32, 102, 111, 114, 32, 115, 111, 109, 101, 32, 57, 51, 46, 54, 107, 32, 109, 105, 110, 115, 44, 32, 10, 32, 121, 111, 117, 32, 97, 114, 101, 32, 105, 110, 32, 102, 111, 114, 32, 97, 32, 116, 114, 101, 97, 116, 32, 58, 32, 41, 32]:
    print(chr(i), end = '')   
print()
rows = 5
for row in range(rows):
    for col in range(rows * 2 - 1):
        if (row == 0 and (col == 1 or col == 5)) or \
           (row == 1 and (col == 0 or col == 3 or col == 6)) or \
           (row == 2 and (col == 1 or col == 5)) or \
           (row == 3 and (col == 2 or col == 4)) or \
           (row == 4 and col == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()
