import os


def get_ai_api_key():
    """
    Get the AI API key from the environment.

    The API key should be stored in the .env file
    and should never be committed to GitHub.
    """

    return os.getenv("OPENAI_API_KEY")