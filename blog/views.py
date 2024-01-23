from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(resquest):
    print('blog app 3!')
    
    context = {
        'text': 'Estamos no blog'
    }
    
    return render(
        resquest,
        'blog/index.html',
        context,
    )

def exemplo(resquest):
    print('exemplo em app 3')
    
    context = {
        'title': '-blog',
        'text': 'Estamos no exemplo',
    }
    
    return render(
        resquest,
        'blog/exemplo.html',
        context,
    )
