a=[2, 1, 2, 3, 3, 4, 2, 4, 1]
b=[1, 2, 5, 1, 2, 4, 2, 3, 2, 1]

a.remove(a[5])
print(a)
map=[]
b_dict={}
b_dict=dict(b)
print(b_dict)
for i in range(0,len(b)):
    for j in range(0,len(a)):

        if b[i]==a[j]:
            if(map.__contains__(j)):
                map.append('NA')
            else:
                map.append(j)
                a.remove(a[j])
            break

print(map)