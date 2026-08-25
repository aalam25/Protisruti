import streamlit as st

from ai_assistant import ask_ai
from study_planner import create_study_plan


st.set_page_config(
    page_title="Protisruti",
    page_icon="🌱",
    layout="wide"
)


st.title("🌱 Protisruti")

st.subheader("Learning, Skills, and Opportunities")

st.write(
    """
    Protisruti is an educational and empowerment platform designed
    to support women and children through personalized learning,
    skill development, educational guidance, and access to
    opportunities.
    """
)


# AI Learning Companion
st.header("🤖 AI Learning Companion")

st.write(
    """
    Ask Protisruti a question about something you are learning.
    The AI Learning Companion will provide a simple explanation.
    """
)


question = st.text_area(
    "What would you like to learn?",
    placeholder="Example: Explain photosynthesis in simple words."
)


if st.button("Ask Protisruti"):

    if not question.strip():

        st.warning("Please enter a question first.")

    else:

        with st.spinner("Protisruti is thinking..."):

            try:

                answer = ask_ai(question)

                st.subheader("Protisruti's Answer")

                st.write(answer)

            except Exception as error:

                st.error(
                    "Something went wrong while connecting "
                    "to the AI service."
                )

                st.write(error)



# Study Planner
st.header("📚 Study Planner")

st.write(
    """
    Create a simple personalized study plan based on your
    learning goal, current level, available time, and target duration.
    """
)


learning_goal = st.text_input(
    "What do you want to learn?",
    placeholder="Example: Python"
)


skill_level = st.selectbox(
    "What is your current level?",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


study_time = st.selectbox(
    "How much time can you study each day?",
    [
        "30 minutes",
        "1 hour",
        "2 hours",
        "3+ hours"
    ]
)


duration = st.number_input(
    "How many weeks do you want to study?",
    min_value=1,
    max_value=52,
    value=4
)


if st.button("Create Study Plan"):

    if not learning_goal.strip():

        st.warning("Please enter something you want to learn.")

    else:

        plan = create_study_plan(
            learning_goal,
            skill_level,
            study_time,
            duration
        )

        st.subheader("Your Study Plan")

        st.write(plan)