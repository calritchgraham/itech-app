import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Video

def populate():

    # Dictionaries of categories, containing pages and videos
    python_pages = [
        {
            "title": "Official Python Tutorial",
             "url":"http://docs.python.org/2/tutorial/",
             "likes": 45
        },
        {
            "title": "How to Think like a Computer Scientist",
             "url":"http://www.greenteapress.com/thinkpython/",
             "likes": 32
        },
        {
            "title": "Learn Python in 10 Minutes",
             "url":"http://www.korokithakis.net/tutorials/python/",
             "likes": 12
        }]

    django_pages = [
        {
            "title": "Official Django Tutorial",
             "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
             "likes": 14
        },
        {
            "title": "Django Rocks",
             "url":"http://www.djangorocks.com/",
             "likes": 22
        },
        {
            "title": "How to Tango with Django",
             "url":"http://www.tangowithdjango.com/",
             "likes": 123
        }
        ]

    other_pages = [
        {
            "title": "Bottle",
             "url":"http://bottlepy.org/docs/dev/",
             "likes": 67
        },
        {
            "title": "Flask",
             "url":"http://flask.pocoo.org",
             "likes": 1
        }
        ]
    
    java_pages = [
        {
            "title": "The Java Tutorials",
             "url":"https://docs.oracle.com/javase/tutorial/",
             "likes": 65
        },
        {
            "title": "Learn Java Programming",
             "url":"https://www.tutorialspoint.com/java/index.htm",
             "likes": 165
        }
        ]

    javaScript_pages = [
        {
            "title": "JavaScript Tutorial",
             "url":"https://www.w3schools.com/js/",
             "likes": 30
        },
        {
            "title": "The Modern JavaScript Tutorial",
             "url":"https://javascript.info",
             "likes": 41
        }
        ]
    
    python_videos = [
        {
            "title": "Learn Python - Full Course for Beginners",
            "url":"https://www.youtube.com/watch?v=rfscVS0vtbw",
            "likes": 12
        },
        {
            "title": "Python Tutorial - Python for Beginners",
            "url":"https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=445s",
            "likes": 54
        },
        {
            "title": "Python Tutorial for Absolute Beginners #1 - What Are Variables?",
            "url":"https://www.youtube.com/watch?v=Z1Yd7upQsXY",
            "likes": 98
        }
        ]


    django_videos = [
        {
            "title": "Python Django Web Framework - Full Course for Beginners",
             "url":"https://www.youtube.com/watch?v=F5mRW0jo-U4",
             "likes": 5
        },
        {
            "title": "Django Tutorial for Beginners [2021]",
             "url":"https://www.youtube.com/watch?v=rHux0gMZ3Eg",
             "likes": 59
        },
        {
            "title": "Django For Beginners - Full Tutorial",
             "url":"https://www.youtube.com/watch?v=sm1mokevMWk",
             "likes": 32
        }
        ]

    other_videos = [
        {
            "title": "An Introduction to the Bottle Web Framework for Python",
             "url":"https://www.youtube.com/watch?v=g_9nsFJS_pk",
             "likes": 3
        },
        {
            "title": "Learn Flask for Python - Full Tutorial",
             "url":"https://www.youtube.com/watch?v=Z1RJmh_OqeA",
             "likes": 41
        }
    ]

    java_videos = [
        {
            "title": "Java Tutorial for Beginners",
             "url":"https://www.youtube.com/watch?v=eIrMbAQSU34",
             "likes": 18
        },
        {
            "title": "Java Full Course",
             "url":"https://www.youtube.com/watch?v=hBh_CC5y8-s",
             "likes": 567
        }
    ]

    javaScript_videos = [
        {
            "title": "JavaScript Tutorial for Beginners: Learn JavaScript in 1 Hour",
             "url":"https://www.youtube.com/watch?v=W6NZfCO5SIk",
             "likes": 5
        },
        {
            "title": "Learn JavaScript - Full Course for Beginners",
             "url":"https://www.youtube.com/watch?v=PkZNo7MFNFg",
             "likes": 66
        }
    ]
    
    no_pages = []
    no_videos = []

    cats = {
        "Python": {"pages": python_pages, "videos": python_videos, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "videos": django_videos, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "videos": other_videos, "views": 32, "likes": 16},
        "Java": {"pages": java_pages, "videos": java_videos, "views": 85, "likes": 112},
        "JavaScript": {"pages": javaScript_pages, "videos": javaScript_videos, "views": "99", "likes": 54},
        'Pascal': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Perl': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'PHP': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Prolog': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'PostScript': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'AJAX': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'CSS': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'HTML': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'SQL': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Angular': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'TypeScript': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Ruby': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Basic': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Assembly': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Ballerina': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Darwin': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Haxe': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Kaleidoscope': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Logtalk': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Oak': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Uniface': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        'Zeno': {'pages': no_pages, 'videos':no_videos, 'views': 0, 'likes': 0},
        }
    

    # Adds all the categories, then adds all the associated pages
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["likes"])

        for p in cat_data["videos"]:
            add_video(c, p["title"], p["url"], p["likes"])


    # Print out the categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

        for p in Video.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.likes=likes
    p.save()
    return p

def add_video(cat, title, url, likes=0):
    v = Video.objects.get_or_create(category=cat, title=title)[0]
    v.url=url
    v.likes=likes
    v.save()
    return v

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# start execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
