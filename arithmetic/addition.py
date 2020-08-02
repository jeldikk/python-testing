def add(arg1,arg2):
    if not isinstance(arg1,list) and not isinstance(arg2,list):
        return arg1+arg2
    else:
        raise ValueError("Argument values are of different type")