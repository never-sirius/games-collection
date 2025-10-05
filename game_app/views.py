from django.shortcuts import render
from .logic.tictactoe.tictactoe import check_winner 

def home(request):
    return render(request, 'games/index.html')

def tic_tac_toe(request):
    board = [[" "]*3 for _ in range(3)]
    winner = None

    return render(request, 'games/tictactoe.html', {'board': board, 'winner': winner})


