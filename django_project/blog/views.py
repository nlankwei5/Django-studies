from django.shortcuts import render

posts =[
    {
        'author': 'Lankwei',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': '15th April, 2025'
    },
     {
        'author': 'Mami',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'date_posted': '15th April, 2025'
    }
]


def home(request):
    context = {
          'posts': posts
    }
    return render(request, 'blog/home.html', context) 


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 