# ============================================================
# PROTISRUTI PERSONALIZED RECOMMENDATIONS
# ============================================================


def generate_recommendations(profile, quiz_results):
    """
    Generate personalized learning recommendations
    based on the user's profile and quiz performance.
    """

    recommendations = []


    # ========================================================
    # PROFILE INFORMATION
    # ========================================================

    learning_goal = profile.get(
        "learning_goal",
        ""
    )

    interests = profile.get(
        "interests",
        []
    )


    # ========================================================
    # LEARNING GOAL RECOMMENDATION
    # ========================================================

    if learning_goal:

        recommendations.append(
            f"Continue working toward your goal: "
            f"**{learning_goal}**."
        )


    # ========================================================
    # INTEREST RECOMMENDATIONS
    # ========================================================

    if interests:

        for interest in interests[:3]:

            recommendations.append(
                f"Explore more learning materials in "
                f"**{interest}**."
            )


    # ========================================================
    # QUIZ PERFORMANCE
    # ========================================================

    if quiz_results:

        # Find the most recent quiz result

        latest_result = quiz_results[0]

        subject = latest_result[0]

        topic = latest_result[1]

        score = latest_result[2]

        total_questions = latest_result[3]

        percentage = latest_result[4]


        # ----------------------------------------------------
        # LOW SCORE
        # ----------------------------------------------------

        if percentage < 60:

            recommendations.append(
                f"Your recent **{subject} — {topic}** "
                f"quiz score was **{percentage:.0f}%**. "
                f"Review this topic and practice again."
            )


        # ----------------------------------------------------
        # MEDIUM SCORE
        # ----------------------------------------------------

        elif percentage < 80:

            recommendations.append(
                f"You are making progress in "
                f"**{subject} — {topic}**. "
                f"Review the topic and try another practice quiz."
            )


        # ----------------------------------------------------
        # HIGH SCORE
        # ----------------------------------------------------

        else:

            recommendations.append(
                f"Excellent work on **{subject} — {topic}** "
                f"with a score of **{percentage:.0f}%**. "
                f"Consider moving to a more advanced topic."
            )


    # ========================================================
    # DEFAULT RECOMMENDATION
    # ========================================================

    if not recommendations:

        recommendations.append(
            "Start by choosing a subject you would like "
            "to learn and complete a practice quiz."
        )


    return recommendations