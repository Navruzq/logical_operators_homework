from re import S


def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    s=0
    if a%2==1 and b%2==1:
        s=False
    else:
        s=True
    return s 
print(main(7,1))
