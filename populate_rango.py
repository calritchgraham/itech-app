import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Video

def populate():

    # Dictionaries of categories, containing pages
    python_pages = [
        {
            "title": "Official Python Tutorial",
             "url":"http://docs.python.org/2/tutorial/",
             "views": 45
        },
        {
            "title": "How to Think like a Computer Scientist",
             "url":"http://www.greenteapress.com/thinkpython/",
             "views": 32
        },
        {
            "title": "Learn Python in 10 Minutes",
             "url":"http://www.korokithakis.net/tutorials/python/",
             "views": 12
        }]

    django_pages = [
        {
            "title": "Official Django Tutorial",
             "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
             "views": 14
        },
        {
            "title": "Django Rocks",
             "url":"http://www.djangorocks.com/",
             "views": 22
        },
        {
            "title": "How to Tango with Django",
             "url":"http://www.tangowithdjango.com/",
             "views": 123
        }
        ]

    other_pages = [
        {
            "title": "Bottle",
             "url":"http://bottlepy.org/docs/dev/",
             "views": 67
        },
        {
            "title": "Flask",
             "url":"http://flask.pocoo.org",
             "views": 1
        }
    ]

    python_videos = [
        {
            "title": "Learn Python - Full Course for Beginners",
             "url":"https://www.youtube.com/watch?v=rfscVS0vtbw",
             "views": 25000000
        },
        {
            "title": "Python Tutorial - Python for Beginners",
             "url":"https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=445s",
             "views": 19000000
        },
        {
            "title": "Python Tutorial for Absolute Beginners #1 - What Are Variables?",
             "url":"https://www.youtube.com/watch?v=Z1Yd7upQsXY",
             "views": 6000000
        }]

    django_videos = [
        {
            "title": "Python Django Web Framework - Full Course for Beginners",
             "url":"https://www.youtube.com/watch?v=F5mRW0jo-U4",
             "views": 2000000
        },
        {
            "title": "Django Tutorial for Beginners [2021]",
             "url":"https://www.youtube.com/watch?v=rHux0gMZ3Eg",
             "views": 124000
        },
        {
            "title": "Django For Beginners - Full Tutorial",
             "url":"https://www.youtube.com/watch?v=sm1mokevMWk",
             "views": 130000
        }
        ]

    other_videos = [
        {
            "title": "An Introduction to the Bottle Web Framework for Python",
             "url":"https://www.youtube.com/watch?v=g_9nsFJS_pk",
             "views": 37000
        },
        {
            "title": "Learn Flask for Python - Full Tutorial",
             "url":"https://www.youtube.com/watch?v=Z1RJmh_OqeA",
             "views": 775000
        }
    ]
    

    cats = {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
    }

    # Adds all the categories, then adds all the associated pages
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

        for p in cat_data["videos"]:
            add_video(c, p["title"], p["url"], p["views"])


    # Print out the categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

        for p in Video.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_video(cat, title, url, views=0):
    v = Video.objects.get_or_create(category=cat, title=title)[0]
    v.url=url
    v.views=views
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
