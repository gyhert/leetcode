def findKthNumber(n, k):
    cur = 1
    k = k -1
    while(k > 0):
        step = 0
        first = cur
        last = cur + 1
        while(first <= n ):
            step += min(n + 1, last * 10) - first
            first *= 10
            last *= 10
        if (step <= k):
            cur += 1
            k -= step
        else:
            cur *= 10
            k -= 1
    return cur

print(findKthNumber(13, 4))
