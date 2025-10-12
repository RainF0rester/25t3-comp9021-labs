from collections import defaultdict
from math import sqrt

def prime_factors_of(n: int) -> None:
    """
    Prints the prime factorization of a given natural number n.

    If n < 2, the function simply returns (since 0 and 1 have no prime factors).
    Otherwise, it prints the prime decomposition of n in ascending order,
    showing exponents only when greater than 1.

    Example:
        >>> prime_factors_of(60)
        60 = 2^2 x 3 x 5

        >>> prime_factors_of(97)
        97 = 97

    Algorithm overview:
        1. Handle the trivial case (n < 2).
        2. Extract all factors of 2.
        3. Repeatedly test odd numbers (3, 5, 7, …) up to √rest
           to find other prime factors.
        4. If no smaller divisor is found, the remaining number is prime.
        5. Print the formatted decomposition.

    Args:
        n (int): The natural number to factorize (n >= 0)

    Returns:
        None — the result is printed directly.
    """

    if n < 2:
        return

    # A dictionary to store prime factors and their multiplicities
    factors = defaultdict(int)

    # rest keeps track of the remaining number to factorize
    rest = n

    # Step 1: extract all factors of 2 first (handle even numbers)
    while not rest % 2:
        rest //= 2
        factors[2] += 1

    # Step 2: start testing odd potential factors from 3 upwards
    potential_factor = 1  # start from 1 so the first increment gives 3

    # Continue until the remaining part (rest) becomes 1
    while rest > 1:
        try:
            # We only need to check up to sqrt(rest)
            upper_bound = round(sqrt(rest))
        except OverflowError:
            # In extremely large integers, math.sqrt() may overflow
            # → fallback: treat the entire rest as potentially prime
            upper_bound = rest

        # Try odd numbers (3, 5, 7, ...) up to √rest
        while (potential_factor := potential_factor + 2) <= upper_bound:
            # Check if current potential_factor divides rest
            if not rest % potential_factor:
                # Found a factor; extract all its multiplicities
                while not rest % potential_factor:
                    rest //= potential_factor
                    factors[potential_factor] += 1
                break
        else:
            # If loop completes normally (no break), rest itself is prime
            factors[rest] = 1
            rest = 1

    # Step 3: print the formatted result
    # Exponents (e > 1) are displayed as “p^e”, otherwise just “p”
    print(
        n,
        '=',
        ' x '.join(
            f'{factor}^{e}' if e > 1 else f'{factor}'
            for (factor, e) in factors.items()
        )
    )