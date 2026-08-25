def create_study_plan(
    learning_goal,
    skill_level,
    study_time,
    duration
):
    """
    Create a personalized study plan.

    This is the local development version.
    A real AI model can be connected later.
    """

    goal = learning_goal.lower()

    if "python" in goal:

        if duration <= 4:

            plan = f"""
🌱 Python Learning Plan

Goal: {learning_goal}
Level: {skill_level}
Study Time: {study_time}
Duration: {duration} weeks

Week 1 — Python Basics
- Variables
- Data types
- print()
- Basic operators
- Simple exercises

Week 2 — Conditions and Loops
- if / elif / else
- for loops
- while loops
- Practice problems

Week 3 — Functions and Data Structures
- Functions
- Lists
- Tuples
- Dictionaries
- Sets

Week 4 — Mini Project
- Build a small Python project
- Practice debugging
- Review previous topics
- Complete a final project

Study Recommendation:
Try to study consistently and practice by writing code yourself.
"""

        else:

            plan = f"""
🌱 Extended Python Learning Plan

Goal: {learning_goal}
Level: {skill_level}
Study Time: {study_time}
Duration: {duration} weeks

Weeks 1–2
Python fundamentals

Weeks 3–4
Conditions and loops

Weeks 5–6
Functions and data structures

Weeks 7–8
File handling and error handling

Weeks 9–10
Object-oriented programming

Weeks 11–12
Build a practical Python project

Remaining weeks:
Review, practice, and improve your project.
"""

    elif "english" in goal:

        plan = f"""
🌱 English Learning Plan

Goal: {learning_goal}
Level: {skill_level}
Study Time: {study_time}
Duration: {duration} weeks

Week 1
- Basic vocabulary
- Common expressions
- Simple sentences

Week 2
- Grammar fundamentals
- Present, past, and future tense

Week 3
- Reading practice
- Short passages
- Vocabulary building

Week 4
- Writing practice
- Conversation practice
- Review

Study Recommendation:
Practice speaking, reading, writing, and listening every day.
"""

    elif "math" in goal or "mathematics" in goal:

        plan = f"""
🌱 Mathematics Learning Plan

Goal: {learning_goal}
Level: {skill_level}
Study Time: {study_time}
Duration: {duration} weeks

Week 1
- Number systems
- Basic arithmetic
- Fractions

Week 2
- Percentages
- Ratios
- Proportions

Week 3
- Algebra basics
- Equations
- Variables

Week 4
- Word problems
- Practice exercises
- Review

Study Recommendation:
Practice several problems every day and review mistakes carefully.
"""

    else:

        plan = f"""
🌱 Personalized Learning Plan

Goal: {learning_goal}
Level: {skill_level}
Study Time: {study_time}
Duration: {duration} weeks

Week 1
- Introduction to the topic
- Learn the basic concepts

Week 2
- Study important concepts
- Practice simple exercises

Week 3
- Practice intermediate concepts
- Work on small exercises

Week 4
- Review previous topics
- Complete a small project

Study Recommendation:
Study consistently and practice what you learn.
"""

    return plan