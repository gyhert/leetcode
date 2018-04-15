t = int(input())
for i in range(1, t + 1):
    D, P = input().split(" ")
    l = len(P)
    Damage = 1
    Dummy_Damage = 0
    count = 0
    total_damage = 0
    C_number = 0
    res = 0
    s = {}
    hack = " "
    l_key = []
    for j in range(l):
        if P[j] == 'C':
            Damage *= 2
            Dummy_Damage *= 2
        else:
            count += 1
            Destroy = Damage
            total_damage += Destroy
            l_key.append(Damage)
            if Damage in s:
                s[Damage] += 1
            else:
                s[Damage] = 1
    k = max(l_key)
    while Dummy_Damage > 1:
        Dummy_Damage /= 2
        C_number += 1
    if total_damage < int(D):
        hack = str(0)
    if count > int(D):
        hack = 'impossible'
    while total_damage >= int(D):
        if k in s:
           h = s[k]
        else:
            break
        total_damage -= (k/2)
        h -= 1
        if h <= 0 and k > 1:
            k /= 2
        res += 1
        hack = str(res)
        s[k] = h
    print("Case #{}: {}".format(i, hack))