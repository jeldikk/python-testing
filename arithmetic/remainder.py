def rem(arg1,arg2):
    if isinstance(arg1,list) or isinstance(arg2,list):
        raise ValueError("operands cannot be a list to do this operation")
    
    return arg1%arg2