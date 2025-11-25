import random
import os

os.makedirs("stats", exist_ok=True)

def check_win(board, player, size):
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True
    
    if all(board[i][i] == player for i in range(size)) or all(board[i][size-1-i] == player for i in range(size)):
        return True
    
    return False

def print_board(board, size):
    print(f"\n  {' '.join(str(i) for i in range(size))}")
    for i in range(size):
        print(f"{i} {' '.join(board[i])}")

while True:
    size = 3
    try:
        user_input = input("Введите размер игрового поля (3): ")
        if user_input == "":
            size = 3
        else:
            size = int(user_input)
            if size < 3:
                print("Минимальный размер поля - 3!")
                size = 3
    except:
        print("Ошибка! Введите число.")
        size = 3
    
    board = [['-' for _ in range(size)] for _ in range(size)]
    player = random.choice(['X', 'O'])
    
    print(f"\n ИГРА НА ПОЛЕ {size}x{size} ")
    print(f"Первым ходит: {player}")
    
    while True:
        print_board(board, size)
        
        try:
            row = int(input(f"\nИгрок {player}, введите номер строки (0-{size-1}): "))
            col = int(input(f"Игрок {player}, введите номер столбца (0-{size-1}): "))
        except:
            print("Ошибка ввода! Введите числа.")
            continue
        
        if row < 0 or row >= size or col < 0 or col >= size:
            print("Координаты вне поля!")
            continue
            
        if board[row][col] != '-':
            print("Эта клетка уже занята!")
            continue
        
        board[row][col] = player
        
        if check_win(board, player, size):
            print_board(board, size)
            print(f"\n Игрок {player} ПОБЕДИЛ!")
            
            with open("stats/results.txt", "a", encoding="utf-8") as f:
                f.write(f"Победил: {player}, Размер поля: {size}x{size}\n")
            break
        
        if all(cell != '-' for row in board for cell in row):
            print_board(board, size)
            print("\n Ничья!")
            
            with open("stats/results.txt", "a", encoding="utf-8") as f:
                f.write(f"Ничья, Размер поля: {size}x{size}\n")
            break
        
        player = 'O' if player == 'X' else 'X'
    
    replay = input("\nХотите сыграть еще раз? (да/нет): ").lower()
    if replay in ["да", "д", "yes", "y"]:
        print("\n" + "="*30)
        continue
    else:
        print("Спасибо за игру! До свидания!")
        break