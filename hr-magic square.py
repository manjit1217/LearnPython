all_n=[]
s = [[int(i) for i in input().split(' ')] for j in range(3)]
n = [s[i][j] for i in range(3) for j in range(3)]
allsum = []
for l in all_n:
    allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))
print(min(allsum))

