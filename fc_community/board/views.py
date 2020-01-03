from django.shortcuts import render

def board_list(request):
    return render(request, 'board_list.html')