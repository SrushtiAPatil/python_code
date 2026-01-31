def cube(cubes):
    def calculation():
        n,sq=cubes()
        cubres=n**3
        return n,sq,cubres
    return calculation


def square(values):
    def operation():
        n=values()
        res=n**2
        return n,res
    return operation

@cube
@square
def val():
    return 5

x,y,z=val()
print("square of({}) is={}".format(x,y)) 
print("cube of({}) is={}".format(x,z)) 
