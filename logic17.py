from re import S


def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    a=75421
    x1=a%10
    x2=a%100//10
    x3=a%1000//100
    x4=a%10000//1000
    x5=a//10000
    if x1<x2 and x2<x3 and x3<x4 and x4<x5:
        s=True
    else:
        s=False
    return s 
print(main(75432))