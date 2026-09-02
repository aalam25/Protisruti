def get_quiz(subject, topic, difficulty, number_of_questions):
    """
    Return a local quiz based on the selected subject and topic.
    """

    quizzes = {
        "Python": {
            "Functions": [
                {
                    "question": "What keyword is used to define a function in Python?",
                    "options": [
                        "function",
                        "def",
                        "define",
                        "fun"
                    ],
                    "answer": "def",
                    "explanation": "The 'def' keyword is used to define a function in Python."
                },
                {
                    "question": "What does a Python function allow you to do?",
                    "options": [
                        "Reuse a block of code",
                        "Delete Python",
                        "Create a computer",
                        "Install Windows"
                    ],
                    "answer": "Reuse a block of code",
                    "explanation": "Functions allow you to organize and reuse code."
                },
                {
                    "question": "Which statement is used to return a value from a function?",
                    "options": [
                        "send",
                        "return",
                        "output",
                        "give"
                    ],
                    "answer": "return",
                    "explanation": "The return statement sends a value back from a function."
                },
                {
                    "question": "Which of the following is a valid Python function definition?",
                    "options": [
                        "def greet():",
                        "function greet():",
                        "create greet():",
                        "fun greet():"
                    ],
                    "answer": "def greet():",
                    "explanation": "Python functions are defined using the def keyword."
                },
                {
                    "question": "What happens when a function is called?",
                    "options": [
                        "The function's code is executed",
                        "The function is deleted",
                        "Python closes",
                        "The computer restarts"
                    ],
                    "answer": "The function's code is executed",
                    "explanation": "Calling a function causes its instructions to execute."
                }
            ]
        },

        "Mathematics": {
            "Basic Arithmetic": [
                {
                    "question": "What is 5 + 7?",
                    "options": [
                        "10",
                        "11",
                        "12",
                        "13"
                    ],
                    "answer": "12",
                    "explanation": "5 + 7 = 12."
                },
                {
                    "question": "What is 10 × 3?",
                    "options": [
                        "20",
                        "30",
                        "40",
                        "13"
                    ],
                    "answer": "30",
                    "explanation": "10 × 3 = 30."
                },
                {
                    "question": "What is 20 ÷ 4?",
                    "options": [
                        "4",
                        "5",
                        "6",
                        "8"
                    ],
                    "answer": "5",
                    "explanation": "20 divided by 4 equals 5."
                },
                {
                    "question": "What is 15 - 6?",
                    "options": [
                        "7",
                        "8",
                        "9",
                        "10"
                    ],
                    "answer": "9",
                    "explanation": "15 - 6 = 9."
                },
                {
                    "question": "What is 8 × 8?",
                    "options": [
                        "56",
                        "64",
                        "72",
                        "81"
                    ],
                    "answer": "64",
                    "explanation": "8 × 8 = 64."
                }
            ]
        },

        "English": {
            "Grammar": [
                {
                    "question": "Which word is a noun?",
                    "options": [
                        "Quickly",
                        "Beautiful",
                        "Teacher",
                        "Run"
                    ],
                    "answer": "Teacher",
                    "explanation": "A teacher is a person, so 'teacher' is a noun."
                },
                {
                    "question": "Which sentence is grammatically correct?",
                    "options": [
                        "She go to school.",
                        "She goes to school.",
                        "She going school.",
                        "She gone school."
                    ],
                    "answer": "She goes to school.",
                    "explanation": "With 'she', the verb 'go' becomes 'goes' in the simple present."
                },
                {
                    "question": "What is the past tense of 'go'?",
                    "options": [
                        "Goed",
                        "Going",
                        "Went",
                        "Gone"
                    ],
                    "answer": "Went",
                    "explanation": "The simple past tense of 'go' is 'went'."
                },
                {
                    "question": "Which word is an adjective?",
                    "options": [
                        "Beautiful",
                        "Run",
                        "Quickly",
                        "Teacher"
                    ],
                    "answer": "Beautiful",
                    "explanation": "An adjective describes a noun."
                },
                {
                    "question": "Which word is a verb?",
                    "options": [
                        "Happy",
                        "School",
                        "Run",
                        "Blue"
                    ],
                    "answer": "Run",
                    "explanation": "A verb describes an action. 'Run' is an action."
                }
            ]
        }
    }
    
    if number_of_questions <= 0:
        return []

    try:
        questions = quizzes[subject][topic]
    except KeyError:
        return []

    if difficulty == "Beginner":
        questions = questions[:]

    elif difficulty == "Intermediate":
        questions = questions[1:]

    elif difficulty == "Advanced":
        questions = questions[2:]

    return questions[:number_of_questions]