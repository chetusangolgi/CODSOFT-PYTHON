def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("enter the first no."))
b=int(input("enter the second no."))
print("enter your choice")
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
ch=input()

if ch=="a":
    print("result=",add(a, b))
elif ch=="b":
    print("result=",sub(a, b))
elif ch=="c":
    print("result=",mul(a, b))
elif ch=="d":
    print("result=",div(a, b))
else:
    print("invalid choice")