## Project Overview

This project investigates the quality and behavior of three pseudo-random number generators (PRNGs):

- **Tausworthe Generator** (a binary linear feedback shift register-based generator)
- **L’Ecuyer’s Combined Generator**
- **Mersenne Twister** (Python’s default PRNG)

The core focus is on verifying whether the outputs from these generators approximate independent, identically distributed (i.i.d.) samples from a Uniform(0,1) distribution. This is done through statistical tests and visual analyses.

---

## Objective

The objective is to:

- Implement the three PRNGs in Python  
- Run formal statistical tests (Chi-squared, von Neumann, runs test) to check uniformity and independence  
- Visualize the output in 2D (`U_i` vs `U_{i+1}`) and 3D (`U_i`, `U_{i+1}`, `U_{i+2}`) plots  
- Evaluate and compare the computational efficiency (random numbers generated per second)

## End Goal

At the conclusion of the project, we aim to:

- Provide insight into the statistical soundness of each generator  
- Determine which generator is most reliable for simulation tasks requiring high-quality randomness  
- Deliver visual and statistical evidence to support our conclusions
- 
---

## Resources for Further Reading

1. L’Ecuyer, P. (1999). “Good Parameters and Implementations for Combined Multiple Recursive Random Number Generators.” *Operations Research*, 47(1), 159–164.  
2. Matsumoto, M., & Nishimura, T. (1998). “Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator.” *ACM Transactions on Modeling and Computer Simulation*, 8(1), 3–30.  
3. Gentle, J. E. (2003). *Random Number Generation and Monte Carlo Methods* (2nd ed.). Springer.  
4. Knuth, D. E. (1997). *The Art of Computer Programming, Vol. 2: Seminumerical Algorithms* (3rd ed.). Addison-Wesley.  
5. L’Ecuyer, P., & Simard, R. (2007). “TestU01: A C library for empirical testing of random number generators.” *ACM Transactions on Mathematical Software (TOMS)*, 33(4), 22.  

These resources are helpful for anyone who wants a deeper understanding of the design, implementation, and evaluation of random number generators.

---

## 📓 Notebook Analysis

The accompanying Jupyter notebook provides a comprehensive analysis of the three PRNGs:

* Generates data for each generator
* Performs formal statistical tests:

  * Chi-squared test
  * Von Neumann test
  * Runs test
* Visualizes generator outputs via:

  * 2D scatter plots (unit square)
  * 3D scatter plots (unit cube)
* Benchmarks the computational efficiency of each generator.

These analyses support understanding the statistical behavior and performance of each PRNG.

---

## 🎈 PRNG Playground - Streamlit App

We built an interactive **Streamlit app** for exploring and experimenting with PRNGs in a fun, educational format.

### 🧩 App Features:

* **Generator Exploration:** Visualize outputs and statistical test results.
* **Parameter Playground:** Tweak Tausworthe parameters and see real-time effects.
* **Guess the Generator Challenge:** Visual + statistical clues to guess which generator produced the data.
* **Kid-Friendly Mode:** Includes explanations, hints, and resources suitable for young learners.

---

## 🚀 Running the App

### 🛠️ Prerequisites

To run the notebook analysis and Streamlit app, you need:

* **Python 3.8+**

  * [Download Python](https://www.python.org/downloads/)
  * Verify installation:

    ```bash
    python --version
    ```

* **pip (Python package installer)**

  * Comes bundled with most Python installations.

### ✅ Optional: Virtual Environment

For isolated development, it's recommended to use a **virtual environment**:

```bash
python -m venv prng-env
source prng-env/bin/activate  # On Windows: .\\prng-env\\Scripts\\activate
```

### 1. **Install Dependencies**

Ensure you have Python 3.8+ and then install the required libraries:

```bash
pip install -r requirements.txt
```

### 2. **Run the Streamlit App**

```bash
streamlit run streamlit_app/app.py
```


