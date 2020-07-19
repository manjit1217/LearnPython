l1=[2,4]
l2=[3,7,8]
print('helo')
if any(x %2==0 for x in l2):
    print('Hi')

def between_sets(l1,l2):
    max_of_l1=max(l1)
    min_of_l2=min(l2)
    count=0
    for i in range(max_of_l1,min_of_l2+1,max_of_l1):
        if all(i % arr ==0 for arr in l1) and all(brr % i==0 for brr in l2 ):
            count=count+1
    print(count)

    #
    # for b in new_list:
    #     for a in l1:
    #         if (b %a )==0:
    #             new_list1.append(b)
    # for c in new_list:
    #     for d in l2:
    #         if d % c == 0:
    #             new_list2.append(c)
    #
    # print(count,new_list1,new_list2)



between_sets(l1,l2)




