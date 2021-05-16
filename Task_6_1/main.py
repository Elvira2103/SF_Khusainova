
def show_board():
    print("   | 0 | 1 | 2 ")
    for i in range(3):
        print('---------------')
        print(i, " | ", end="")
        for j in range(3):
            print(list[i][j], " ", end=" ")
        print()


def input_xy():
    while True:
        try:
            x,y = map(int,input("Выберите поле (введите номер строки и номер колонки от 0 до 2 через пробел): ").split())
        except:
            print("Введите два числа через пробел!")
            continue
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Неверные координаты!")
            continue
        if list[x][y] != "":
            print("Поле уже занято!")
            continue
        return x,y


def win():
    win_coord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))]
    for coord in win_coord:
        a = coord[0]
        b = coord[1]
        c = coord[2]
        if list[a[0]][a[1]] == list[b[0]][b[1]] == list[c[0]][c[1]]:
            winner = list[a[0]][a[1]]
            return winner
    return False


turn = 0
list = [["","",""],["","",""],["","",""]]
print("Начинаем игру крестики-нолики!")
show_board()
while True:
    turn += 1
    if turn % 2:
        print("Ходит Х:")
        x, y = input_xy()
        list[x][y] = "X"
    else:
        print("Ходит O:")
        x, y = input_xy()
        list[x][y] = "O"
    show_board()
    if win():
        print(f"Выиграл {win()}")
        break
    if turn == 9:
        print("Это ничья!")
        break
