import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Protisruti",
    page_icon="🌱",
    layout="wide"
)


# Application title
st.title("🌱 Protisruti")

st.subheader("Learning, Skills, and Opportunities")


# Introduction
st.write(
    """
    Protisruti is an educational and empowerment platform designed to
    support women and children through personalized learning, skill
    development, educational guidance, and access to opportunities.
    """
)


# User type
st.header("Who are you?")

user_type = st.selectbox(
    "Please select your user type:",
    [
        "Student / Child",
        "Woman"
    ]
)


# Learning goal
st.header("What would you like to learn?")

learning_goal = st.selectbox(
    "Choose a learning goal:",
    [
        "Academic Learning",
        "English",
        "Digital Skills",
        "Programming",
        "Communication Skills",
        "Career Preparation",
        "Other"
    ]
)


# Continue button
if st.button("Start Learning"):

    st.success(
        f"Welcome to Protisruti! "
        f"You selected {user_type} and your goal is {learning_goal}."
    )

    st.info(
        "More personalized learning features will be added as the "
        "Protisruti project develops."
    )