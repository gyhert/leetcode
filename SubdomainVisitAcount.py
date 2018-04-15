import collections
class Solution:
    def __init__(self):
        print("in init")
    def subdomainvisit(self, domains):
        cnt = collections.defaultdict(int)
        for domain in domains:
            c,d = domain.split()
            c = int(c)
            while True:
                try:
                    loc = d.index('.')
                except ValueError:
                    cnt[d] += c
                    break
                cnt[d] += c
                d = d[loc+1:]
        res = []
        for k, v in cnt.items():
            res.append(str(v) + " " + k)
        return res


