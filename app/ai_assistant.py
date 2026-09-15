def get_local_response(question):
    """
    Provide a local response for development and testing.
    """

    question_lower = question.lower()

    if "photosynthesis" in question_lower:
        answer = """
Photosynthesis is the process plants use to make their own food.

Plants use:
- Sunlight
- Water
- Carbon dioxide

to produce:
- Glucose (food)
- Oxygen

In simple words, plants use sunlight to turn water and carbon dioxide
into food and oxygen.
"""

        next_topic = (
            "Learn about cellular respiration to understand how "
            "plants and other organisms use stored energy."
        )

    elif "python" in question_lower:
        answer = """
Python is a programming language that is easy to learn and widely used
for software development, data analysis, artificial intelligence,
automation, and web development.

For example:

print("Hello, Protisruti!")

This tells Python to display the words "Hello, Protisruti!".
"""

        next_topic = (
            "Try learning Python variables and conditional statements "
            "next."
        )

    elif (
        "machine learning" in question_lower
        or "artificial intelligence" in question_lower
        or question_lower.strip() == "ai"
    ):
        answer = """
Machine learning is a part of artificial intelligence that allows
computers to learn patterns from data and make predictions or decisions.

For example, a machine learning model can learn from students'
previous exam results and use that information to predict whether
a student may pass or fail.

A simple machine learning process includes:

1. Collect data
2. Prepare the data
3. Train a model
4. Test the model
5. Use the model to make predictions

In simple words, machine learning helps computers learn from data
instead of being programmed with every possible rule.
"""

        next_topic = (
            "Learn about supervised learning and how classification "
            "and regression models are used to make predictions."
        )

    elif "data science" in question_lower:
        answer = """
Data science is the process of using data to find useful information,
patterns, and insights.

It combines several important areas, including:

- Programming
- Statistics
- Data analysis
- Machine learning
- Data visualization

For example, a data scientist could analyze student performance data
to understand learning patterns and help predict future results.

In simple words, data science helps us turn raw data into useful
information for making better decisions.
"""

        next_topic = (
            "Learn about data cleaning, exploratory data analysis, "
            "and how Python libraries such as pandas are used."
        )

    elif "statistics" in question_lower or "statistical" in question_lower:
        answer = """
Statistics is the study of collecting, organizing, analyzing,
and interpreting data.

Some common statistical concepts include:

- Mean
- Median
- Mode
- Range
- Standard deviation

For example, we can use statistics to calculate the average exam
score of a group of students and understand how their scores differ.

In simple words, statistics helps us understand data and identify
patterns or useful information.
"""

        next_topic = (
            "Learn about mean, median, mode, and standard deviation "
            "using a small dataset."
        )

    elif "computer" in question_lower:
        answer = """
A computer is an electronic device that receives data, processes it,
stores information, and produces results.

The four basic functions are:

1. Input
2. Processing
3. Storage
4. Output

For example, when you type something on a keyboard, the computer
receives the input, processes it, and displays the result on the screen.
"""

        next_topic = (
            "Learn about the CPU, memory, and storage to understand "
            "how a computer processes information."
        )

    elif "math" in question_lower or "mathematics" in question_lower:
        answer = """
Mathematics is the study of numbers, quantities, patterns, shapes,
and relationships.

Some important areas of mathematics include:

- Arithmetic
- Algebra
- Geometry
- Statistics
- Calculus

Mathematics helps us solve problems in everyday life, science,
engineering, computing, and many other fields.
"""

        next_topic = (
            "Try learning basic algebra and practice solving simple "
            "equations."
        )

    else:
        answer = f"""
Thank you for your question:

"{question}"

Protisruti is here to support your learning journey.

This is currently the development version of Protisruti's
AI Learning Companion. A full AI model is not connected yet,
but you can still continue learning by asking focused questions
about a specific concept, example, problem, or skill.

You can also ask me about:
- Photosynthesis
- Python
- Machine Learning
- Data Science
- Statistics
- Computers
- Mathematics
"""

        next_topic = (
            "Try asking a more specific question about a concept, "
            "example, problem, or skill you want to understand."
        )

    return answer, next_topic


def ask_ai(question, profile=None):
    """
    Protisruti AI Learning Companion.

    The user's profile is optional.
    If available, the profile can be used to personalize
    the learning response and suggest what to learn next.
    """

    if not question.strip():
        return "Please enter a question so Protisruti can help you learn."
    
    question_lower = question.lower()
    
    learning_goal = ""
    interests = []

    if profile:
        learning_goal = profile.get(
            "learning_goal",
            ""
        )

        interests = profile.get(
            "interests",
            []
        )

    answer, next_topic = get_local_response(question)

    # Personalized learning guidance
    if learning_goal:
        answer += (
            f"\n\nPersonalized Learning Tip:\n"
            f"Your current learning goal is: {learning_goal}\n"
            f"Try connecting this topic to your goal as you continue learning."
        )

    if interests:
        answer += (
            f"\nYour learning interests include: "
            f"{', '.join(interests)}."
        )

        related_interests = []

        for interest in interests:
            interest_lower = interest.lower()

            if (
                    interest_lower in question_lower
                    or (
                        interest_lower == "programming"
                        and (
                            "python" in question_lower
                            or "code" in question_lower
                            or "coding" in question_lower
                            or "programming" in question_lower
                        )
                    )
                    or (
                        interest_lower in [
                            "artificial intelligence",
                            "ai"
                        ]
                        and (
                            "python" in question_lower
                            or "machine learning" in question_lower
                            or "artificial intelligence" in question_lower
                            or "ai" in question_lower
                        )
                    )
                ):
                    related_interests.append(interest)

            if related_interests:
                answer += (
                    "\n\nConnection to Your Interests:\n"
                    f"This topic connects with your interest in "
                    f"{', '.join(related_interests)}."
                )

    # Next learning suggestion
    answer += (
        f"\n\nWhat to Learn Next:\n"
        f"{next_topic}"
    )

    return answer