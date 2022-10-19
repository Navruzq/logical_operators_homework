from re import S


def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    s=0
    if a%2==0 and b%2==0:
        s=True
    else:
        s=False
    return s
print(main(2,4))