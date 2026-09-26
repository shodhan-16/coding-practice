n1 = int(input("Enter the number 1"))
n2 = int(input("Enter the number 2"))
n3 = int(input("Enter the number 3"))
if n1 > n2 and n1 > n3:
    print("N1 is the largest.")
elif n2 > n1 and n2 > n3:
    print("N2 is the largest.")
elif n3 > n1 and n3 > n2:
    print("N3 is the largest.")
else:
    print("Two or more numbers are equal and largest.")
