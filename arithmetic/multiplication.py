def multiply(arg1,arg2):
    if isinstance(arg1,list) or isinstance(arg2,list):
        raise ValueError("Multiplication is not done if either one is a list")
    
    return arg1*arg2
    