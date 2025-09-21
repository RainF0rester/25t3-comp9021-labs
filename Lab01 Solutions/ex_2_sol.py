def f2_1(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    """
    if n == 0:
        return ""
    return (str(n) * n + "\n") * n


def f2_2(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    """
    if n == 0:
        return ""
    
    result = ""
    for _ in range(n):
        result += str(n) * n + "\n"
    return result


def f2_3(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    """
    if n == 0:
        return ""
    
    rows = [str(n) * n for _ in range(n)]
    return "\n".join(rows) + "\n"
