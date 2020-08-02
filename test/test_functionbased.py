# import sys
# import os
# # sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../arithmetic"))
# # print(sys.path)

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../arithmetic")))
# print(sys.path)
# from ..arithmetic.division import divide
# from arithmetic import addition
# from arithmetic import multiplication
# from arithmetic import remainder


from arithmetic import addition

def test_addition():
    assert addition.add(10,20) == 30, "Should be 30"

def test_division():
    assert division.divide(3,2) == 1, "should be 1.5"


def test_multiplication():
    assert multiplication.multiply(3,2) == 6, "Should be 6"


def test_remainder():
    assert remainder.rem(3,2) == 1, "Should be 1"


if __name__ == "__main__":
    import sys
    sys.path.append("../arithmetic")

    print(sys.path)
    test_addition()
    test_division()
    test_multiplication()
    test_remainder()
    print("Tests are successfully completed")