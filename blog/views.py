from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Yves',
        'title': '1st post',
        'content': 'This is the first post on the blog',
        'date_posted': 'September 5, 2018'
    },
    {
        'author': 'Yves',
        'title': '1 more',
        'content': 'Another dummy post to pass content',
        'date_posted': 'September 5, 2018'
    }
]

def home(request):
    context = { 'posts': posts }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
