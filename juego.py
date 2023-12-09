from IPython.display import clear_output
import random

test_board = [' ','X','O','X','O','X','O','X','O']
turno=''
def display_board(board):
    
    print(board[6]+" | "+board[7]+" | "+board[8])
    print("--|---|--")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("--|---|--")
    print(board[0]+" | "+board[1]+" | "+board[2])

def player_input():
    choose=input("Qué ficha quieres elegir? [O / X]: ")
    while (choose != "O") and (choose != "X"):
        choose=input("Qué ficha quieres elegir? [O / X]: ")
    return choose

def place_marker(board, marker, position):
    
    board[position]=marker

def win_check(board, mark):
    
  # Comprobación de filas
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] is mark:
            return True

    # Comprobación de columnas
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] is mark:
            return True

    # Comprobación de diagonales
    if board[0] == board[4] == board[8] and board[0] is mark:
        return True
    if board[2] == board[4] == board[6] and board[2] is mark:
        return True

    return False

def choose_first():
    turno=random.choice(['X','O'])
    if(turno=='X'):
        print("Empieza el jugador X")
    else:
        print("Empieza el jugador O")
    return turno

def space_check(board, position):
    if (len(board)<position):
        return False
    return board[position]==' '

def full_board_check(board):
    return ' ' not in board
   
 
def player_choice(board):
    pos=(input("Introduce la posición: "))
 
    while (True):
        if(pos.isdigit()==False):
            print("Introduzca un número")
        elif(int(pos)>8 and int(pos)<0 or len(board)<int(pos)):
             print("La posición no es válida")
        elif(space_check(board,int(pos)-1)==False):
             print("La posición está ocupada")
        else:
            return int(pos)-1
        pos=(input("Introduce la posición: "))


def replay():
    response=(input("¿Quieres jugar otra vez? [S/N]"))
    while(response.upper()!="S" and response.upper()!="N"):
        response=(input("¿Quieres jugar otra vez? [S/N]"))

    return response

print('Welcome to Tic Tac Toe!')

while True:

    board = [' '] * 9
    game_on = True
    marca= player_input()
    turno =choose_first()
    while game_on:
        # Player 1 Turn
        print("Turno del jugador {}".format(turno))
        display_board(board)
        position = player_choice(board)
        place_marker(board, marca, position)
        if win_check(board, marca):
            display_board(board)
            print('Ha ganado el jugador {}!'.format(turno))
            game_on = False
        elif full_board_check(board):
            display_board(board)
            print('Empate!')
            game_on = False
        if(marca=="X"):
            marca="O"
            turno="O"
        else:
            marca="X"
            turno="X"
    if not replay():
        break