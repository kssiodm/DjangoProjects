from django.shortcuts import render
from django.http import Http404
from blog.data import posts

# Create your views here.
def blog(resquest):
    print('blog app 3!')
    
    context = {
        'title': '- blog',
        'text': 'Estamos no blog',
        
    }
    
    return render(
        resquest,
        'blog/index.html',
        context,
        {
            'title': 'blog',
            'posts': posts,
        }
    )
    
def post(resquest, post_id):

    found_post = None
    
    for post in posts:
        if post('id') == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise  Http404('post não encontrado!')
    
    return render(
        resquest,
        'blog/post.html',
        {
            'title': 'post',
            'posts': found_post,
        }
    )

def exemplo(resquest):
    print('exemplo em app 3')
    
    context = {
        'title': '-exemplo',
        'text': 'Estamos no exemplo',
    }
    
    return render(
        resquest,
        'blog/exemplo.html',
        context,
    )
