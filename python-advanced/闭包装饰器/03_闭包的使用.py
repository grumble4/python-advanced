# 实现需求：
# 张三：到北京了吗？
# 李四：已经到了，放心吧。

def config_name(name):
    # 内部函数
    def say_info(info):
        print(name+":",info)

    return say_info
tom=config_name("tom")
tom("你好")
tom("你在吗")
jerry=config_name("jerry")
jerry("你好")
jerry("我在呢")