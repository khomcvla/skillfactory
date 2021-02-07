from random import randint


# Menu
# --------------------------------------------------------
def renderMenu():
    print('1. Новая игра\n2. Выход')


print(str.upper('«Крестики-нолики»'))
key = None
while key not in ['1', '2']:
    renderMenu()
    key = input('Выберите вариант: ')
if key == '2':
    exit()


# Game
# --------------------------------------------------------
def start_game():
    m = [['-' for _ in range(3)] for _ in range(3)]
    steps = 0

    def render_game():
        print(f'  0 1 2\n' \
              f'0 {m[0][0]} {m[0][1]} {m[0][2]}\n'\
              f'1 {m[1][0]} {m[1][1]} {m[1][2]}\n'\
              f'2 {m[2][0]} {m[2][1]} {m[2][2]}\n')

    def set_cell(i, j, turn):
        m[i][j] = 'o' if turn else 'x'
        nonlocal steps
        steps += 1

    def check_winner(turn):
        if (m[0][0] == m[0][1] == m[0][2] != '-' or
            m[1][0] == m[1][1] == m[1][2] != '-' or
            m[2][0] == m[2][1] == m[2][2] != '-' or
            m[0][0] == m[1][0] == m[2][0] != '-' or
            m[0][1] == m[1][1] == m[2][1] != '-' or
            m[0][2] == m[1][2] == m[2][2] != '-' or
            m[0][0] == m[1][1] == m[2][2] != '-' or
            m[0][2] == m[1][1] == m[2][0] != '-'):
            print('Вы победитель!' if turn else 'Противник победил!')
            return True
        elif steps == 9:
            print('Победила ничья!')
            return True
        else:
            return False

    # 0 - противник, 1 - игрок
    turn = randint(0, 1) % 2
    print(f'Игра началась! Вы ходите {"вторым" if turn else "первым"}!')
    if turn:
        set_cell(randint(0, 2), randint(0, 2), not turn)
    render_game()

    while True:
        while True:
            print('Ваш ход!')
            i, j = None, None
            while i not in ['0', '1', '2']:
                i = input('Введите строку: ')
            while j not in ['0', '1', '2']:
                j = input('Введите столбец: ')

            if m[int(i)][int(j)] != '-':
                print(f'Ошибка ввода! Клетка [{i}, {j}] уже заполнена!')
                render_game()
            else:
                break
        set_cell(int(i), int(j), turn)
        render_game()
        if check_winner(True):
            break

        print('Ход противника!')
        i, j = randint(0, 2), randint(0, 2)
        while m[i][j] != '-':
            i, j = randint(0, 2), randint(0, 2)
        set_cell(i, j, not turn)
        render_game()
        if check_winner(False):
            break


while True:
    start_game()
    print('Начать сначала?\n1.Да\n2.Нет')
    key = None
    while key not in ['1', '2']:
        key = input('Выберите вариант: ')
    if key == '2':
        break


