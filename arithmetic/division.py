def divide(arg1,arg2):
    if isinstance(arg1,list) or isinstance(arg2,list):
        raise ValueError("Cannot divide if either of the operand is a list")

    return arg1/arg2

    