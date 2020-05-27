import re

def 反馈信息(例外):
    类型 = 例外.__class__.__name__
    原信息 = str(例外)
    if 类型 == 'NameError':
        return re.sub(r"name '(.*)' is not defined", r"请先定义'\1'再使用", 原信息)
    elif 类型 == 'ZeroDivisionError':
        return "请勿除以零"
    elif 类型 == 'RecursionError':
        return "递归过深。请确认: 1、的确需要递归 2、递归的收敛正确"
    return 原信息