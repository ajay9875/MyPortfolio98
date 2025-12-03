from django.shortcuts import render
from decouple import config
from .models import VisitorCount

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def increase_visitor(request):
    visitor_data, created = VisitorCount.objects.get_or_create(id=1)
    visitor_data.count += 1
    visitor_data.save()
    return JsonResponse({"success": True, "count": visitor_data.count})

def portfolio(request):
    # Get visitor count (do NOT increment here)
    visitor_data, created = VisitorCount.objects.get_or_create(id=1)

    context = {
        "visitor_count": visitor_data.count,
        "ticker_items": [
            "🏆 All India NCAT Rank #39493 (Top 3%) | HackerRank Gold (Python 115/115, SQL 58/58)",
            "🤖 Developed Revolt Motors Voice Assistant (Node.js, Gemini API, Socket.IO)",
            "📄 Built Intelli Doc AI for multi-format document processing & NLU",
            "📊 Created AI-Powered Mutual Fund Recommendation System (Collaborative/Content-Based Filtering)",
            "🎓 Built Adaptive Online Course Recommendation System using AI & similarity scoring",
            "✅ Developed TaskCare360: Flask To-Do App with email reminders & OTP security",
            "🌐 Designed & Deployed MyPortfolio24*7 (Live on Render)",
            "📈 Data Analysis: Python, SQL, ETL, EDA, Pandas, NumPy, Power BI, Tableau",
            "🤖 AI/ML: NLP, LLMs, Prompt Engineering, Scikit-Learn",
            "💻 Backend: Django, Flask, REST APIs, PostgreSQL, MySQL",
            "☁️ Cloud & DevOps: AWS (S3, Lambda), CI/CD, GitHub, Render"
            ],

        'name': 'AJAY KUMAR SAH',
        'title': "",
        'about':
               '''A dedicated and results-oriented professional with a passion for innovation and continuous improvement. I am seeking a challenging role that allows me to utilize my full potential and contribute directly to the strategic goals of a forward-thinking organization. My goal is to leverage my sincerity and hard work to achieve outstanding results while embracing new challenges.''',
        'email': 'kumar.ajaysah2003@gmail.com',
        'phone': '+91-9875400827',
        'address': "https://www.google.com/maps/place/17%C2%B016'14.7%22N+78%C2%B032'16.5%22E/@17.270735,78.5353368,17z/data=!3m1!4b1!4m4!3m3!8m2!3d17.270735!4d78.5379117?hl=en&entry=ttu&g_ep=EgoyMDI1MDcxMy4wIKXMDSoASAFQAw%3D%3D",
        'birth_date': 'January 2, 2003',
        'gender': 'Male',
        'location': 'Hyderabad',
        
        'skills': [
            {'name': 'Python', 'image': 'skills/python.png'},
            {'name': 'SQL', 'image': 'skills/sql.png'},
            {'name': 'Problem Solving', 'image': 'skills/problem-solving.png'},
            {'name': 'Large Language Models', 'image': 'skills/large.png'},
            {'name': 'Prompt Engineering', 'image': 'skills/prompt.png'},
            {'name': 'Natural Language Processing', 'image': 'skills/natural.png'},
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
                'description': 'Gained hands-on experience in provisioning EC2 instances and managing IAM user permissions and root access controls in Amazon AWS.'
            },
        ],
        
        'education': [
            {
                'degree': 'B.Tech/B.E. in Computer Science',
                'institution': 'Brainware University, West Bengal',
                'year': '2021 - 2025',
                'score': '8.73 CGPA'
            },
            {
                'degree': 'Class XII',
                'institution': 'Bihar Board (Hindi Medium)',
                'year': '2018 - 2020',
                'score': '66.6%'
            },
            {
                'degree': 'Class X',
                'institution': 'Bihar Board (Hindi Medium)',
                'year': '2017 - 2018',
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