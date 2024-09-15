# 定义一个装饰器（装饰器的本质是闭包）
# 把一个函数当做参数传递给闭包中的外部函数
def check(fn):
    def inner():
        print("请先登录...")
        fn()
    return inner
# 需要被装饰的函数
def comment():
    print("发表评论")

# 使用装饰器的函数（增加一个登录功能）
# fn=comment fn()=comment()
# comment=inner,comment函数发生了变化
comment=check(comment)
comment()