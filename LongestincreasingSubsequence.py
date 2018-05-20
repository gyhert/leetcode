nums = [10, 9, 2, 5, 3, 4, 7, 101, 18]
tails = [0] * len(nums)
print(tails)
size = 0
for x in nums:
    i,j = 0, size
    while i != j:
        m = int((i+j)/2)
        if tails[m] < x:
            i = m + 1
        else:
            j = m
    tails[i] = x
    size = max(i + 1, size)
print(size)