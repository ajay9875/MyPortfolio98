from django.shortcuts import render
from decouple import config
def portfolio(request):
    context = {
        'name': 'AJAY KUMAR SAH',
        'title': 'Backend Developer | Python Specialist',
        'about':
            "I am a passionate backend developer with a strong foundation in Python. "
            "I am actively seeking roles as a Web Developer, Software Developer, or Data Analyst. "
            "My technical expertise includes Python, SQL, Git, MS Office, Data Handling, Artificial Intelligence, "
            "Object-Oriented Programming, and Data Structures. "
            "I have successfully built and contributed to several full-stack projects such as "
            "an AI-Powered Mutual Fund Recommendation System, AI-Based Course Recommender, "
            "Budget Wisely, TaskCare360, and more. "
            "I take pride in being a highly determined individual, capable of managing the complete web development lifecycle - "
            "from backend development and frontend integration to deployment and long-term maintenance. "
            "I strive to deliver scalable, secure, and user-friendly solutions.",

        'email': 'kumar.ajaysah2003@gmail.com',
        'phone': '+91-9875400827',
        'address': 'Plot number 35, AMR Township, Balapur, Nadergul, Ranga Reddy, Telangana - 501510',
        'birth_date': 'January 2, 2003',
        'gender': 'Male',
        'location': 'Hyderabad',
        
        'skills': [
            {'name': 'Python', 'image': 'skills/python.png'},
            {'name': 'SQL', 'image': 'skills/sql.png'},
            {'name': 'Problem Solving', 'image': 'skills/problem-solving.png'},
            {'name': 'Artificial Intelligence', 'image': 'skills/ai.png'},
            {'name': 'Flask', 'image': 'skills/flask.png'},
            {'name': 'Django', 'image': 'skills/django.png'},
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
            {'name': 'Bootstrap', 'image': 'skills/bootstrap.png'},

        ],

        'experience': [
            {
                'position': 'Web Development Intern',
                'company': 'Webguru Infosystem',
                'duration': 'August 2024 - October 2024',
                'description': 'Learned about creating instances and managing IAM user or root user accessibility using Amazon AWS.'
            },
        ],
        
        'education': [
            {
                'degree': 'B.Tech/B.E. in Computer Science',
                'institution': 'Brainware University, West Bengal',
                'year': '2020 - 2024',
                'score': '82.23% & 8.72'
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
            'All India NCAT 2025',
            'Codecuezf #20 Coding Challenge'
        ],
        
        'languages': [
            {'name': 'Hindi', 'proficiency': 'Native'},
            {'name': 'English', 'proficiency': 'Fluent'}
        ],
        
        'achievements': [
            'Developed multiple full-stack projects during college',
            'Built complete web applications from backend to frontend',
            'Implemented AI/ML solutions in financial and educational domains'
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