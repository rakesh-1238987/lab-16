n = input("Enter a number: ")
swapped = n[-1] + n[1:-1] + n[0] if len(n) > 1 else n
print("Number after swapping:", swapped)
