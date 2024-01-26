from django.shortcuts import render

# Create your views here.
def games(resquest):
    print('games em app 3')
    
    context = {
        'title': '-games',
        'text': 'Estamos no games',
    }
    
    return render(
        resquest,
        'games/index.html',
        context,
    )
