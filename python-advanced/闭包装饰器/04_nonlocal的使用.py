# 修改闭包内使用的外部变量使用nonlocal关键词
def func_out(num1):
    def func_inner(num2):
        # 重新定义一个新变量num1
        nonlocal num1
        num1=num2+10

    print(num1)
    func_inner(10)
    print(num1)
    return func_inner

# f=func_out(10)
# 调用闭包等价于调用内部函数     num2=10
# f(10)
func_out(10)