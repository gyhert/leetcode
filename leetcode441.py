class solution:
    def arrangeCoins(self,n):
        i =0
        num=0
        while (num<n):
            i+=1
            num+=i
            if(num==n):
                return i
            else:
                return i-1

n=10
print(arrangeCoins())