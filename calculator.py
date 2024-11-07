def add(x, y):
    """add numbers"""
    return x + y

def subtract(x, y):
    """subtract numbers"""
    return x - y

def divide(x, y):
    """divide numbers"""
    return x / y

def multiply(x, y):
    """multiply numbers"""
    return x * y

def error(x, y):
    return 0

def count_by(x, n):
    count_list = []
    for i in range(1, n + 1):
        count_list.append(i * x)
    return count_list