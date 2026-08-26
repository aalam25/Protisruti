def get_resources(category):
    """
    Return educational and empowerment resources
    based on the selected category.
    """

    resources = {

        "🌸 Women's Education": [

            {
                "title": "Continue Your Education",
                "description": (
                    "Explore learning opportunities that can help "
                    "you continue your education and build confidence."
                ),
                "type": "Education"
            },

            {
                "title": "Digital Literacy",
                "description": (
                    "Learn basic computer skills, internet safety, "
                    "online communication, and digital tools."
                ),
                "type": "Skill"
            },

            {
                "title": "English Language Learning",
                "description": (
                    "Improve reading, writing, listening, and "
                    "communication skills through regular practice."
                ),
                "type": "Learning"
            },

            {
                "title": "Financial Literacy",
                "description": (
                    "Learn about budgeting, saving, managing money, "
                    "and making informed financial decisions."
                ),
                "type": "Life Skill"
            }
        ],


        "📚 Children's Learning": [

            {
                "title": "Reading Practice",
                "description": (
                    "Encourage children to read age-appropriate "
                    "stories and practice new vocabulary."
                ),
                "type": "Education"
            },

            {
                "title": "Mathematics Practice",
                "description": (
                    "Practice basic mathematics through simple "
                    "problems and everyday examples."
                ),
                "type": "Education"
            },

            {
                "title": "Science Learning",
                "description": (
                    "Explore science through simple explanations, "
                    "experiments, and observations."
                ),
                "type": "Education"
            },

            {
                "title": "Creative Learning",
                "description": (
                    "Encourage drawing, writing, storytelling, "
                    "and other creative activities."
                ),
                "type": "Activity"
            }
        ],


        "💼 Skills & Career": [

            {
                "title": "Computer Skills",
                "description": (
                    "Develop practical computer skills that can "
                    "support education and future employment."
                ),
                "type": "Skill"
            },

            {
                "title": "Communication Skills",
                "description": (
                    "Practice communication, presentation, and "
                    "professional interaction skills."
                ),
                "type": "Career Skill"
            },

            {
                "title": "Resume Preparation",
                "description": (
                    "Learn how to organize education, skills, "
                    "projects, and experience into a professional resume."
                ),
                "type": "Career"
            },

            {
                "title": "Interview Preparation",
                "description": (
                    "Practice common interview questions and learn "
                    "how to communicate your strengths confidently."
                ),
                "type": "Career"
            }
        ],


        "🎓 Scholarships & Opportunities": [

            {
                "title": "Scholarship Research",
                "description": (
                    "Learn how to search for scholarships and "
                    "identify opportunities that match your goals."
                ),
                "type": "Opportunity"
            },

            {
                "title": "Educational Opportunities",
                "description": (
                    "Explore programs, courses, fellowships, and "
                    "other educational opportunities."
                ),
                "type": "Education"
            },

            {
                "title": "Community Programs",
                "description": (
                    "Look for community organizations that provide "
                    "education, training, mentoring, and support."
                ),
                "type": "Community"
            },

            {
                "title": "Career Development",
                "description": (
                    "Explore internships, training programs, "
                    "volunteer opportunities, and career resources."
                ),
                "type": "Career"
            }
        ],


        "🛡️ Safety & Well-being": [

            {
                "title": "Online Safety",
                "description": (
                    "Learn how to protect passwords, personal "
                    "information, and accounts while using the internet."
                ),
                "type": "Safety"
            },

            {
                "title": "Privacy Awareness",
                "description": (
                    "Understand why personal information should be "
                    "protected when using websites and applications."
                ),
                "type": "Safety"
            },

            {
                "title": "Healthy Learning Habits",
                "description": (
                    "Develop balanced study habits with appropriate "
                    "rest, organization, and time management."
                ),
                "type": "Well-being"
            },

            {
                "title": "Ask a Trusted Adult",
                "description": (
                    "Children should talk to a trusted parent, teacher, "
                    "guardian, or another responsible adult when they "
                    "feel unsafe or need help."
                ),
                "type": "Safety"
            }
        ]
    }

    return resources.get(category, [])