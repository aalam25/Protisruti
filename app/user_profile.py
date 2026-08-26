def create_profile(
    name,
    age_group,
    user_type,
    education_level,
    interests,
    learning_goal
):
    """
    Create a user profile for Protisruti.
    """

    profile = {
        "name": name,
        "age_group": age_group,
        "user_type": user_type,
        "education_level": education_level,
        "interests": interests,
        "learning_goal": learning_goal
    }

    return profile


def get_profile_summary(profile):
    """
    Create a readable summary of the user's profile.
    """

    interests_text = ", ".join(
        profile["interests"]
    )

    summary = f"""
### 👤 Profile Summary

**Name:** {profile["name"]}

**Age Group:** {profile["age_group"]}

**User Type:** {profile["user_type"]}

**Education Level:** {profile["education_level"]}

**Learning Interests:** {interests_text}

**Learning Goal:** {profile["learning_goal"]}
"""

    return summary