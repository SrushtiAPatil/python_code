import sys
print("enter number of values and press @ to stop")

lst=[]
while("  "):
    val=input()
    if(val=="@"):
        if(len(lst)==0):
            print("list is empty")
        else:
            print("content of list =" ,lst)
        sys.exit()
    else:
        lst.append(float(val))
        
