f = input()
s = input()

dp = [[['', '', '']]]

for i in range(max(len(f), len(s))):
    before = dp[i]
    next = []
    f_a, s_a = ('', '')
    if i < len(f):
        f_a = f[i]
    if i < len(s):
        s_a = s[i]
    
    for cs, fs, ss in before:
        if s_a not in fs and f_a not in ss:
            ncs, nfs, nss = cs[:], fs[:], ss[:]
            if f_a == s_a:
                ncs += f_a
                nfs = ''
                nss = ''
            else:
                nfs += f_a
                nss += s_a
            next.append([ncs, nfs, nss])

        if s_a in fs:
            ncs, nfs, nss = cs[:], fs[:] + f_a, ss[:]
            if len(s_a) != 0:
                start = fs.index(s_a)
                ncs += s_a
                nfs = nfs[start+1:]
                nss = ''
            next.append([ncs, nfs, nss])

        if f_a in ss:
            ncs, nfs, nss = cs[:], fs[:], ss[:] + s_a
            if len(f_a) != 0:
                start = ss.index(f_a)
                ncs += f_a
                nfs = ''
                nss = nss[start+1:]
            next.append([ncs, nfs, nss])
    
    next.sort(key = lambda x:-len(x[0]))
    dp.append(next)

for i in range(len(dp)):
    print(dp[i])
print(len(dp[-1][0][0]))