def add(n):
    if n==1:
        return ("1")
    else:
        return (n + int(add(n-1)))

a=int(input("Enter the value of n: "))
s=add(a)
print(s)