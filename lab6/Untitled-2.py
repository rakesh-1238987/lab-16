n = int(input("Enter a number: "))
last = n % 10
first = n
while first >= 10:
    first //= 10
print("First digit:", first)
print("Last digit:", last)
