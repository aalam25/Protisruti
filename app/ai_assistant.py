def ask_ai(question):
    """
    Temporary local AI Learning Companion.

    This function is used during development while the
    real AI API is not connected.
    """

    question_lower = question.lower()

    if "photosynthesis" in question_lower:
        return """
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

    elif "python" in question_lower:
        return """
Python is a programming language that is easy to learn and widely used
for software development, data analysis, artificial intelligence,
automation, and web development.

For example:

print("Hello, Protisruti!")

This tells Python to display the words "Hello, Protisruti!".
"""

    elif "computer" in question_lower:
        return """
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

    elif "math" in question_lower or "mathematics" in question_lower:
        return """
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

    else:
        return f"""
Thank you for your question:

"{question}"

This is currently the development version of Protisruti's
AI Learning Companion.

The local version can demonstrate the application interface and
learning workflow. A real AI model will be connected in a later
development stage.

For now, try asking about:
- Photosynthesis
- Python
- Computers
- Mathematics
"""