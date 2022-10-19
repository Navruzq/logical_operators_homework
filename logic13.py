def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10
    x2=a//10
    m=x1+x2
    if m%2==0:
        s=True
    else:
        s=False
    return s
print(main(35))