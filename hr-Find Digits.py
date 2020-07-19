n=1012
def find_digits(n):
    count=0
    n=str(n)
    for i in range(len((n))):
        if int(n[i:i+1])!=0 and  int(n) % int(n[i:i+1]) ==0:
           count+=1
    print(count)
find_digits(n)

x=len([i for i in map(int, list(str(n))) if i != 0 and n % i == 0])
print(list(map(str, list(str(n)))))
print(x)
