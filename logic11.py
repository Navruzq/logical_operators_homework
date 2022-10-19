from re import S


def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a>=100 and a<1000:
        s=True
    else:
        s=False
    return s
print(main(123))