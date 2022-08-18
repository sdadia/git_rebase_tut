from  main import  func_add2, func_add3_from_main

def func_add3(x, y, z):
    return func_add2(z, func_add2(x,y))


print(func_add3(1,2 ,3))

def test_func_add3_from_main():
    assert func_add3_from_main(1, 2, 3) == 6