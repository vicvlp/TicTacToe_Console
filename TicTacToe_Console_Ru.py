"""
Консольная игра "Крестики-нолики"

Простая реализация классической игры "Крестики-нолики" для двух игроков на Python.

Особенности
*   Интуитивный интерфейс: Игровое поле отображается в консоли в формате шахматной доски (столбцы a-c, строки 1-3).
*   Ввод имен: Игроки в начале вводят свои имена.
*   Проверка победы и ничьей: Программа автоматически определяет конец игры.
*   Гибкость: Во время игры доступны специальные команды:
    *   'stop' - немедленно завершить игру.
    *   'next' - начать новую партию с теми же игроками (текущая игра не доигрывается).
    *   'new' - начать новую партию с вводом новых имен игроков.
*   Реванш: После окончания каждой партии предлагается сыграть еще раз без перезапуска программы.

Как играть

1.  Запустите скрипт 'TicTacToe_Console_Ru.py'.
2.  Введите имена игроков.
3.  Игроки по очереди вводят координаты ячейки (например, 'a1', 'b2', 'c3'), куда хотят поставить свой символ ('X' или 'O').
4.  Игра продолжается до победы одного из игроков или ничьей.

Команды во время игры:
- Ход: Введите координаты ячейки (a1, b2, c3, и т.д.)
- 'stop': Полностью завершает игровую сессию
- 'next': Немедленно начинает новую игру с теми же игроками (текущая игра не доигрывается)
- 'new': Начинает новую игру с запросом новых имен игроков

Требования:
*   Python 3.x

Запуск:
    python TicTacToe_Console_Ru.py

Author: Viktor Pichugin
Emaile: vicvlp@mail.ru | vicgm4ay@gmail.ru
Date: 2025.10.20
Version: 1.0
"""

def start_init_game():  # Начальный инит
    # Инициализирует игру, запрашивает имена игроков и возвращает их
    print("Добро пожаловать в игру Крестики-нолики!")
    player1 = input("Игрок 1, введите своё имя: ").strip()
    player2 = input("Игрок 2, введите своё имя: ").strip()
    return player1, player2

def create_board():  # Создание поля игры
    # Создает и возвращает пустое игровое поле 3x3 в шахматном формате
    return {
        'a1': '-', 'b1': '-', 'c1': '-',
        'a2': '-', 'b2': '-', 'c2': '-',
        'a3': '-', 'b3': '-', 'c3': '-'
    }

def print_board(board):  # Отрисовка поля игры
    # Выводит текущее состояние игрового поля в консоли в шахматном формате
    print("\n   a b c")  # Заголовок с буквами столбцов
    print(f"1  {board['a1']} {board['b1']} {board['c1']}")  # Ряд 1
    print(f"2  {board['a2']} {board['b2']} {board['c2']}")  # Ряд 2
    print(f"3  {board['a3']} {board['b3']} {board['c3']}\n")  # Ряд 3

def get_available_moves(board):  # Доступные ячейки для хода
    # Возвращает список доступных для хода ячеек. Фильтр по содержимому
    return [key for key, value in board.items() if value == '-']

def make_move(board, move, symbol):  # Ход
    # Обновляет поле и возвращает новое состояние после хода
    board[move] = symbol
    return board

def check_win(board, symbol):  # Проверка на выигрыш
    # Проверяет, есть ли выигрышная комбинация для указанного символа X или O
    # Все возможные выигрышные линии в шахматном формате
    lines = [
        # Горизонтальные линии (ряды)
        ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
        # Вертикальные линии (столбцы)
        ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
        # Диагонали
        ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
    ]
    for line in lines:
        if all(board[cell] == symbol for cell in line):
            return True
    return False

def check_draw(board):  # Проверка на ничью
    # Проверяет, наступила ли ничья (все ячейки заполнены)
    return '-' not in board.values()

def game_loop(player1, player2):  # Основной игровой цикл
    board = create_board()  # Создание игрового поля с начальными значениями
    current_player = (player1, 'X')  # Первый игрок начинает с X
    game_active = True  # Текущий статус игры (True - on, False - off)

    while game_active:
        print_board(board)  # Очередная отрисовка игрового поля
        cur_player_name, sym = current_player  # Имя текущего игрока и символ которым он ходит ('X', 'O')
        available_moves = get_available_moves(board)  # Ячейки доступные для входа

        print('Подсказка \nВозможные команды:')
        print('"stop" - закончить игру')
        print('"next" - играть заново')
        print('"new" - новая игра с новыми игроками\n')
        print(f'Свободные ячейки для хода: {available_moves}\n')
        move = input(f'{cur_player_name}, введите ячейку для {sym}: ').strip().lower()

        if move == 'stop':  # Завершаем игру досрочно
            print('\nИгра остановлена')
            return  
          
        if move == 'next':  # Запускаем новую игру с теми же игроками
            print('\nНовая игра с теми же игроками')
            print(f"Текущие игроки: 1. {player1};  2. {player2}\n")
            board = create_board()  # Создание игрового поля с начальными значениями
            current_player = (player1, 'X')  # Первый игрок начинает с X
            game_active = True  # Текущий статус игры (True - on, False - off)
            continue
          
        if move == 'new':  # Запускаем новую игру с новыми игроками
            print('\nНовая игра с новыми игроками')
            player1, player2 = start_init_game()
            board = create_board()  # Создание игрового поля с начальными значениями
            current_player = (player1, 'X')  # Первый игрок начинает с X
            continue

        if move not in available_moves:  # Если такой ход нельзя сделать - ячейка занята или не существует
            print('\nОшибка! Некорректный ход. Попробуйте снова')
            continue

        # Выполняем ход
        board = make_move(board, move, sym)

        # Проверяем победу
        if check_win(board, sym):
            print_board(board)  # Финальная отрисовка поля
            print(f'{cur_player_name} выиграл. Поздравляю!\n')
            game_active = False
        # Проверяем ничью
        elif check_draw(board):
            print_board(board)  # Финальная отрисовка поля
            print('Игра завершилась ничьей\n')
            game_active = False
        else:
            # Передаем ход другому игроку
            current_player = (player2, 'O') if current_player[0] == player1 else (player1, 'X')

        # Предложение сыграть снова
        if game_active == False:
          replay = input('Хотите сыграть ещё раз? (Y - да; любое другое - нет): ').strip().upper()
    
          if replay == 'Y':  # Запускаем новую игру с теми же игроками
              print('\nНовая игра с теми же игроками')
              print(f"Текущие игроки: 1. {player1};  2. {player2}\n")
              board = create_board()  # Создание игрового поля с начальными значениями
              current_player = (player1, 'X')  # Первый игрок начинает с X
              game_active = True  # Текущий статус игры (True - on, False - off)
              continue
            
          else:
              print('\nИгра завершена')
              print('Спасибо за игру!')
              break

# Запуск программы
if __name__ == "__main__":
    players = start_init_game()
    game_loop(*players)