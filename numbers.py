def is_prime_number(n:int) -> bool:
    """
    Check if a number is a prime number

    Args:
        n (int): number

    Returns:
        bool: True if nuùber is prime, False else
    """
    # get divisors
    factors = divisors(n)
    # a prime number is a number that is divisible only by itself and 1 (so 2 numbers only)
    return len(factors) == 2

def get_prime_factors(n:int) -> list[int]:
    """
    Get prime factors of a number

    Args:
        n (int): number

    Returns:
        list[int]: List of prime factors
    """
    if n == 1: raise Exception("1 is not a compound number")
    prime_factors = []
    
    # get all divisors
    for factor in divisors(n):
        # if divisor is a prime number, add to factors
        if is_prime_number(factor): prime_factors.append(factor)
        # if factor is number, ignore
        elif factor == n: continue
        # else, add divisors of the divisor to prime factors with recursivity
        else: prime_factors.extend(get_prime_factors(factor))

    return prime_factors


def divisors(n:int, negative:bool=False, sort_list:bool=False) -> list[int]:
    """
    Get the divisors of a number

    Args:
        n (int): number
        negative (bool, optional): Include negative numbers . Defaults to False.
        sort_list (bool, optional): Sort the list in ascending order. Defaults to False.

    Returns:
        list[int]: List of divisors
    """
    # if number is 0, only 0 divides him
    if n == 0: return [0]
    # 1 divides all numbers
    divisors_list = [1]
    for potential_divisor in range(2, abs(n)): # so we start to 2
        if n % potential_divisor == 0: divisors_list.append(potential_divisor)
    divisors_list.append(n)
    
    # add negative numbers (the opposites of the positive divisors)
    if negative:
        for divisor in divisors_list.copy(): divisors_list.append(-divisor)
    
    # sort list (maybe for a beautiful result)
    if sort_list: divisors_list.sort()

    return divisors_list
