from django.shortcuts import render
from.models import Board

def board_list(request):
    boards = Board.objects.all().order_by('-id') # id 시간역순으로 정렬 = 최신순
    return render(request, 'board_list.html', {'boards' : boards})