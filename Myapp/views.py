from django.shortcuts import render
from decouple import config
from .models import VisitorCount
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def format_count(n):
    if n < 1000:
        return str(n)
    units = [
        (1_000_000_000_000, 'T'),
        (1_000_000_000, 'B'),
        (1_000_000, 'M'),
        (1_000, 'K'),
    ]
    for divisor, suffix in units:
        if n >= divisor:
            value = n / divisor
            if value < 10:
                rounded = round(value, 1)
                return f"{rounded:g}{suffix}"
            else:
                return f"{int(round(value))}{suffix}"
    return str(n)

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
        "visitor_count": format_count(visitor_data.count),
        "ticker_items": [
            "🏆 Certified Python Programming Associate | 100+ HackerRank challenges solved",
            "🚗 Building RideBasket: Kotlin + Jetpack Compose Android apps with a Django REST backend",
            "🎨 WordPress Engineering: CPTs, Elementor, WooCommerce, ShopLentor & Orderable",
            "📄 Built AI-Powered Document Analyzer using FAISS embeddings & Groq LLM",
            "📊 Built AI-Powered Mutual Fund Recommender using TF-IDF & cosine similarity",
            "✅ Built TaskCare360: React Native & Flask app with offline step sync & push notifications",
            "🌐 Portfolio deployed on PythonAnywhere (Django + Bootstrap + AOS)",
            "📈 Data & AI: Pandas, NumPy, Scikit-Learn, TensorFlow",
            "💻 Backend: Django, Flask, REST APIs, JWT, PostgreSQL, MySQL, MongoDB",
            "🎨 Frontend: React.js, React Native, HTML, CSS",
            "☁️ Tools: Git/GitHub, VS Code, Android Studio, Postman",
        ],

        'name': 'AJAY KUMAR SAH',
        'title': "",
        'about':
               '''Software Engineer building production-grade ride-booking and logistics platforms with Kotlin, React.js, Python, and Django. Developing RideBasket across Customer and Driver Android apps and a React.js Admin Dashboard, backed by unified Django REST APIs—delivering end-to-end features across booking, real-time tracking, payments, KYC, and operations.''',
        'email': 'kumar.ajaysah2003@gmail.com',
        'phone': '+91-9875400827',
        'address': "https://www.google.com/maps/place/17%C2%B016'14.7%22N+78%C2%B032'16.5%22E/@17.270735,78.5353368,17z/data=!3m1!4b1!4m4!3m3!8m2!3d17.270735!4d78.5379117?hl=en&entry=ttu&g_ep=EgoyMDI1MDcxMy4wIKXMDSoASAFQAw%3D%3D",
        'birth_date': 'January 2, 2003',
        'gender': 'Male',
        'location': 'Hyderabad',
        
        # ===== SKILLS (Grouped by Category) =====
        'skill_categories': [
            {
                'name': 'Languages',
                'skills': [
                    {'name': 'Python', 'image': 'python.png'},
                    {'name': 'Kotlin', 'image': 'kotlin.png'},
                    {'name': 'SQL', 'image': 'sql.png'},
                    {'name': 'JavaScript', 'image': 'javascript.png'},
                ]
            },
            {
                'name': 'Backend',
                'skills': [
                    {'name': 'Django', 'image': 'django.png'},
                    {'name': 'Flask', 'image': 'flask.png'},
                    {'name': 'RESTful APIs', 'image': 'restful-apis.png'},
                    {'name': 'JWT', 'image': 'jwt.png'},
                ]
            },
            {
                'name': 'Frontend',
                'skills': [
                    {'name': 'React.js', 'image': 'react.png'},
                    {'name': 'React Native', 'image': 'react-native.png'},
                    {'name': 'HTML and CSS', 'image': 'html.png'},
                ]
            },
            {
                'name': 'Tools',
                'skills': [
                    {'name': 'Git/GitHub', 'image': 'git.png'},
                    {'name': 'VS Code', 'image': 'vs-code.png'},
                    {'name': 'Android Studio', 'image': 'android-studio.png'},
                    {'name': 'Postman', 'image': 'postman.png'},
                ]
            },
            {
                'name': 'AI & ML Libraries',
                'skills': [
                    {'name': 'Pandas', 'image': 'pandas.png'},
                    {'name': 'NumPy', 'image': 'numpy.png'},
                    {'name': 'Scikit-Learn', 'image': 'scikit-learn.png'},
                    {'name': 'TensorFlow', 'image': 'tensorflow.png'},
                ]
            },
            {
                'name': 'Databases',
                'skills': [
                    {'name': 'PostgreSQL', 'image': 'postgresql.png'},
                    {'name': 'MySQL', 'image': 'mysql.png'},
                    {'name': 'MongoDB', 'image': 'mongodb.png'},
                ]
            },
        ],

        # ===== WORK EXPERIENCE + INTERNSHIP (Updated to match resume) =====
        'experience': [
            {
                'position': 'Software Engineer',
                'company': 'Rivalkart Logistics Pvt Ltd',
                'duration': 'August 2026 - Present',
                'live': 'https://ridebasket.in/',
                'achievements': [
                    'Developing <strong>RideBasket</strong>, a ride-booking and logistics platform across <strong>Customer Android</strong>, <strong>Driver Android</strong>, and a <strong>React.js Admin Dashboard</strong>.',
                    'Building a centralised <strong>Django REST backend</strong> for auth, ride booking, map-based pickup/drop selection, tracking, trip history, wallet, SOS, OTP-verified ride start, document uploads, and driver payouts.',
                    'Delivering admin workflows for <strong>live-ride monitoring</strong>, customer/driver management, <strong>KYC verification</strong>, payments, dynamic pricing, and reporting.',
                    'Unifying end-to-end ride operations using <strong>Kotlin</strong>, <strong>Jetpack Compose</strong>, and <strong>React.js</strong>.',
                ]
            },
            {
                'position': 'Software Developer Trainee',
                'company': 'White Soft Info',
                'duration': 'Mar 2026 - Jul 2026',
                'live': 'https://wp-websites.free.nf/',
                'achievements': [
                    'Engineered responsive <strong>WordPress</strong> solutions using <strong>CPTs</strong>, <strong>Elementor</strong>, <strong>WooCommerce</strong>, <strong>ShopLentor</strong>, and <strong>Orderable</strong>.',
                    'Automated backend booking workflows via custom post types and secure shortcodes, reducing manual data entry by <strong>80%</strong>.',
                    'Built responsive digital architecture with custom theme templates, achieving <strong>100%</strong> mobile compatibility.',
                    'Optimised custom checkout modules and Orderable integrations, boosting ordering efficiency by <strong>65%</strong>.',
                    'Developed single-page web structures with custom footers and interactive features, unifying multi-site brand ecosystems.',
                ]
            },
        ],

        # ===== EDUCATION (Unchanged) =====
        'education': [
            {
                'degree': 'B.Tech/B.E. in Computer Science',
                'institution': 'Brainware University, West Bengal',
                'year': '2021 - 2025',
                'score': '8.73 CGPA / 82.23 %'
            },
            {
                'degree': 'Class XII',
                'institution': 'Bihar School Examination Board, Patna',
                'year': '2018 - 2020',
                'score': '66.6%'
            },
            {
                'degree': 'Class X',
                'institution': 'Bihar School Examination Board, Patna',
                'year': '2017 - 2018',
                'score': '64.2%'
            },
        ],
        
        # ===== CERTIFICATIONS (Unchanged) =====
        'certifications': [
            'Python',
            'Cloud Architecture Using AWS',
            'Problem Solving',
            'Data Science Internship',
            'AWS Certified Cloud Practitioner (CLF-C02) Cert Prep: 1 Cloud Concepts',
        ],
        
        # ===== LANGUAGES (Unchanged) =====
        'languages': [
            {'name': 'English', 'proficiency': 'Fluent'},
            {'name': 'Hindi', 'proficiency': 'Native'},
            {'name': 'Bengali', 'proficiency': 'Intermediate'},
        ],
        
        # ===== ACHIEVEMENTS (Unchanged) =====
        'achievements': [
            "All India NCAT 2025 Rank 39,493 (Top 3%)",
            'Implemented AI/ML solutions in financial and educational domains',
            'Codecuezt #20 Coding Challenge',
            'Developed multiple full-stack projects during college',
            'Built complete web applications from backend to frontend',
        ],

        # ===== SOCIAL LINKS (Unchanged) =====
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