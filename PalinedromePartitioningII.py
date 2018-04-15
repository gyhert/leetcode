import math
s = "aab"
print(len(s)+2)
print(s[::-1])
dp = list(range(1,len(s)+2))
print(dp)
dp[-1] = 0
print(dp)

for i in range(1, len(s)):
    for j in range(i+1):
        if dp[j-1] == math.inf:
            continue
        print(s[j:i+1][::-1])
        print(s[j:i+1])