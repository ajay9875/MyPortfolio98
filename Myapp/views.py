from django.shortcuts import render
from decouple import config
def portfolio(request):
    context = {
        'ticker_items': [
            "🏆 All India NCAT (Top 3%) | B.Tech CSE (AI/ML) - 8.73 CGPA", 
            "🌟 Aspiring Data Analyst | Python, SQL, ETL, EDA & Visualization",
            "🚀 Seeking Opportunities to Drive Data-Driven Insights",
            "💻 Backend Development: Python, Django, Flask",
            "💼 Open to Roles: Data Analyst | Backend Developer",
            "📈 Projects: AI-Powered Mutual Fund Recommender (Django + Render)",
            "📈 AI-Powered Course Recommender (Flask + PythonAnywhere)",
            "📊 TaskCare360 (Flask + Render) | Budget Wisely (Finance App)",
            "🌐 MyPortfolio98 (Django + Render)",
            "🔧 Open-Source Contributor (Django & Flask REST)",
            "🔐 REST API Development | SQL & PostgreSQL Optimization"
        ],

        'name': 'AJAY KUMAR SAH',
        'title': "Aspiring Data Analyst | Proficient in Python, ETL, EDA & Data Visualization | Seeking Opportunities to Drive Data-Driven Decisions | Skilled in Backend Development (Python, Django/Flask)",
        'about':
                "I am an aspiring Data Analyst with strong expertise in Python, SQL, ETL, Exploratory Data Analysis (EDA), and Data Visualization. "
                "I am actively seeking roles as a Data Analyst or Backend Developer, where I can apply my analytical and technical skills "
                "to transform raw data into actionable insights and build data-powered applications. "
                "My technical expertise includes Python, SQL, Data Handling, Data Structures, Object-Oriented Programming, and visualization tools "
                "such as Matplotlib, Seaborn, and MS Excel, along with backend development frameworks like Django and Flask. "
                "I have successfully completed a Data Science Internship at Unified Mentor, where I worked on real-world projects including "
                "Retail Sales Data Analysis, Financial Data Visualization, and Customer Segmentation & Prediction Models. "
                "I have also built and contributed to independent projects such as an AI-Powered Mutual Fund Recommendation System, "
                "AI-Based Course Recommender, Budget Wisely, and TaskCare360, applying both data analysis and backend integration. "
                "I take pride in being a highly determined individual capable of managing the complete data and development lifecycle — "
                "from ETL workflows, exploratory analysis, and model building to backend development, deployment, and long-term maintenance. "
                "I strive to deliver scalable, insightful, and data-driven solutions that support business growth and strategic decision-making.",

        'email': 'kumar.ajaysah2003@gmail.com',
        'phone': '+91-9875400827',
        'address': "https://www.google.com/maps/place/17%C2%B016'14.7%22N+78%C2%B032'16.5%22E/@17.270735,78.5353368,17z/data=!3m1!4b1!4m4!3m3!8m2!3d17.270735!4d78.5379117?hl=en&entry=ttu&g_ep=EgoyMDI1MDcxMy4wIKXMDSoASAFQAw%3D%3D",
        'birth_date': 'January 2, 2003',
        'gender': 'Male',
        'location': 'Hyderabad',
        
        'skills': [
            {'name': 'Python Full Stack Development', 'image': 'skills/python.png'},
            {'name': 'SQL', 'image': 'skills/sql.png'},
            {'name': 'Problem Solving', 'image': 'skills/problem-solving.png'},
            {'name': 'Artificial Intelligence', 'image': 'skills/ai.png'},
            {'name': 'Django', 'image': 'skills/django.png'},
            {'name': 'Flask', 'image': 'skills/flask.png'},
            {'name': 'PostgreSQL', 'image': 'skills/postgresql.png'},
            {'name': 'Git', 'image': 'skills/git.png'},
            {'name': 'GitHub', 'image': 'skills/github.png'},
            {'name': 'AWS', 'image': 'skills/aws.png'},
            {'name': 'Object Oriented Programming', 'image': 'skills/oop.png'},
            {'name': 'Data Structure', 'image': 'skills/data-structure.png'},
            {'name': 'Pandas', 'image': 'skills/pandas.png'},
            {'name': 'Numpy', 'image': 'skills/numpy.png'},
            {'name': 'Matplotlib', 'image': 'skills/matplotlib.png'},
            {'name': 'Seaborn', 'image': 'skills/seaborn.png'},
            {'name': 'HTML', 'image': 'skills/html.png'},
            {'name': 'CSS', 'image': 'skills/css.png'},
            {'name': 'JavaScript', 'image': 'skills/javascript.png'},
            {'name': 'BootStrap', 'image': 'skills/bootstrap.png'},

        ],

        'experience': [
            {
                'position': 'Cloud Architecture using AWS',
                'company': 'Webguru Infosystem',
                'duration': 'August 2024 - October 2024',
                'description': 'Learned about creating instances and managing IAM user or root user accessibility using Amazon AWS.'
            },
        ],
        
        'education': [
            {
                'degree': 'B.Tech/B.E. in Computer Science',
                'institution': 'Brainware University, West Bengal',
                'year': '2021 - 2025',
                'score': '82.23% /  8.73 CGPA'
            },
            {
                'degree': 'Class XII',
                'institution': 'Bihar Board (Hindi Medium)',
                'year': '2020',
                'score': '66.6%'
            },
            {
                'degree': 'Class X',
                'institution': 'Bihar Board (Hindi Medium)',
                'year': '2018',
                'score': '64.2%'
            },
        ],
        
        'certifications': [
            'Python (Basic)',
            'SQL (Basic)',
            'Cloud Architecture Using AWS',
            'Problem Solving (Basic)',
            'Communication Foundations',
            'Data Science Internship',
            'Version Control With Git',
            'AWS Certified Cloud Practitioner (CLF-C02) Cert Prep: 1 Cloud Concepts',
        ],
        
        'languages': [
            {'name': 'Hindi', 'proficiency': 'Native'},
            {'name': 'English', 'proficiency': 'Fluent'}
        ],
        
        'achievements': [
            "All India NCAT 2025 Rank 39,493 (Top 3%)",
            'Implemented AI/ML solutions in financial and educational domains',
            'Codecuezt #20 Coding Challenge',
            'Developed multiple full-stack projects during college',
            'Built complete web applications from backend to frontend',
        ],

        'social_links':{
            'github': config('GITHUB_URL', default='/'),
            'linkedin': config('LINKEDIN_URL', default='#'),
            'naukri': config('NAUKRI_URL', default='#'),
            'hackerrank': config('HACKERRANK_URL', default='#'),
            'leetcode': config('LEETCODE_URL', default='#'),
            'instagram': config('INSTAGRAM_USERNAME', default=''),
            'whatsapp': config('WHATSAPP_NUMBER', default=''),
        }

    }
    return render(request, 'index.html', context)