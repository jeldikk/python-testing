def multiply(arg1,arg2):
    if not isinstance(arg1,list) and not isinstance(arg2,list):
        raise ValueError("Multiplication is not done if either one is a list")
    
    return arg1*arg2
    