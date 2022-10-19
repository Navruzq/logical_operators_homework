from re import S


def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    
    x1=a/10000
    if x1>=1 and x1<10:
        s=True
    else:
        s=False
    return s
print(main(15234))