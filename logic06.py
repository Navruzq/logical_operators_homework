def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    s=0
    if a<=0 and b<=0:
        s=False
    else:
        s=Ture
    return s
print(main(0,0))
1 "1"