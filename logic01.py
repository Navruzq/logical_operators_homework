def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    s=0
    if c>b and b>a:
        s="True"
    if a>b and b>c:
        s="True"
    else:
        s="False"
    return s
print(main(6,4,1))  