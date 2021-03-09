from datetime import datetime

def get_time():
    timestamp = datetime.now()
    time_string = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return time_string

def decorator_function(time):
    def wrapper(function):
        def internal_wrapper(*args):            
            print(f"we are doing {function.__name__} on the values {args}")
            function(*args)
            print(time)
            print()
        return internal_wrapper
    return wrapper

@decorator_function(get_time())
def multiplication(*args):
    ans=1
    for arg in range(len(args)):
        ans *= args[arg]
    print(ans)

@decorator_function(get_time())
def addition(*args):
    ans = 0
    for arg in args:
        ans += arg
    print(ans)

multiplication(2,3,5)
addition(2,3,5)
        


