# ============================================================
# PROTISRUTI STUDY PLANNER
# ============================================================


def create_study_plan(
    learning_goal,
    skill_level,
    study_time,
    duration,
    profile=None
):
    """
    Create a personalized study plan.

    The user's profile is optional.
    If available, it can provide additional context
    about the learner's interests and broader goal.
    """

    # ========================================================
    # BASIC INFORMATION
    # ========================================================

    learning_goal = learning_goal.strip()


    # ========================================================
    # PROFILE INFORMATION
    # ========================================================

    profile_goal = ""

    interests = []


    if profile:

        profile_goal = profile.get(
            "learning_goal",
            ""
        )

        interests = profile.get(
            "interests",
            []
        )


    # ========================================================
    # CREATE PLAN
    # ========================================================

    plan = f"""
# 📚 Personalized Study Plan

## 🎯 Learning Goal

**{learning_goal}**

## 📊 Current Level

**{skill_level}**

## ⏰ Daily Study Time

**{study_time}**

## 🗓️ Study Duration

**{duration} weeks**

"""


    # ========================================================
    # PROFILE CONNECTION
    # ========================================================

    if profile_goal:

        plan += f"""
## 👤 Your Broader Goal

Your profile indicates that your broader learning goal is:

**{profile_goal}**

This study plan is designed to support your current
learning goal while keeping your broader goal in mind.

"""


    # ========================================================
    # INTERESTS
    # ========================================================

    if interests:

        interest_text = ", ".join(interests)

        plan += f"""
## 🌱 Your Interests

You are interested in:

**{interest_text}**

You can connect these interests with your current
learning goal as you progress.

"""


    # ========================================================
    # WEEKLY PLAN
    # ========================================================

    plan += """
## 🗓️ Weekly Plan

"""


    for week in range(
        1,
        int(duration) + 1
    ):

        if week == 1:

            topic = (
                f"Introduction to {learning_goal} "
                "and basic concepts"
            )

        elif week == 2:

            topic = (
                f"Core concepts and practical exercises "
                f"in {learning_goal}"
            )

        elif week == 3:

            topic = (
                f"Practice, problem solving, and "
                f"real-world applications of {learning_goal}"
            )

        else:

            topic = (
                f"Review, projects, and advanced practice "
                f"related to {learning_goal}"
            )


        plan += f"""
### Week {week}

**Focus:** {topic}

**Daily Study Time:** {study_time}

**Suggested Activities:**

- Learn the main concepts.
- Take notes on important ideas.
- Practice what you learned.
- Complete small exercises.
- Review previous material.
- Ask Protisruti questions when you need help.

"""


    # ========================================================
    # FINAL ADVICE
    # ========================================================

    plan += """
## 💡 Study Tips

- Study consistently rather than trying to learn everything at once.
- Practice what you learn.
- Review difficult topics regularly.
- Use quizzes to measure your progress.
- Ask the AI Learning Companion when you need an explanation.
- Celebrate small improvements.

🌱 Keep learning step by step. Progress takes time.
"""


    return plan