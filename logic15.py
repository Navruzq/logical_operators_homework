def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10
    x2=a//10%10
    x3=a//100
    m=x1+x2+x3
    if m%2==1:
      s=True
    else:
      s=False
    return s
print(main(335))