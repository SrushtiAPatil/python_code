a=input("Enter first value")
b=input("Enter second value")
c=input("Enter third value")

res=a if a>=b and a>c else b if b>=a and b>c else c if c>=a and c>b else "All are equal"
print("big of ({},{},{})={}".format(a,b,c,res))