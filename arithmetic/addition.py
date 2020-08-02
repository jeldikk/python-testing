def add(arg1,arg2):
    if isinstance(arg1,list) or isinstance(arg2,list):
        raise ValueError("cannot add if either one of operand is list")

    return arg1+arg2