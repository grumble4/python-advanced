def check(fn):
    def inner():
        print("请先登录...")
        fn()
    return inner
# 需要被装饰的函数
# 解释器遇到@check 会立即执行comment=check(comment)
@check
def comment():
    print("发表评论")

comment()