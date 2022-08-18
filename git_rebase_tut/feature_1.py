from  main import  func_add2

def func_add3(x, y, z):
    return func_add2(z, func_add2(x,y))


print(func_add3(1,2 ,3))