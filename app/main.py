import streamlit as st
import pandas as pd

import sys
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_FOLDER = PROJECT_ROOT / "database"

sys.path.insert(
    0,
    str(DATABASE_FOLDER)
)


# ============================================================
# IMPORTS
# ============================================================

from database import (
    initialize_database,
    add_user,
    save_quiz_result,
    get_user_quiz_results,
    get_user_by_name
)

from ai_assistant import ask_ai

from study_planner import create_study_plan

from quiz_generator import get_quiz

from resources import get_resources

from user_profile import (
    create_profile,
    get_profile_summary
)

from recommendations import generate_recommendations


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Protisruti",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# INITIALIZE DATABASE
# ============================================================

initialize_database()


# ============================================================
# PROTISRUTI HOME
# ============================================================

st.title("🌱 Protisruti")

st.subheader(
    "Learning, Skills, and Opportunities"
)

st.write(
    """
    Protisruti is an educational and empowerment platform designed
    to support women and children through personalized learning,
    skill development, educational guidance, and access to
    opportunities.
    """
)


# ============================================================
# AI LEARNING COMPANION
# ============================================================

st.header("🤖 AI Learning Companion")

st.write(
    """
    Ask Protisruti a question about something you are learning.
    The AI Learning Companion will provide a simple explanation.
    """
)


question = st.text_area(
    "What would you like to learn?",
    placeholder="Example: Explain photosynthesis in simple words.",
    key="ai_question"
)


if st.button("Ask Protisruti"):

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        with st.spinner(
            "Protisruti is thinking..."
        ):

            try:

                answer = ask_ai(question)

                st.subheader(
                    "Protisruti's Answer"
                )

                st.write(answer)

            except Exception as error:

                st.error(
                    "Something went wrong while processing your question."
                )

                st.write(error)


# ============================================================
# STUDY PLANNER
# ============================================================

st.header("📚 Study Planner")

st.write(
    """
    Create a personalized study plan based on what you want
    to learn right now. Your profile can help Protisruti
    understand your broader goals, but you can choose a
    different subject whenever you want.
    """
)


# ============================================================
# PROFILE INFORMATION FOR STUDY PLANNER
# ============================================================

if "profile" in st.session_state:

    profile = st.session_state["profile"]

    st.success(
        f"Welcome back, {profile['name']}!"
    )

    st.write(
        f"**Your broader goal:** "
        f"{profile['learning_goal']}"
    )

    st.caption(
        "You can choose any subject you want to study below."
    )

else:

    st.info(
        """
        You have not created a profile yet.

        You can still create a study plan by choosing
        something you want to learn below.
        """
    )


# ============================================================
# CURRENT LEARNING GOAL
# ============================================================

learning_goal = st.text_input(
    "What do you want to learn right now?",
    placeholder="Example: Python",
    key="learning_goal"
)


# ============================================================
# SKILL LEVEL
# ============================================================

skill_level = st.selectbox(
    "What is your current level?",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    key="skill_level"
)


# ============================================================
# STUDY TIME
# ============================================================

study_time = st.selectbox(
    "How much time can you study each day?",
    [
        "30 minutes",
        "1 hour",
        "2 hours",
        "3+ hours"
    ],
    key="study_time"
)


# ============================================================
# STUDY DURATION
# ============================================================

duration = st.number_input(
    "How many weeks do you want to study?",
    min_value=1,
    max_value=52,
    value=4,
    step=1,
    key="study_duration"
)


# ============================================================
# CREATE STUDY PLAN
# ============================================================

if st.button("Create Study Plan"):

    if not learning_goal.strip():

        st.warning(
            "Please enter what you want to learn."
        )

    else:

        plan = create_study_plan(
            learning_goal,
            skill_level,
            study_time,
            duration,
            profile=st.session_state.get("profile")
        )

        st.subheader(
            "Your Personalized Study Plan"
        )

        st.write(plan)


# ============================================================
# QUIZ GENERATOR
# ============================================================

st.header("📝 Quiz Generator")

st.write(
    """
    Test your knowledge with a practice quiz.
    Choose a subject, topic, difficulty level, and number
    of questions.
    """
)


# ============================================================
# QUIZ SETTINGS
# ============================================================

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


# ============================================================
# QUIZ DIFFICULTY
# ============================================================

quiz_difficulty = st.selectbox(
    "Choose difficulty:",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    key="quiz_difficulty"
)


# ============================================================
# NUMBER OF QUESTIONS
# ============================================================

quiz_number = st.number_input(
    "Number of questions:",
    min_value=1,
    max_value=5,
    value=3,
    step=1,
    key="quiz_number"
)


# ============================================================
# START QUIZ
# ============================================================

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

        st.session_state["quiz"] = quiz

        st.session_state["quiz_answers"] = {}

        st.session_state["quiz_submitted"] = False


        # Remove old question selections

        for key in list(
            st.session_state.keys()
        ):

            if key.startswith("question_"):

                del st.session_state[key]


        st.rerun()


# ============================================================
# DISPLAY QUIZ
# ============================================================

if "quiz" in st.session_state:

    st.subheader("Your Quiz")


    for index, question in enumerate(
        st.session_state["quiz"]
    ):

        st.write(
            f"### Question {index + 1}"
        )

        st.write(
            question["question"]
        )


        # Empty option prevents automatic selection

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

            st.session_state["quiz_answers"][index] = (
                selected_answer
            )

        else:

            if index in st.session_state["quiz_answers"]:

                del st.session_state["quiz_answers"][index]


    # ========================================================
    # SUBMIT QUIZ
    # ========================================================

    if st.button("Submit Quiz"):

        unanswered = []


        for index in range(
            len(st.session_state["quiz"])
        ):

            if index not in st.session_state["quiz_answers"]:

                unanswered.append(
                    index + 1
                )


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

            # ------------------------------------------------
            # CALCULATE SCORE
            # ------------------------------------------------

            score = 0


            for index, question in enumerate(
                st.session_state["quiz"]
            ):

                user_answer = (
                    st.session_state["quiz_answers"][index]
                )


                if user_answer == question["answer"]:

                    score += 1


            total = len(
                st.session_state["quiz"]
            )


            percentage = (
                score / total
            ) * 100


            # ------------------------------------------------
            # SAVE RESULT TO DATABASE
            # ------------------------------------------------

            if "user_id" in st.session_state:

                save_quiz_result(
                    user_id=st.session_state["user_id"],
                    subject=quiz_subject,
                    topic=quiz_topic,
                    score=score,
                    total_questions=total
                )

                st.success(
                    "✅ Your quiz result has been saved!"
                )

            else:

                st.warning(
                    """
                    Your quiz was completed, but your result
                    could not be saved because you have not
                    created a user profile.
                    """
                )


            st.session_state["quiz_submitted"] = True


            # ------------------------------------------------
            # RESULT
            # ------------------------------------------------

            st.subheader(
                "🎯 Quiz Result"
            )


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


            # ------------------------------------------------
            # ANSWER EXPLANATIONS
            # ------------------------------------------------

            st.subheader(
                "📖 Answer Explanations"
            )


            for index, question in enumerate(
                st.session_state["quiz"]
            ):

                user_answer = (
                    st.session_state["quiz_answers"][index]
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


    # ========================================================
    # RETAKE QUIZ
    # ========================================================

    if st.session_state.get(
        "quiz_submitted",
        False
    ):

        if st.button(
            "🔄 Take Another Quiz"
        ):

            del st.session_state["quiz"]

            st.session_state["quiz_answers"] = {}

            st.session_state["quiz_submitted"] = False

            st.rerun()


# ============================================================
# RESOURCE CENTER
# ============================================================

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
    ],
    key="resource_category"
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


# ============================================================
# USER PROFILE
# ============================================================

st.header("👤 User Profile")


# ============================================================
# LOAD EXISTING PROFILE
# ============================================================

st.subheader(
    "Already have a profile?"
)


existing_name = st.text_input(
    "Enter your name to load your profile:",
    placeholder="Example: Ayesha",
    key="existing_profile_name"
)


if st.button("Load My Profile"):

    if not existing_name.strip():

        st.warning(
            "Please enter your name."
        )

    else:

        existing_user = get_user_by_name(
            existing_name.strip()
        )


        if existing_user:

            # ------------------------------------------------
            # SAVE USER ID
            # ------------------------------------------------

            st.session_state["user_id"] = int(
                existing_user[0]
            )


            # ------------------------------------------------
            # CONVERT INTERESTS TO LIST
            # ------------------------------------------------

            if existing_user[5]:

                interests = [
                    interest.strip()
                    for interest in existing_user[5].split(",")
                    if interest.strip()
                ]

            else:

                interests = []


            # ------------------------------------------------
            # CREATE PROFILE OBJECT
            # ------------------------------------------------

            st.session_state["profile"] = {

                "name": existing_user[1],

                "age_group": existing_user[2],

                "user_type": existing_user[3],

                "education_level": existing_user[4],

                "interests": interests,

                "learning_goal": existing_user[6]

            }


            # ------------------------------------------------
            # SUCCESS MESSAGE
            # ------------------------------------------------

            st.success(
                f"Welcome back, {existing_user[1]}!"
            )

            st.info(
                f"Your profile ID is {existing_user[0]}."
            )


        else:

            st.warning(
                "No profile was found with that name. "
                "Please create a new profile below."
            )


# ============================================================
# CREATE NEW PROFILE
# ============================================================

st.subheader(
    "Create a New Profile"
)


profile_name = st.text_input(
    "Your name:",
    placeholder="Example: Ayesha",
    key="profile_name"
)


profile_age_group = st.selectbox(
    "Age group:",
    [
        "Child",
        "Teenager",
        "Young Adult",
        "Adult"
    ],
    key="profile_age_group"
)


profile_user_type = st.selectbox(
    "I am:",
    [
        "Girl",
        "Woman",
        "Parent/Guardian",
        "Teacher/Educator"
    ],
    key="profile_user_type"
)


profile_education = st.selectbox(
    "Education level:",
    [
        "Elementary School",
        "Middle School",
        "High School",
        "College/University",
        "Other"
    ],
    key="profile_education"
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
    ],
    key="profile_interests"
)


profile_goal = st.text_input(
    "What is your main learning goal?",
    placeholder="Example: I want to learn Python.",
    key="profile_goal"
)


# ============================================================
# CREATE PROFILE BUTTON
# ============================================================

if st.button("Create My Profile"):

    if not profile_name.strip():

        st.warning(
            "Please enter your name."
        )

    elif not profile_interests:

        st.warning(
            "Please select at least one learning interest."
        )

    elif not profile_goal.strip():

        st.warning(
            "Please enter your learning goal."
        )

    else:

        # ----------------------------------------------------
        # CREATE PROFILE OBJECT
        # ----------------------------------------------------

        profile = create_profile(
            profile_name,
            profile_age_group,
            profile_user_type,
            profile_education,
            profile_interests,
            profile_goal
        )


        # ----------------------------------------------------
        # SAVE PROFILE IN SESSION
        # ----------------------------------------------------

        st.session_state["profile"] = profile


        # ----------------------------------------------------
        # SAVE USER IN DATABASE
        # ----------------------------------------------------

        user_id = add_user(
            profile_name,
            profile_age_group,
            profile_user_type,
            profile_education,
            profile_goal,
            profile_interests
        )


        # ----------------------------------------------------
        # SAVE USER ID
        # ----------------------------------------------------

        st.session_state["user_id"] = int(
            user_id
        )


        st.success(
            "✅ Your Protisruti profile has been created!"
        )

        st.info(
            f"Your profile ID is {user_id}."
        )


# ============================================================
# DISPLAY CURRENT PROFILE
# ============================================================

if "profile" in st.session_state:

    st.subheader(
        "Your Profile"
    )


    profile_summary = get_profile_summary(
        st.session_state["profile"]
    )


    st.markdown(
        profile_summary
    )


# ============================================================
# LEARNING PROGRESS
# ============================================================

st.header(
    "📊 Learning Progress"
)

st.write(
    """
    View your quiz history and track your learning progress.
    """
)


if "user_id" not in st.session_state:

    st.info(
        "Create a user profile to start tracking your progress."
    )

else:

    results = get_user_quiz_results(
        st.session_state["user_id"]
    )


    if not results:

        st.info(
            "You have not completed any quizzes yet."
        )

    else:

        st.subheader(
            "📈 Your Quiz History"
        )


        # ----------------------------------------------------
        # CALCULATE TOTALS
        # ----------------------------------------------------

        total_quizzes = len(
            results
        )


        total_score = sum(
            result[2]
            for result in results
        )


        total_questions = sum(
            result[3]
            for result in results
        )


        if total_questions > 0:

            overall_percentage = (
                total_score /
                total_questions
            ) * 100

        else:

            overall_percentage = 0


        # ----------------------------------------------------
        # METRICS
        # ----------------------------------------------------

        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Quizzes Completed",
                total_quizzes
            )


        with col2:

            st.metric(
                "Overall Score",
                f"{overall_percentage:.0f}%"
            )


        # ============================================================
        # QUIZ SCORE CHART
        # ============================================================

        st.subheader("📈 Quiz Score Trend")


        chart_data = []

        for result in results:

             chart_data.append({
                 "Quiz": f"{result[0]} - {result[1]}",
                  "Score": result[4]
        })


        if chart_data:

            chart_df = pd.DataFrame(chart_data)

            chart_df = chart_df.iloc[::-1]

        st.bar_chart(
            chart_df.set_index("Quiz")
        )
        
        
        
        # ----------------------------------------------------
        # RECENT RESULTS
        # ----------------------------------------------------

        st.subheader(
            "Recent Quiz Results"
        )


        for result in results:

            subject = result[0]

            topic = result[1]

            score = result[2]

            total = result[3]

            percentage = result[4]

            completed_at = result[5]


            st.write(
                f"### {subject} — {topic}"
            )


            st.write(
                f"Score: **{score}/{total}** "
                f"({percentage:.0f}%)"
            )


            st.caption(
                f"Completed: {completed_at}"
            )


            st.divider()
            
            
            
# ============================================================
# PROTISRUTI DASHBOARD
# ============================================================

st.header("🏠 My Dashboard")

st.write(
    """
    Welcome to your Protisruti learning dashboard.
    Here you can quickly see your profile, learning goal,
    quiz progress, and personalized recommendations.
    """
)


# ============================================================
# CHECK USER PROFILE
# ============================================================

if "user_id" not in st.session_state:

    st.info(
        """
        👤 You have not created or loaded a profile yet.

        Create a profile to see your personalized
        learning dashboard.
        """
    )

else:

    # ========================================================
    # USER PROFILE
    # ========================================================

    if "profile" in st.session_state:

        dashboard_profile = (
            st.session_state["profile"]
        )

        st.subheader("👤 Your Profile")

        profile_name = dashboard_profile.get(
            "name",
            "User"
        )

        learning_goal = dashboard_profile.get(
            "learning_goal",
            "Not specified"
        )

        interests = dashboard_profile.get(
            "interests",
            []
        )

        st.write(
            f"### Welcome, {profile_name}! 🌱"
        )

        st.write(
            f"**Learning Goal:** {learning_goal}"
        )

        if interests:

            st.write(
                "**Learning Interests:** "
                + ", ".join(interests)
            )

        else:

            st.write(
                "**Learning Interests:** Not specified"
            )


    # ========================================================
    # QUIZ PROGRESS
    # ========================================================

    st.subheader("📊 Your Learning Progress")


    dashboard_results = get_user_quiz_results(
        st.session_state["user_id"]
    )


    if dashboard_results:

        total_quizzes = len(
            dashboard_results
        )


        total_score = sum(
            result[2]
            for result in dashboard_results
        )


        total_questions = sum(
            result[3]
            for result in dashboard_results
        )


        if total_questions > 0:

            dashboard_percentage = (
                total_score /
                total_questions
            ) * 100

        else:

            dashboard_percentage = 0


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "📝 Quizzes Completed",
                total_quizzes
            )


        with col2:

            st.metric(
                "🎯 Questions Answered",
                total_questions
            )


        with col3:

            st.metric(
                "📈 Overall Score",
                f"{dashboard_percentage:.0f}%"
            )


        # ====================================================
        # LATEST QUIZ
        # ====================================================

        st.subheader("📝 Latest Quiz")


        latest_quiz = dashboard_results[0]


        latest_subject = latest_quiz[0]

        latest_topic = latest_quiz[1]

        latest_score = latest_quiz[2]

        latest_total = latest_quiz[3]

        latest_percentage = latest_quiz[4]

        latest_date = latest_quiz[5]


        st.write(
            f"**Subject:** {latest_subject}"
        )

        st.write(
            f"**Topic:** {latest_topic}"
        )

        st.write(
            f"**Score:** "
            f"{latest_score}/{latest_total} "
            f"({latest_percentage:.0f}%)"
        )

        st.caption(
            f"Completed: {latest_date}"
        )


    else:

        st.info(
            """
            📝 You have not completed a quiz yet.

            Complete your first quiz to start tracking
            your learning progress.
            """
        )


    # ========================================================
    # DASHBOARD RECOMMENDATION
    # ========================================================

    if "profile" in st.session_state:

        dashboard_recommendations = (
            generate_recommendations(
                st.session_state["profile"],
                dashboard_results
            )
        )


        st.subheader(
            "💡 Recommended for You"
        )


        for recommendation in (
            dashboard_recommendations[:3]
        ):

            st.markdown(
                f"• {recommendation}"
            )
            
            
            
# ============================================================
# PERSONALIZED RECOMMENDATIONS
# ============================================================

st.header("💡 Personalized Recommendations")

st.write(
    """
    Protisruti uses your profile and quiz performance
    to suggest what you may want to learn next.
    """
)


if "user_id" not in st.session_state:

    st.info(
        "Create or load a profile to receive "
        "personalized recommendations."
    )

else:

    if "profile" not in st.session_state:

        st.info(
            "Load your profile to receive "
            "personalized recommendations."
        )

    else:

        user_results = get_user_quiz_results(
            st.session_state["user_id"]
        )


        recommendations = generate_recommendations(
            st.session_state["profile"],
            user_results
        )


        st.subheader(
            "Recommended for You"
        )


        for recommendation in recommendations:

            st.markdown(
                f"• {recommendation}"
            )


# ============================================================
# SIDEBAR USER STATUS
# ============================================================

st.sidebar.markdown(
    "---"
)


if "user_id" in st.session_state:

    st.sidebar.success(
        f"Profile ID: "
        f"{st.session_state['user_id']}"
    )

else:

    st.sidebar.info(
        "No profile created yet."
    )