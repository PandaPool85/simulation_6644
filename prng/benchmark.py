from prng.generators import tausworthe, lecuyer_combined, mersenne_twister
import time

def benchmark_generators(sample_size=100000):
    """
    Benchmarks the runtime performance of Tausworthe, L’Ecuyer,
    and Mersenne Twister by measuring the time taken to generate a
    specified number of random values.
    """
    # Parameters for best Tausworthe
    seed, r, q, l = 456, 29, 7, 8

    timings = {}

    start = time.time()
    tausworthe(seed, r, q, l, sample_size)
    timings['Tausworthe'] = time.time() - start

    start = time.time()
    lecuyer_combined(sample_size)
    timings['L’Ecuyer'] = time.time() - start

    start = time.time()
    mersenne_twister(sample_size)
    timings['Mersenne Twister'] = time.time() - start

    return timings
