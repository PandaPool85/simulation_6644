
import numpy as np

def tausworthe(seed, r, q, l, size):
    """
    Tausworthe generator implementation.
    Parameters:
        seed (int): Initial binary seed (e.g., 32-bit integer)
        r (int): Bit position used in recurrence
        q (int): Another bit position
        l (int): Output bit length
        size (int): Number of uniform values to generate
    Returns:
        list of floats: PRNs in [0,1)
    """

    def get_bit(val, pos):
        return (val >> pos) & 1

    bits = []
    state = seed
    for _ in range(size * l):
        new_bit = get_bit(state, r) ^ get_bit(state, q)
        state = ((state << 1) | new_bit) & ((1 << (r + 1)) - 1)
        bits.append(new_bit)

    result = []
    for i in range(0, len(bits), l):
        chunk = bits[i:i + l]
        if len(chunk) < l:
            break
        value = sum([bit << (l - j - 1) for j, bit in enumerate(chunk)])
        result.append(value / (2 ** l))

    return result

def lecuyer_combined(size):
    """
    L'Ecuyer's combined linear congruential generator.
    Returns a list of size uniformly distributed numbers in [0, 1).
    """
    m1 = 2147483563
    a1 = 40014
    m2 = 2147483399
    a2 = 40692

    x1 = 12345
    x2 = 67890

    result = []
    for _ in range(size):
        x1 = (a1 * x1) % m1
        x2 = (a2 * x2) % m2
        z = (x1 - x2) % (m1 - 1)
        result.append(z / (m1 - 1))

    return result

def mersenne_twister(size):
    """
    Generates a sequence of pseudo-random numbers between 0 and 1
    using NumPy's Mersenne Twister implementation.

    Returns an array of random numbers of the specified size.
    """
    return np.random.random(size)