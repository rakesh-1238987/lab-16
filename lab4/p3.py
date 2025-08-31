nums = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print("Frequencies:", freq)
