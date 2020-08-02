def divide(arg1,arg2):
    if not isinstance(arg1,list) and not isinstance(arg2,list):
        raise ValueError("Cannot divide if either of the operand is a list")

    return arg1/arg2

    