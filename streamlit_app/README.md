# PRNG Playground Streamlit App

Welcome to the **PRNG Playground**, an interactive Streamlit application designed to explore, visualize, and test pseudo-random number generators (PRNGs) through engaging and educational modules.

## 📦 Modules Overview

### 1. Generator Exploration

* **Purpose:** Explore outputs from three PRNGs: Tausworthe, L’Ecuyer, and Mersenne Twister.
* **How to Use:**

  * Select a generator.
  * Configure any parameters if applicable (e.g., seed, `r`, `q`, `l` for Tausworthe).
  * Generate data and visualize it in 2D (Unit Square) and 3D (Unit Cube).
  * View statistical test results for randomness quality.

### 2. Parameter Playground (Tausworthe)

* **Purpose:** Play with the parameters of the Tausworthe generator to observe how they impact randomness.
* **How to Use:**

  * Adjust the seed, `r`, `q`, and `l` sliders.
  * Visualizations and statistical test results update in real-time.
  * A histogram helps visualize distribution uniformity.

### 3. Guess the Generator Challenge

* **Purpose:** Fun, educational game to guess which generator produced a dataset based on visual and statistical clues.
* **How to Use:**

  * Examine the 2D and 3D plots.
  * Review Chi-squared, Von Neumann, and Runs test outcomes.
  * Use the **Super Hint** if needed.
  * Make your guess and reveal the answer.
  * Start a new challenge anytime.

### 4. Sidebar Resources

* Access research papers, kid-friendly articles, and educational videos to learn more about randomness and PRNGs.

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Launch the app:

```bash
streamlit run streamlit_app/app.py
```

---

## 🛠 Technologies Used

* Python
* Streamlit
* Matplotlib
* Plotly
* NumPy

---

## 📚 Additional Resources

Links to references and kid-friendly learning materials are provided directly in the app's sidebar.

---

Enjoy learning and experimenting with PRNGs!
