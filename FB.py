a = 1
b = 1
i = 1

d = int(input("Enter number..."))
while i < d:
    c = a + b
    a = b
    b = c
    print(c)
    i = i + 1
