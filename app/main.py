import streamlit as st

from ai_assistant import ask_ai


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