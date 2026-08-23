# Protisruti — Technical Requirements & System Architecture

## 1. Purpose

This document defines the technical requirements, technology stack, system
architecture, and development approach for Protisruti.

Protisruti is an AI-powered educational and empowerment platform designed
to support women and children through personalized learning, skill
development, educational guidance, and access to opportunities.

The initial objective is to develop a functional prototype that can be
tested and demonstrated as part of the fellowship project before the
October 2026 deadline.

---

## 2. Project Goals

The technical development of Protisruti will focus on creating a platform
that is:

- Easy to use
- Accessible
- Mobile-friendly
- Reliable
- Secure
- Maintainable
- Responsible in its use of artificial intelligence
- Suitable for users with different levels of technical experience

The first version will prioritize the most important features rather than
trying to build a large and complicated system.

---

## 3. Target Users

Protisruti will initially support two primary groups.

### 3.1 Students and Children

The platform will help students:

- Ask educational questions
- Understand difficult concepts
- Generate practice questions
- Create study plans
- Practice academic subjects
- Track learning progress

### 3.2 Women

The platform will help women:

- Learn digital skills
- Improve English and communication skills
- Learn programming
- Explore career pathways
- Explore educational opportunities
- Find scholarships and free learning resources
- Create personalized learning plans
- Track learning progress

---

## 4. Core Functional Requirements

### 4.1 User Interface

The application must provide a simple interface where users can:

- Open the Protisruti application
- Select their user type
- Select a learning goal
- Enter questions
- Interact with the AI Learning Companion
- Create study plans
- Generate quizzes
- Explore learning resources
- View basic learning progress

The interface should use simple language and clear navigation.

### 4.2 AI Learning Companion

The AI Learning Companion will be one of the central features of
Protisruti.

Users should be able to ask questions using natural language.

The AI should be able to:

- Explain difficult concepts
- Provide simple explanations
- Provide examples
- Answer follow-up questions
- Break complicated topics into smaller steps
- Adjust explanations based on the user's learning level
- Provide educational guidance
- Encourage independent learning

The AI should not simply provide answers. It should help users understand
the topic.

### 4.3 Personalized Study Planner

The Study Planner will help users create structured learning plans.

Users may provide:

- Learning goal
- Subject or skill
- Current skill level
- Available study time
- Target duration

The system will generate a personalized study plan.

A study plan may include:

- Topics to study
- Recommended activities
- Practice tasks
- Suggested study schedule
- Learning goals
- Progress checkpoints

### 4.4 AI Quiz Generator

The Quiz Generator will allow users to create practice quizzes.

Users may select:

- Subject
- Topic
- Difficulty level
- Number of questions

The system should:

1. Generate questions.
2. Display the questions.
3. Allow the user to submit answers.
4. Calculate the result.
5. Provide feedback.
6. Explain incorrect answers.
7. Save the basic quiz result.

### 4.5 Women's Skills Learning

The Women's Skills section will provide structured learning pathways.

Possible areas include:

- Digital literacy
- Computer fundamentals
- English
- Communication
- Programming
- Resume development
- Professional skills
- Career preparation

Users should be able to select a skill and receive a beginner-friendly
learning pathway.

### 4.6 Career and Educational Guidance

Protisruti will help users explore possible educational and career
pathways.

Users may provide:

- Interests
- Skills
- Educational background
- Learning goals

The system may provide:

- Possible career areas
- Relevant skills
- Suggested learning paths
- Educational resources
- General career information

The system will provide general educational guidance and should not make
high-stakes decisions on behalf of users.

### 4.7 Opportunity Finder

The Opportunity Finder will help users discover relevant educational and
professional opportunities.

Possible opportunities include:

- Scholarships
- Free courses
- Training programs
- Educational resources
- Career-development resources

The first version may use a manually curated dataset.

Information should come from reliable and verifiable sources.

### 4.8 Progress Tracker

The Progress Tracker will allow users to monitor basic learning progress.

Possible information includes:

- Learning goals
- Completed activities
- Quiz scores
- Completed lessons
- Progress toward learning goals

The initial version will use simple progress tracking rather than complex
learning analytics.

---

## 5. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| User Interface | Streamlit |
| AI | Large Language Model API |
| Database | SQLite |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Version Control | Git |
| Repository | GitHub |

---

## 6. Technology Selection

### 6.1 Python

Python will be the primary programming language for Protisruti.

Python is suitable because it provides strong support for:

- Artificial intelligence
- Machine learning
- Data processing
- APIs
- Web applications
- Rapid prototyping

### 6.2 Streamlit

Streamlit will be used to create the initial web application.

Streamlit is appropriate for the first version because:

- It works well with Python.
- It is suitable for AI applications.
- It allows rapid development.
- It requires less frontend complexity.
- It is suitable for demonstrations and prototypes.

A more advanced frontend may be considered in a future version.

### 6.3 Large Language Model API

A large language model will provide the main AI capabilities of
Protisruti.

The AI will be used for:

- Educational explanations
- Study-plan generation
- Quiz generation
- Learning guidance
- Career and educational guidance

The specific AI provider and model will be selected during implementation.

### 6.4 SQLite

SQLite will be used as the initial database.

SQLite is suitable for the prototype because it is:

- Lightweight
- Easy to configure
- Free
- Suitable for small applications
- Easy to use with Python

Potential information stored in the database includes:

- Learning goals
- Quiz results
- Learning activities
- Progress information
- Educational resources

### 6.5 Pandas

Pandas may be used for structured data processing.

Potential uses include:

- Processing educational resources
- Managing opportunity datasets
- Analyzing learning activity
- Preparing project impact data

### 6.6 Scikit-learn

Scikit-learn may be introduced for future machine-learning functionality.

Potential future uses include:

- Personalized recommendations
- Learning analytics
- User segmentation
- Recommendation systems

Machine learning is not required for the first functional prototype.

### 6.7 Git and GitHub

Git and GitHub will be used throughout the development process.

They will be used for:

- Version control
- Code management
- Project documentation
- Tracking changes
- Maintaining development history
- Demonstrating the project to fellowship reviewers

---

## 7. Basic System Architecture

The initial Protisruti architecture will follow a simple layered design.

```text
                         USER
                           |
                           v
                  +----------------+
                  |   Streamlit    |
                  | User Interface |
                  +-------+--------+
                          |
                          v
                  +----------------+
                  |  Application   |
                  |     Logic      |
                  +-------+--------+
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
   AI Assistant     Study Planner    Quiz Generator
          |               |               |
          +---------------+---------------+
                          |
                          v
                  +----------------+
                  |   AI Model     |
                  |      API       |
                  +-------+--------+
                          |
                          v
                  +----------------+
                  |     SQLite     |
                  |    Database    |
                  +----------------+
                          |
                          v
                  +----------------+
                  |   Educational  |
                  |    Resources   |
                  +----------------+

```

## 8. Main System Components

### 8.1 User Interface Layer

The Streamlit interface will provide the main interaction between users
and Protisruti.

Potential sections include:

- Home
- Student Learning
- Women's Skills
- AI Learning Companion
- Study Planner
- Quiz Generator
- Opportunity Finder
- Progress Dashboard

### 8.2 Application Logic Layer

The application logic will connect the user interface with the AI system,
database, and other components.

It will handle:

- User inputs
- Input validation
- Feature selection
- AI requests
- Database operations
- Progress calculations
- Error handling

### 8.3 AI Layer

The AI layer will communicate with the selected large language model API.

It will provide:

- Educational explanations
- Study plans
- Quiz questions
- Learning recommendations
- Career guidance

The application will use structured prompts to improve consistency and
quality.

### 8.4 Database Layer

SQLite will store appropriate application data.

Potential database tables include:

#### Users

Stores only the basic information required by the application.

#### Learning Goals

May store:

- Goal
- Subject
- Skill
- Target date
- Status

#### Quiz Results

May store:

- Topic
- Score
- Date
- Difficulty

#### Progress

May store:

- Completed activities
- Learning progress
- Goals

#### Resources

May store:

- Resource name
- Resource type
- Description
- URL
- Target audience
- Subject or skill

The database should not store unnecessary sensitive information.

---

## 9. Basic User Flow

```text
                     Open Protisruti
                            |
                            v
                    Select User Type
                            |
               +------------+------------+
               |                         |
               v                         v
            Student                    Woman
               |                         |
               v                         v
         Choose Goal               Choose Goal
               |                         |
               +------------+------------+
                            |
                            v
                  Personalized Support
                            |
               +------------+------------+
               |            |            |
               v            v            v
             Learn        Quiz       Study Plan
               |            |            |
               +------------+------------+
                            |
                            v
                     Track Progress
                            |
                            v
                Discover Opportunities

```

## 10. AI Request Flow

When a user asks the AI Learning Companion a question, the basic process will be:

User Question
      |
      v
Streamlit Interface
      |
      v
Input Validation
      |
      v
Prompt Construction
      |
      v
AI Model API
      |
      v
AI Response
      |
      v
Response Validation
      |
      v
Display Response

The application should avoid sending unnecessary personal information to the AI service.

---

## 11. Study Planner Flow

The Study Planner will use information provided by the user to create a personalized learning plan.

The user may provide:

- Learning goal
- Subject or skill
- Current skill level
- Available study time
- Target duration

The basic process will be:

User Learning Goal
        |
        v
Current Skill Level
        |
        v
Available Study Time
        |
        v
Target Duration
        |
        v
Prompt Construction
        |
        v
AI Model
        |
        v
Structured Study Plan
        |
        v
Display Study Plan
        |
        v
Save Progress

The generated plan should be clear, realistic, and appropriate for the user's stated learning goal.

---

## 12. Quiz Generation Flow

The Quiz Generator will create practice questions based on the user's selected topic.

The user may select:

- Subject
- Topic
- Difficulty level
- Number of questions

The basic process will be:

Subject
   |
   v
Topic
   |
   v
Difficulty
   |
   v
Number of Questions
   |
   v
AI Quiz Generation
   |
   v
Display Questions
   |
   v
User Answers
   |
   v
Calculate Score
   |
   v
Provide Feedback
   |
   v
Save Result

The system should provide explanations for incorrect answers whenever possible.

---

## 13. Opportunity Finder Flow

The first version of the Opportunity Finder will use a structured resource database.

The basic process will be:

Educational Resources
        |
        v
Resource Database
        |
        v
User Interests
        |
        v
User Goals
        |
        v
Filtering
        |
        v
Relevant Opportunities

The initial dataset may be manually created and verified.

Possible opportunities include:

- Scholarships
- Free courses
- Training programs
- Educational resources
- Career-development resources

Future versions may integrate external APIs or verified data sources.

The application should avoid presenting outdated or unverified opportunities as current information.

---

## 14. Security Requirements

Protisruti will follow basic security practices.

The application should:

- Never store API keys directly in source code.
- Use environment variables for secrets.
- Store API credentials outside the public repository.
- Add `.env` to `.gitignore`.
- Validate user inputs.
- Avoid unnecessary personal data collection.
- Protect stored user information.
- Avoid exposing database credentials.
- Handle application errors safely.
- Avoid displaying sensitive technical information to users.

API keys and other private credentials must never be committed to GitHub.

---

## 15. Privacy Requirements

Protisruti will follow a data-minimization approach.

The application should collect only information necessary for providing the intended functionality.

Potential information may include:

- Learning goals
- Selected subjects
- Skill level
- Quiz results
- Learning progress

The application should avoid collecting unnecessary sensitive information.

For children, the system should use additional privacy protections and should not request unnecessary personal information.

The project will prioritize privacy during both development and future deployment.


## 16. Responsible AI Requirements

Responsible AI is an important part of Protisruti because the platform may
be used by women and children.

The system should:

- Clearly identify AI-generated information.
- Avoid presenting uncertain information as fact.
- Encourage verification of important information.
- Avoid high-stakes decision-making.
- Provide supportive and respectful responses.
- Avoid inappropriate content.
- Use age-appropriate language for children.
- Avoid collecting unnecessary personal information.
- Avoid making decisions about users based on sensitive personal
  characteristics.
- Provide users with the ability to review AI-generated information.

AI-generated information should be treated as assistance rather than a
replacement for teachers, parents, counselors, or qualified professionals.

---

## 17. Child Safety Requirements

Because children may use Protisruti, additional safeguards are necessary.

The child-facing portion should:

- Use age-appropriate language.
- Avoid inappropriate content.
- Avoid requesting sensitive personal information.
- Avoid encouraging unsafe behavior.
- Provide educationally appropriate assistance.
- Encourage involvement of parents, guardians, teachers, or other trusted
  adults when appropriate.
- Avoid creating inappropriate or unsafe interactions.
- Avoid providing instructions that could put a child at risk.

Any real-world deployment involving children should undergo additional
privacy and safety review.

The fellowship prototype will prioritize demonstrating the educational
value of the system while maintaining appropriate safety boundaries.

---

## 18. Accessibility Requirements

Protisruti should be designed for users with different educational,
technical, and language backgrounds.

The interface should:

- Use clear and simple language.
- Use simple navigation.
- Use readable text.
- Provide clear labels.
- Use consistent buttons and menus.
- Work on common screen sizes.
- Avoid unnecessarily complicated workflows.
- Provide helpful instructions for first-time users.

Future versions may include:

- Bangla language support
- Additional multilingual support
- Voice interaction
- Additional accessibility features
- Low-bandwidth support
- Mobile application support

Accessibility improvements will be prioritized based on user feedback and
the needs identified during testing.