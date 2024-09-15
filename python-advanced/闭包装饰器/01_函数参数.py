def func01():
    print("func01 is show")

# func01()
#<function func01 at 0x000002DB1C5B3E20>
# 函数名存放的是函数所在空间的地址
# print(func01)

# 函数名也可以像普通的变量一样赋值
# func02=func01
# func01 is show
# func02()

# 0x11
# func=func01=0x11
def foo(func):
    func()
    # 0x11
foo(func01)