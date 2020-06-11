import time
# 装饰器原理
def timer(func):
    def deco():
        start = time.time()
        print(start,"装饰器封装的功能")
        func()
        stop = time.time()
        print(stop-start)
    return deco
def test():
    time.sleep(2)
    print("test is running!")
test1 = timer(test)

test1()


#  装饰器修饰有参数的函数
def timer(func):
    def deco(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        t = stop - start
        print(t)
        return t

    return deco

@timer
def test(e):
    time.sleep(e)
    print("test is running!")


test(1)


#  有参数的装饰器
def timer(parameter):

    def outer_wrapper(func):

        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task1 run time is :", stop - start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task2 run time is :", stop - start)

        return wrapper

    return outer_wrapper

@timer(parameter='task1')
def task1():
    time.sleep(2)
    print("in the task1")

@timer(parameter='task2')
def task2():
    time.sleep(2)
    print("in the task2")

task1()
task2()
