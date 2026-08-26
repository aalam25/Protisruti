import streamlit as st

from ai_assistant import ask_ai
from study_planner import create_study_plan
from quiz_generator import get_quiz
from resources import get_resources
from user_profile import create_profile, get_profile_summary


st.set_page_config(
    page_title="Protisruti",
    page_icon="🌱",
    layout="wide"
)



# PROTISRUTI HOME

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


# AI LEARNING COMPANION

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
                    "Something went wrong while processing your question."
                )

                st.write(error)



# STUDY PLANNER

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



# QUIZ GENERATOR

st.header("📝 Quiz Generator")

st.write(
    """
    Test your knowledge with a practice quiz.
    Choose a subject, topic, difficulty level, and number of questions.
    """
)


quiz_subject = st.selectbox(
    "Choose a subject:",
    [
        "Python",
        "Mathematics",
        "English"
    ],
    key="quiz_subject"
)


if quiz_subject == "Python":

    quiz_topic = st.selectbox(
        "Choose a topic:",
        [
            "Functions"
        ],
        key="python_topic"
    )

elif quiz_subject == "Mathematics":

    quiz_topic = st.selectbox(
        "Choose a topic:",
        [
            "Basic Arithmetic"
        ],
        key="math_topic"
    )

else:

    quiz_topic = st.selectbox(
        "Choose a topic:",
        [
            "Grammar"
        ],
        key="english_topic"
    )


quiz_difficulty = st.selectbox(
    "Choose difficulty:",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    key="quiz_difficulty"
)


quiz_number = st.number_input(
    "Number of questions:",
    min_value=1,
    max_value=5,
    value=3,
    step=1,
    key="quiz_number"
)



# START QUIZ

if st.button("Start Quiz"):

    quiz = get_quiz(
        quiz_subject,
        quiz_topic,
        quiz_difficulty,
        quiz_number
    )

    if not quiz:

        st.error(
            "No questions are currently available "
            "for this subject and topic."
        )

    else:

        st.session_state.quiz = quiz

        st.session_state.quiz_answers = {}

        st.session_state.quiz_submitted = False

        # Remove old selections from previous quiz
        for key in list(st.session_state.keys()):

            if key.startswith("question_"):

                del st.session_state[key]

        st.rerun()



# DISPLAY QUIZ

if "quiz" in st.session_state:

    st.subheader("Your Quiz")

    for index, question in enumerate(
        st.session_state.quiz
    ):

        st.write(
            f"### Question {index + 1}"
        )

        st.write(question["question"])

        # Add an empty option at the beginning.
        # This prevents the first real answer from
        # being selected automatically.

        options = [
            "Select an answer"
        ] + question["options"]

        selected_answer = st.radio(
            "Choose your answer:",
            options,
            index=0,
            key=f"question_{index}"
        )

        if selected_answer != "Select an answer":

            st.session_state.quiz_answers[index] = (
                selected_answer
            )

        else:

            # Remove the answer if the user returns
            # to the default selection.

            if index in st.session_state.quiz_answers:

                del st.session_state.quiz_answers[index]


    
    # SUBMIT QUIZ

    if st.button("Submit Quiz"):

        unanswered = []

        for index in range(
            len(st.session_state.quiz)
        ):

            if index not in st.session_state.quiz_answers:

                unanswered.append(index + 1)


        if unanswered:

            question_numbers = ", ".join(
                map(str, unanswered)
            )

            st.warning(
                "Please answer all questions before "
                f"submitting. Unanswered question(s): "
                f"{question_numbers}"
            )

        else:

            score = 0

            for index, question in enumerate(
                st.session_state.quiz
            ):

                user_answer = (
                    st.session_state.quiz_answers[index]
                )

                if user_answer == question["answer"]:

                    score += 1


            total = len(
                st.session_state.quiz
            )

            percentage = (
                score / total
            ) * 100


            st.session_state.quiz_submitted = True


            
            # RESULT
        
            st.subheader("🎯 Quiz Result")

            st.write(
                f"You scored **{score} out of {total}**."
            )

            st.write(
                f"Your score is **{percentage:.0f}%**."
            )


            if percentage >= 80:

                st.success(
                    "Excellent work! Keep learning and practicing."
                )

            elif percentage >= 60:

                st.info(
                    "Good job! Review the questions you missed."
                )

            else:

                st.warning(
                    "Keep practicing. You can improve with more study."
                )


            
            # ANSWER EXPLANATIONS

            st.subheader("📖 Answer Explanations")


            for index, question in enumerate(
                st.session_state.quiz
            ):

                user_answer = (
                    st.session_state.quiz_answers[index]
                )


                if user_answer == question["answer"]:

                    st.success(
                        f"Question {index + 1}: Correct"
                    )

                else:

                    st.error(
                        f"Question {index + 1}: Incorrect"
                    )

                    st.write(
                        f"Correct answer: "
                        f"{question['answer']}"
                    )


                st.write(
                    question["explanation"]
                )


    
    # RETAKE QUIZ

    if st.session_state.get(
        "quiz_submitted",
        False
    ):

        if st.button("🔄 Take Another Quiz"):

            del st.session_state["quiz"]

            st.session_state.quiz_answers = {}

            st.session_state.quiz_submitted = False

            st.rerun()



# RESOURCE CENTER

st.header("🌸 Resource Center")

st.write(
    """
    Explore learning, skills, opportunities, and safety resources
    designed to support women and children.
    """
)


resource_category = st.selectbox(
    "Choose a resource category:",
    [
        "🌸 Women's Education",
        "📚 Children's Learning",
        "💼 Skills & Career",
        "🎓 Scholarships & Opportunities",
        "🛡️ Safety & Well-being"
    ]
)


if st.button("Explore Resources"):

    selected_resources = get_resources(
        resource_category
    )


    if not selected_resources:

        st.warning(
            "No resources are currently available "
            "for this category."
        )

    else:

        st.subheader(
            f"Resources: {resource_category}"
        )


        for resource in selected_resources:

            st.markdown(
                f"### {resource['title']}"
            )

            st.write(
                resource["description"]
            )

            st.caption(
                f"Resource type: {resource['type']}"
            )

            st.divider()



# USER PROFILE

st.header("👤 User Profile")

st.write(
    """
    Create a profile so Protisruti can better understand
    your learning needs and goals.
    """
)


profile_name = st.text_input(
    "Your name:",
    placeholder="Example: Ayesha"
)


profile_age_group = st.selectbox(
    "Age group:",
    [
        "Child",
        "Teenager",
        "Young Adult",
        "Adult"
    ]
)


profile_user_type = st.selectbox(
    "I am:",
    [
        "Girl",
        "Woman",
        "Parent/Guardian",
        "Teacher/Educator"
    ]
)


profile_education = st.selectbox(
    "Education level:",
    [
        "Elementary School",
        "Middle School",
        "High School",
        "College/University",
        "Other"
    ]
)


profile_interests = st.multiselect(
    "What are you interested in learning?",
    [
        "Computer Skills",
        "Programming",
        "Mathematics",
        "English",
        "Science",
        "Financial Literacy",
        "Career Skills",
        "Creative Skills"
    ]
)


profile_goal = st.text_input(
    "What is your main learning goal?",
    placeholder="Example: I want to learn Python."
)


if st.button("Create My Profile"):

    if not profile_name.strip():

        st.warning("Please enter your name.")

    elif not profile_interests:

        st.warning(
            "Please select at least one learning interest."
        )

    elif not profile_goal.strip():

        st.warning(
            "Please enter your learning goal."
        )

    else:

        profile = create_profile(
            profile_name,
            profile_age_group,
            profile_user_type,
            profile_education,
            profile_interests,
            profile_goal
        )

        st.session_state.profile = profile

        st.success(
            "Your Protisruti profile has been created!"
        )



# DISPLAY PROFILE

if "profile" in st.session_state:

    st.subheader("Your Profile")

    profile_summary = get_profile_summary(
        st.session_state.profile
    )

    st.markdown(profile_summary)