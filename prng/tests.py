from scipy.stats import chisquare, norm
import numpy as np


def chi_squared_test(data, bins=10):
    """
    Performs the Chi-squared goodness-of-fit test to assess whether
    the generated data is uniformly distributed across a specified number of bins.

    Returns the test statistic and p-value.
    """
    counts, _ = np.histogram(data, bins=bins)
    expected = [len(data)/bins] * bins
    return chisquare(counts, expected)

def von_neumann_test(data):
    """
    Performs Von Neumann test for randomness (based on successive differences).
    Returns test statistic and p-value.
    """
    diffs = np.diff(data)
    d_squared = np.sum((diffs - np.mean(diffs)) ** 2)
    n = len(diffs)
    expected = (n - 1) * np.var(diffs)
    z = (d_squared - expected) / np.sqrt(2 * (expected ** 2) / (n - 1))
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return z, p_value

def runs_test(data):
    """
    Runs test for randomness based on median.
    Returns test statistic and p-value.
    """
    median = np.median(data)
    signs = [1 if x > median else 0 for x in data]
    runs = 1 + sum([1 for i in range(1, len(signs)) if signs[i] != signs[i-1]])

    n1 = signs.count(1)
    n2 = signs.count(0)
    mean = ((2 * n1 * n2) / (n1 + n2)) + 1
    std = np.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) /
                  (((n1 + n2) ** 2) * (n1 + n2 - 1)))

    z = (runs - mean) / std
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return z, p_value