from prng.generators import tausworthe
import numpy as np


def tune_tausworthe(tests, seeds, r_values, q_values, l_values, sample_size):
    """
    Tunes the Tausworthe generator by testing combinations of parameters.
    Returns the parameter set that yields the highest combined p-value
    across provided statistical tests.
    """
    best_score = None
    best_params = None
    best_test_results = None

    for seed in seeds:
        for r in r_values:
            for q in q_values:
                if q >= r:
                    continue  # q must be less than r
                for l in l_values:
                    data = tausworthe(seed, r, q, l, sample_size)

                    test_results = {test.__name__: test(data) for test in tests}
                    combined_p_value = np.prod([p for stat, p in test_results.values()])  # Product of p-values

                    if best_score is None or combined_p_value > best_score:
                        best_score = combined_p_value
                        best_params = (seed, r, q, l)
                        best_test_results = test_results

                    chi_p = test_results['chi_squared_test'][1] if 'chi_squared_test' in test_results else None
                    von_p = test_results['von_neumann_test'][1] if 'von_neumann_test' in test_results else None
                    runs_p = test_results['runs_test'][1] if 'runs_test' in test_results else None

                    print(f"Tested seed={seed}, r={r}, q={q}, l={l} => Combined p-value: {combined_p_value:.6f}, "
                          f"Chi2 p-value: {chi_p:.4f}, Von Neumann p-value: {von_p:.4f}, Runs p-value: {runs_p:.4f}")

    if best_test_results is None:
        best_test_results = {}

    return best_params, best_score, best_test_results

