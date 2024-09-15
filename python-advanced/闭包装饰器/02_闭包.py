# 闭包的构成条件
# 在函数嵌套的前提下
def func_out(num1):
    def func_inner(num2):
        # 内部函数使用了外部函数的变量
        num=num1+num2
        print("现在的值：",num)
        # 外部函数返回了内部函数
    return func_inner

# 创建闭包实例，4-8行不执行
# f=func_inner
# f()=func_inner()
f=func_out(10)
# 执行闭包
f(1)
f(2)