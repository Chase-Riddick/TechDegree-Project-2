
nums = range(5, 101)
halves = []
for num in nums:
    halves.append(num/2)

#print(halves)

halves1 = [num/2 for num in nums]
#print(halves1)
print([num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0])

