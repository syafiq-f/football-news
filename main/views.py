from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406439715',
        'name': 'Syafiq Faqih',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
