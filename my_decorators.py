def end_test(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Test passed")
        return result
    return wrapper