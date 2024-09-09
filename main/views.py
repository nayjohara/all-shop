from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'All Shop',
        'name': 'Najya Johara Robby',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)