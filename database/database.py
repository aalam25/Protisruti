import sqlite3
from pathlib import Path


# ============================================================
# DATABASE LOCATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_FOLDER = PROJECT_ROOT / "database"

DATABASE_FILE = DATABASE_FOLDER / "protisruti.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    DATABASE_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(
        DATABASE_FILE
    )

    return connection


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # USERS TABLE
    # --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age_group TEXT,
            user_type TEXT,
            education_level TEXT,
            interests TEXT,
            learning_goal TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


    # --------------------------------------------------------
    # ADD INTERESTS COLUMN TO EXISTING DATABASE
    # --------------------------------------------------------

    cursor.execute(
        "PRAGMA table_info(users)"
    )

    columns = [
        column[1]
        for column in cursor.fetchall()
    ]


    if "interests" not in columns:

        cursor.execute(
            """
            ALTER TABLE users
            ADD COLUMN interests TEXT
            """
        )


    # --------------------------------------------------------
    # QUIZ RESULTS TABLE
    # --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            percentage REAL NOT NULL,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
    )


    connection.commit()

    connection.close()


# ============================================================
# ADD USER
# ============================================================

def add_user(
    name,
    age_group,
    user_type,
    education_level,
    learning_goal,
    interests=None
):

    connection = get_connection()

    cursor = connection.cursor()


    if interests is None:

        interests_text = ""

    elif isinstance(interests, list):

        interests_text = ", ".join(interests)

    else:

        interests_text = str(interests)


    cursor.execute(
        """
        INSERT INTO users (
            name,
            age_group,
            user_type,
            education_level,
            interests,
            learning_goal
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            age_group,
            user_type,
            education_level,
            interests_text,
            learning_goal
        )
    )


    user_id = cursor.lastrowid


    connection.commit()

    connection.close()


    return user_id


# ============================================================
# SAVE QUIZ RESULT
# ============================================================

def save_quiz_result(
    user_id,
    subject,
    topic,
    score,
    total_questions
):

    if total_questions <= 0:

        return


    percentage = (
        score / total_questions
    ) * 100


    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO quiz_results (
            user_id,
            subject,
            topic,
            score,
            total_questions,
            percentage
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            subject,
            topic,
            score,
            total_questions,
            percentage
        )
    )


    connection.commit()

    connection.close()


# ============================================================
# GET USER QUIZ RESULTS
# ============================================================

def get_user_quiz_results(user_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            subject,
            topic,
            score,
            total_questions,
            percentage,
            completed_at
        FROM quiz_results
        WHERE user_id = ?
        ORDER BY completed_at DESC
        """,
        (user_id,)
    )


    results = cursor.fetchall()

    connection.close()


    return results


# ============================================================
# FIND USER BY NAME
# ============================================================

def get_user_by_name(name):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            id,
            name,
            age_group,
            user_type,
            education_level,
            interests,
            learning_goal,
            created_at
        FROM users
        WHERE name = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (name,)
    )


    user = cursor.fetchone()

    connection.close()


    return user