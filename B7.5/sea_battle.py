from random import randint


class MyException(Exception):
    def __init__(self, text):
        self.txt = text


class Board:
    ships = []
    hp1 = hp2 = 11
    m1 = [['О' for _ in range(7)] for _ in range(7)]
    m2 = [['О' for _ in range(7)] for _ in range(7)]
    m3 = [['О' for _ in range(7)] for _ in range(7)]
    m1[0][0] = m2[0][0] = m3[0][0] = ' '
    for i in range(1, 7):
        m1[0][i] = m2[0][i] = m3[0][i] = m1[i][0] = m2[i][0] = m3[i][0] = str(i)

    def __init__(self, *ships):
        self.ships = ships

    def render_board(self):
        for i in range(7):
            print('|'.join(self.m1[i]) + '|\t' + '|'.join(self.m3[i]))

    def append_ship(self, turn, ship):
        # проверка расположения корабля
        for x, y in ship.get_dots():
            if turn:
                if (self.m1[y][x] == '■' or
                        x - 1 > 0 and self.m1[y][x - 1] == '■' or
                        x + 1 < 7 and self.m1[y][x + 1] == '■' or
                        y - 1 > 0 and self.m1[y - 1][x] == '■' or
                        y + 1 < 7 and self.m1[y + 1][x] == '■' or
                        y - 1 > 0 and x - 1 > 0 and self.m1[y - 1][x - 1] == '■' or
                        y - 1 > 0 and x + 1 < 7 and self.m1[y - 1][x + 1] == '■' or
                        y + 1 < 7 and x - 1 > 0 and self.m1[y + 1][x - 1] == '■' or
                        y + 1 < 7 and x + 1 < 7 and self.m1[y + 1][x + 1] == '■'):
                    raise MyException('Корабли должны находится на расстоянии минимум одна клетка друг от друга!')
            else:
                if (self.m2[y][x] == 'E' or
                        x - 1 > 0 and self.m2[y][x - 1] == 'E' or
                        x + 1 < 7 and self.m2[y][x + 1] == 'E' or
                        y - 1 > 0 and self.m2[y - 1][x] == 'E' or
                        y + 1 < 7 and self.m2[y + 1][x] == 'E' or
                        y - 1 > 0 and x - 1 > 0 and self.m2[y - 1][x - 1] == 'E' or
                        y - 1 > 0 and x + 1 < 7 and self.m2[y - 1][x + 1] == 'E' or
                        y + 1 < 7 and x - 1 > 0 and self.m2[y + 1][x - 1] == 'E' or
                        y + 1 < 7 and x + 1 < 7 and self.m2[y + 1][x + 1] == 'E'):
                    raise MyException('Корабли должны находится на расстоянии минимум одна клетка друг от друга!')

        # если все ок, располагаем корабль
        for x, y in ship.get_dots():
            if turn:
                self.m1[y][x] = '■'
            else:
                self.m2[y][x] = 'E'

    def set_cell(self, turn, x, y):
        if turn:
            if self.m2[y][x] == 'T' or self.m2[y][x] == 'X':
                raise MyException('Ошибка! Нельзя стрелять дважды в одно и то же место!')
            elif self.m2[y][x] == 'E':
                self.m2[y][x] = self.m3[y][x] = 'X'
                self.hp2 -= 1
                return True
            else:
                self.m2[y][x] = self.m3[y][x] = 'T'
                return False
        else:
            if self.m1[y][x] == 'T':
                raise Exception
            elif self.m1[y][x] == '■':
                self.m1[y][x] = 'X'
                self.hp1 -= 1
                return True
            else:
                self.m1[y][x] = 'T'
                return False

    def is_end(self):
        if self.hp1 and self.hp2:
            return False
        else:
            return True


class Ship:
    dots = []

    def __init__(self, dots):
        x = dots[::2]
        y = dots[1::2]
        if not all(i == y[0] for i in y):
            raise MyException("Корабли должны располагаться горизонтально!")
        self.dots = list(zip(x, y))
        self.hp = len(dots)

    def get_dots(self):
        return self.dots


class Game:
    game_board = Board()

    @staticmethod
    def render_menu():
        print('-=-=-=-=-=-=-')
        print('«Морской бой»')
        print('1.Новая игра')
        print('2.Правила')
        print('3.Выход')
        print()

    @staticmethod
    def render_rules():
        print('«Морской бой» — игра для двух участников, в которой игроки по очереди\n'
              'называют координаты на неизвестной им карте соперника. Если у соперника\n'
              'по этим координатам имеется корабль (координаты заняты), то корабль или\n'
              'его часть «топится», а попавший получает право сделать ещё один ход.\n'
              'Цель игрока — первым потопить все корабли противника.\n')

    def render_game(self):
        print()
        self.game_board.render_board()
        print()

    def start(self):
        while True:
            try:
                Game.render_menu()
                key = int(input('Ваш выбор: '))
            except ValueError:
                print('Некорректный ввод! Введите 1, 2 или 3.\n')
                continue
            else:
                if key not in [1, 2, 3]:
                    print('Некорректный ввод! Введите 1, 2 или 3.\n')
                    continue
                elif key == 1:
                    break
                elif key == 2:
                    Game.render_rules()
                    continue
                else:
                    exit(0)
        self.play()

    def set_ships(self):
        ships = {
            1: 3,
            2: 2,
            4: 1
        }

        print('На каждой доске должно находится следующее количество кораблей:\n'
              '1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.')

        self.render_game()

        for key, value in ships.items():
            print(f'''Расположите {key} {'корабль' if key == 1 else 'корабля'}'''
                  f''' на {value} {'клетку' if value == 1 else 'клетки'}'''
                  f''' в формате ({' '.join(['x'+str(i+1)+' y'+str(i+1) for i in range(value)])}):''')

            for i in range(key):
                while True:
                    print(f'{i+1}-й корабль ({value} кл.) -> ', end='')
                    try:
                        dots = list(map(int, str(input()).split()))
                        if len(dots) != value * 2:
                            raise Exception
                        elif any(map(lambda x: x < 1 or x > 6, dots)):
                            raise MyException('Ошибка! Координаты должны быть в диапазоне од 1 до 6 включительно!')
                        ship = Ship(dots)
                    except MyException as me:
                        print(me)
                        continue
                    except:
                        print(f'''Ошибка ввода координат! Задайте координаты в формате ({' '.join(['x'+str(i+1)+' y'+str(i+1) for i in range(value)])}):''')
                        continue
                    else:
                        try:
                            self.game_board.append_ship(True, ship)
                        except MyException as me:
                            print(me)
                            continue
                        else:
                            break
                self.render_game()

    def set_enemies(self):
        ships = {
            1: 3,
            2: 2,
            4: 1
        }

        for key, value in ships.items():
            for i in range(key):
                while True:
                    try:
                        dots = []
                        rand_x = randint(1, 7 - value)
                        rand_y = randint(1, 6)
                        for j in range(value):
                            dots.append(rand_x + j)
                            dots.append(rand_y)
                        ship = Ship(dots)
                    except MyException:
                        continue
                    else:
                        try:
                            self.game_board.append_ship(False, ship)
                        except MyException:
                            continue
                        else:
                            break

    def enemy_turn(self):
        while True:
            try:
                x, y = randint(1, 6), randint(1, 6)
                is_hit = self.game_board.set_cell(False, x, y)
            except:
                continue
            else:
                print(f'Ход противника! -> ({x} {y})')
                if is_hit:
                    print('Противник попал!')
                    self.render_game()
                    continue
                else:
                    print('Противник промахнулся!')
                    break

    def play(self):
        self.set_ships()
        self.set_enemies()

        turn = randint(0, 1)
        print(f'''Игра началась! Вы ходите {'первым'.upper() if turn else 'вторым'.upper()}!''')
        if not turn:
            self.enemy_turn()

        self.render_game()
        while True:

            # ход игрока
            while True:
                try:
                    print("Ваш ход! Задайте координаты в формате (x y): ", end='')
                    shot = list(map(int, str(input()).split()))
                    x, y = shot[0], shot[1]
                    if len(shot) != 2:
                        raise MyException("Ошибка! Должно быть две координаты!")
                    elif x < 0 or x > 6 or y < 0 or y > 6:
                        raise MyException('Ошибка! Координаты должны быть в диапазоне од 1 до 6 включительно!')
                    is_hit = self.game_board.set_cell(True, x, y)
                except MyException as me:
                    print(me)
                    continue
                except:
                    print("Ошибка ввода! Попытайтесь снова!")
                    continue
                else:
                    if is_hit:
                        print('Вы попали!')
                        self.render_game()
                        continue
                    else:
                        print('Вы промахнулись!')
                        break
            self.render_game()
            if self.game_board.is_end():
                print('Конец игры! Вы победитель!'.upper())
                break

            # ход противника
            self.enemy_turn()
            self.render_game()
            if self.game_board.is_end():
                print('Конец игры! Противник победил!'.upper())
                break


game = Game()
game.start()
