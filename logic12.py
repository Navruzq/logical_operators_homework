from operator import truediv


def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10
    x2=a//10
    if x1==x2:
        s=True
    else:
        s=False
    return s
print(main(22))
    