def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return str(x)
    else:
        return digital_root(x)
def validate(n):
    n=str(n)
    a=[]
    for i in range(0,len(n)):
        a.append(n[i])
    if len(a)%2==0:
        for i in range(0,len(a)):
            if i%2 == 0:
                a[i] = str(int(a[i])*2)
            if len(str(a[i]))>1:
                a[i]=digital_root(a[i])
            
    else:
        for i in range(0,len(n)):
            if i%2 != 0:
                a[i] = str(int(a[i])*2)
            if len(str(a[i]))>1:
                a[i]=digital_root(a[i])
    x=sum(int(i) for i in a)
    if x%10 == 0:
        return 1
    else:
        return 0
print (validate(2121))
    
