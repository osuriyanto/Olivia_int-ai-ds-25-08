import streamlit as st
import random

st.set_page_config(page_title="Guess the Number")
st.title("Guess the Number")

# --- difficulty presets ---
DIFFICULTIES = {
    "Easy (1–50, 10 guesses)":   (50, 10),
    "Medium (1–100, 7 guesses)": (100, 7),
    "Hard (1–200, 5 guesses)":   (200, 5),
}

# --- initialize state ---
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Medium (1–100, 7 guesses)"
if "max_num" not in st.session_state or "max_guesses" not in st.session_state:
    st.session_state.max_num, st.session_state.max_guesses = DIFFICULTIES[st.session_state.difficulty]
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, st.session_state.max_num)
if "guesses_left" not in st.session_state:
    st.session_state.guesses_left = st.session_state.max_guesses

# --- difficulty selector ---
choice = st.radio("Choose difficulty", list(DIFFICULTIES.keys()), index=list(DIFFICULTIES.keys()).index(st.session_state.difficulty))
if st.button("Start / Apply difficulty"):
    st.session_state.difficulty = choice
    st.session_state.max_num, st.session_state.max_guesses = DIFFICULTIES[choice]
    st.session_state.secret_number = random.randint(1, st.session_state.max_num)
    st.session_state.guesses_left = st.session_state.max_guesses
    st.info(f"New game: guess 1–{st.session_state.max_num} with {st.session_state.max_guesses} guesses.")

# Show guess range and remaining guesses
st.caption(f"I'm thinking of a number between 1 and {st.session_state.max_num}…")
st.write(f"You have {st.session_state.guesses_left} guesses left.")

# Let user guess with a number input
user_guess = st.number_input("Take a guess:", min_value=1, max_value=st.session_state.max_num, step=1, key="guess")

# Button to submit guess
submit = st.button("Submit guess")
if submit and st.session_state.guesses_left > 0:
    st.session_state.guesses_left -= 1
    secret = st.session_state.secret_number
    if user_guess == secret:
        st.success(f"🎉 You got it in {st.session_state.max_guesses - st.session_state.guesses_left} tries!")
    elif user_guess < secret:
        st.warning("Too low!")
    else:
        st.warning("Too high!")

    if st.session_state.guesses_left == 0 and user_guess != secret:
        st.error(f"Game over! The number was {secret}.")

# Restart game
if st.button("New game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses_left = 7
    st.info("Let's play again…")

