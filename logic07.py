def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    s=0
    if a>=0 and b>=0:
        s=False
    else:
        s=True
    return s
print(main(3,8))
