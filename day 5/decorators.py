def star(func):#hello
    def wrapper():
        print("*"*10)
        func()#hello
        print("*"*10)
    return wrapper


def hash(func):#hello
    def wrapper():
        print("#"*10)
        func()#hello
        print("#"*10)
    return wrapper


# def hello():
#     print('hello')
@hash
@star
def world():
    print('world')

world()
# star(hello)()#return wrapper functin


""" 
    ##########
    **********
    world
    **********
    ########## 

 """
# homework