import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from prng.generators import tausworthe, lecuyer_combined, mersenne_twister
from prng.tests import chi_squared_test, von_neumann_test, runs_test
from prng.visualizations import plot_unit_square_and_cube_interactive, plot_unit_square_and_cube
import random
import plotly.express as px

st.title("🎲 PRNG Playground!")

st.markdown("Welcome to the PRNG Playground! Here you can explore how computers create 'random' numbers. Pick a mode and have fun learning!")

st.markdown("---")
with st.expander("🧒 What are Random Numbers? (For Kids!)"):
    st.markdown("""
    Random numbers are like surprises from a magic box! 🎁

    Computers use special recipes called **Random Number Generators (RNGs)** to create numbers that seem like surprises. But guess what? 
    Since computers follow instructions exactly, the numbers aren't truly random — they're called **pseudo-random** because they *pretend* to be random!

    In this playground, you can explore how these magic number machines work, see their patterns, and even test how good they are at being random! 🎲✨
    """)


mode = st.sidebar.selectbox(
    "Choose Your Adventure:",
    ("🔍 Generator Exploration", "🛠️ Parameter Playground (Tausworthe)", "🎯 Guess the Generator Challenge")
)

sample_size = st.sidebar.slider("How many numbers to generate?", min_value=100, max_value=5000, value=1000, step=100, help="Think of this like scooping up this many random marbles!")

if mode == "🔍 Generator Exploration":
    st.header("🔍 Explore Different Random Number Generators")
    generator = st.selectbox("Pick a Random Number Machine:", ("Tausworthe", "L’Ecuyer", "Mersenne Twister"))

    data = []
    label = generator

    if generator == "Tausworthe":
        seed = st.number_input("Seed", min_value=1, value=456, help="A starting point for the generator, like the first move in a board game.")
        r = st.slider("r (bit position)", min_value=1, max_value=31, value=29, help="r decides how far back we look in the number's bits to create the next number.")
        q = st.slider("q (bit position < r)", min_value=1, max_value=r-1, value=7, help="q is another look-back position, but it must be smaller than r!")
        l = st.slider("l (output bit length)", min_value=1, max_value=32, value=8, help="l decides how many bits we use to make each number. More bits = more variety!")

        if st.button("Generate Tausworthe Data"):
            data = tausworthe(seed, r, q, l, sample_size)

    elif generator == "L’Ecuyer":
        if st.button("Generate L’Ecuyer Data"):
            data = lecuyer_combined(sample_size)

    elif generator == "Mersenne Twister":
        if st.button("Generate Mersenne Twister Data"):
            data = mersenne_twister(sample_size)

    if data:
        st.subheader("👀 What Do the Numbers Look Like?")
        fig = plot_unit_square_and_cube(data, label)
        st.pyplot(fig)

        st.subheader("📊 Are These Numbers Truly Random?")
        chi2_stat, chi2_p = chi_squared_test(data)
        von_stat, von_p = von_neumann_test(data)
        runs_stat, runs_p = runs_test(data)

        def explain_pval(test_name, p_value):
            if p_value < 0.05:
                st.error(f"{test_name}: Hmm... This looks fishy! p-value = {p_value:.4f}")
            else:
                st.success(f"{test_name}: Looks good! p-value = {p_value:.4f}")

        explain_pval("Chi-squared Test", chi2_p)
        explain_pval("Von Neumann Test", von_p)
        explain_pval("Runs Test", runs_p)

elif mode == "🛠️ Parameter Playground (Tausworthe)":
    st.header("🛠️ Play with Tausworthe Settings!")

    seed = st.number_input("Seed", min_value=1, value=456, help="This is the first 'clue' the generator uses to start making numbers!")
    r = st.slider("r (bit position)", min_value=1, max_value=31, value=29, help="r picks how far back we peek into our bit history.")
    q = st.slider("q (bit position < r)", min_value=1, max_value=r-1, value=7, help="q is another peeking spot but closer than r.")
    l = st.slider("l (output bit length)", min_value=1, max_value=32, value=8, help="l chooses how many bits to glue together to make one number.")

    data = tausworthe(seed, r, q, l, sample_size)

    st.subheader("🔄 See Your Numbers in Action")
    fig2d, fig3d = plot_unit_square_and_cube_interactive(data, "Tausworthe")
    st.plotly_chart(fig2d)
    st.plotly_chart(fig3d)

    st.subheader("🧪 Did Your Settings Make Good Random Numbers?")
    chi2_stat, chi2_p = chi_squared_test(data)
    von_stat, von_p = von_neumann_test(data)
    runs_stat, runs_p = runs_test(data)

    def test_result_display(test_name, p_value):
        if p_value < 0.05:
            st.error(f"{test_name}: Uh oh! This test didn't pass. p = {p_value:.4f}")
        else:
            st.success(f"{test_name}: Yay! Passed with p = {p_value:.4f}")

    test_result_display("Chi-squared Test", chi2_p)
    test_result_display("Von Neumann Test", von_p)
    test_result_display("Runs Test", runs_p)

    st.subheader("🎨 How Many Times Did Each Number Show Up?")
    hist_fig = px.histogram(data, nbins=20, title='Histogram of Your Numbers')
    st.plotly_chart(hist_fig)

elif mode == "🎯 Guess the Generator Challenge":
    st.header("🎯 Guess the Generator Challenge")

    generators = {
        "Tausworthe": lambda: tausworthe(456, 29, 7, 8, sample_size),
        "L’Ecuyer": lambda: lecuyer_combined(sample_size),
        "Mersenne Twister": lambda: mersenne_twister(sample_size)
    }

    secret_gen = random.choice(list(generators.keys()))
    data = generators[secret_gen]()

    st.write("Look at these patterns and guess who made them!")
    fig2d, fig3d = plot_unit_square_and_cube_interactive(data, "Mystery Generator")
    st.plotly_chart(fig2d)
    st.plotly_chart(fig3d)

    st.subheader("🔎 Clues to Help You")

    chi2_stat, chi2_p = chi_squared_test(data)
    von_stat, von_p = von_neumann_test(data)
    runs_stat, runs_p = runs_test(data)

    st.write(f"🧩 Chi-squared Test: {chi2_p:.4f}")
    st.write(f"🧩 Von Neumann Test: {von_p:.4f}")
    st.write(f"🧩 Runs Test: {runs_p:.4f}")

    hist_fig = px.histogram(data, nbins=20, title='Guess Helper: Histogram of Numbers')
    st.plotly_chart(hist_fig)

    if 'challenge_secret_gen' not in st.session_state:
        st.session_state['challenge_secret_gen'] = random.choice(['Tausworthe', 'L’Ecuyer', 'Mersenne Twister'])


    if 'challenge_secret_gen' not in st.session_state:
        st.session_state['challenge_secret_gen'] = random.choice(['Tausworthe', 'L’Ecuyer', 'Mersenne Twister'])

    if 'answer_revealed' not in st.session_state:
        st.session_state['answer_revealed'] = False

    secret_gen = st.session_state['challenge_secret_gen']
    data = generators[secret_gen]()

    if st.checkbox("Need a Super Hint? 🕵️"):
        if secret_gen == "Tausworthe":
            st.info("Hint: This one needed a lot of tweaking to work well!")
        elif secret_gen == "L’Ecuyer":
            st.info("Hint: This one mixes numbers together to get better randomness!")
        else:
            st.info("Hint: This one is super popular and used in Python by default!")

    user_guess = st.radio("Who do you think made these numbers?", ['Tausworthe', 'L’Ecuyer', 'Mersenne Twister'])

    if st.button("Reveal the Magic Answer!"):
        st.session_state['answer_revealed'] = True

    if st.session_state['answer_revealed']:
        if user_guess == secret_gen:
            st.balloons()
            st.success(f"🎉 Woohoo! You're right! It was {secret_gen}.")
        else:
            st.error(f"Oops! It was actually {secret_gen}.")

        if st.button("🔄 Start a New Challenge"):
            st.session_state['challenge_secret_gen'] = random.choice(['Tausworthe', 'L’Ecuyer', 'Mersenne Twister'])
            st.session_state['answer_revealed'] = False
            st.rerun()


st.sidebar.markdown("---")
st.sidebar.header("📚 Learn More")

st.sidebar.markdown("**Research Papers:**")
st.sidebar.markdown("- [Mersenne Twister (Matsumoto & Nishimura, 1998)](https://dl.acm.org/doi/10.1145/272991.272995)")
st.sidebar.markdown("- [L’Ecuyer Combined Recursive Generators (1999)](https://www.jstor.org/stable/3009972)")
st.sidebar.markdown("- [Knuth's Art of Computer Programming (1997)](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)")

st.sidebar.markdown("**Kid-Friendly Resources:**")
st.sidebar.markdown("- [Khan Academy: What is Randomness?](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/randomness-1)")
st.sidebar.markdown("- [Math is Fun: Random Numbers](https://www.mathsisfun.com/data/random-numbers.html)")
st.sidebar.markdown("- [Computerphile: Pseudo Random Numbers](https://www.youtube.com/watch?v=E5n0gqJG1aY)")