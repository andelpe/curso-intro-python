from time import perf_counter

def timer(func):
    """
    Print the runtime of the decorated function
    """
    
    def wrapper_timer(*args, **kwargs):
        
        t0 = perf_counter()
        value = func(*args, **kwargs)
        t1 = perf_counter()
        
        print(f"Finished {func.__name__!r} in {t1-t0:.4f} secs")
        
        return value
    
    return wrapper_timer