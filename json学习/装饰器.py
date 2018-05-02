import logging

'''
def use_logging(func):
    logging.warning('%s is running' % func.__name__)
    func()


def foo():
    print('i am foo')

use_logging(foo)
'''

'''
# 简单装饰器
def use_logging(func):
    def wrapper():
        logging.warning('%s is running' % func.__name__)
        return func()  # 把foo当作参数传递进来时，执行func()相当于执行foo()

    return wrapper


def foo():
    print('i am foo')


foo = use_logging(foo)  # 因为装饰器use_logging(foo)返回的是函数对象wrapper，这条语句相当于foo = wrapper
foo()  # 执行foo()就相当于执行wrapper()
'''

'''
# 语法糖
def use_logging(func):
    def wrapper():
        logging.warning('%s is running' % func.__name__)
        return func()

    return wrapper


@use_logging
def foo():
    print('i am foo')


foo()
'''


# 业务逻辑函数foo需要参数：
def use_logging(func):
    def wrapper(name):
        logging.warning('%s is running' % func.__name__)
        return func(name)

    return wrapper


@use_logging
def foo(name):
    print('i am %s' % name)

foo('buyu')