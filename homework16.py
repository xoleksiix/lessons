def check_win(board: list[str]) -> str:
    if (board[0][1] == board[1][1] == board[2][2]) \
            or (board[0][2] == board[1][1] == board[2][0]) \
            or (board[0][1] == board[1][1] == board[2][1]) \
            or (board[1][0] == board[1][1] == board[1][2]):
        return board[1][1]
        #комбинации через центральную клетку
    elif (board[0][0] == board[0][1] == board[0][2]) \
            or (board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]
        #через левый верхний угол, искллючая диагональ
    elif board[2][0] == board[2][1] == board[2][2] \
            or board[0][2] == board[1][2] == board[2][2]:
        return board[2][2]
        #через нижний правый угол, исключая диагональ
    else:
        return "D"
        #нет победителя


if __name__ == '__main__':

    board = ["O.X",
             "XOX",
             "XOO"]

  print(check_win(board))
