def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    s=0
    if a%2==1 and b%2==1:
        s=True
    else:
        s=False
    return s
print(main(1,3))
