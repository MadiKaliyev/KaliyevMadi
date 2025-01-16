# Задание №2
# Написать игру крестики-нолики. Output:
# ********** Игра Крестики-нолики для двух игроков **********
def doska(doska1):
    print("********** Игра Крестики-нолики для двух игроков **********")
    print("-------------")
    for row in doska1:
        print("|", end= " ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

#
def pobeditel(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '*':
            return f"Выйграл {board[i][0]}"
        if board[0][i] == board[1][i] == board[2][i] != '*':
            return f"Выйграл {board[0][i]}"

    if board[0][0] == board[1][1] == board[2][2] != '*':
        return f"Выйграл {board[0][0]}"
    if board[0][2] == board[1][1] == board[2][0] != '*':
        return f"Выйграл {board[0][2]}"

    if all(all(cell != '*' for cell in row) for row in board):
        return "Ничья"

    return None

hod = 0
board=[["*","*","*"],["*","*","*"],["*","*","*"]]
doska(board)
while True:
    hod += 1
    tekuch_user = 'X' if hod % 2 == 0 else '0'

    coords_str = input("куда ставить:  "+tekuch_user+"").split(",")
    coords = list(map(int, coords_str))
    coords = list(map(lambda x: x-1, coords))
    board[coords[0]][coords[1]] = tekuch_user
    doska(board)
    if pobeditel(board) != None:
        print(pobeditel(board))
        break


