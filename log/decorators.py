

def log_method(f):
    """ Log method name"""
    def wrapper(*args, **kwargs):
        print(f"Begin : {f.__name__}")
        value = f(*args, **kwargs)
        print(f"End : {f.__name__}")
        return value

    return wrapper