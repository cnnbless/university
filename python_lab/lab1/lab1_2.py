def is_valid_position(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

def is_attacking_queen(qx, qy, tx, ty):
    return qx == tx or qy == ty or abs(qx - tx) == abs(qy - ty)

def is_attacking_king(kx, ky, tx, ty):
    return abs(kx - tx) <= 1 and abs(ky - ty) <= 1

def determine_move(first_piece, positions):
    white_queen, black_king, black_queen = positions
    wq_x, wq_y = white_queen
    bk_x, bk_y = black_king
    bq_x, bq_y = black_queen
    
    if first_piece == 1:  # Білий ферзь ходить
        if is_attacking_queen(wq_x, wq_y, bq_x, bq_y):
            if is_attacking_king(bk_x, bk_y, wq_x, wq_y):
                return "здійснюється захист (після нападу Чорний король може атакувати Білого ферзя)"
            return "здійснює напад на Чорного ферзя"
        elif is_attacking_queen(wq_x, wq_y, bk_x, bk_y):
            return "здійснює напад на Чорного короля"
        else:
            return "простий хід"
    
    elif first_piece == 2:  # Чорний король ходить
        if is_attacking_king(bk_x, bk_y, wq_x, wq_y):
            return "здійснює напад на Білого ферзя"
        else:
            return "простий хід"
    
    elif first_piece == 3:  # Чорний ферзь ходить
        if is_attacking_queen(bq_x, bq_y, wq_x, wq_y):
            return "здійснює напад на Білого ферзя"
        else:
            return "простий хід"
    
    return "Невідомий хід"

def main():
    pieces = ["Білий ферзь", "Чорний король", "Чорний ферзь"]
    positions = []
    
    for i, piece in enumerate(pieces, 1):
        x, y = map(int, input(f"Введіть координати {piece} (x y): ").split())
        if not is_valid_position(x, y):
            print("Некоректні координати! Фігура поза шаховим полем.")
            return
        positions.append((x, y))
    
    print("Оберіть фігуру для першого ходу:")
    for i, piece in enumerate(pieces, 1):
        print(f"{i}. {piece}")
    
    try:
        first_piece = int(input("Введіть номер фігури: "))
        if first_piece not in range(1, 4):
            print("Некоректний вибір фігури.")
            return
    except ValueError:
        print("Будь ласка, введіть число.")
        return
    
    result = determine_move(first_piece, positions)
    print(result)
    
if __name__ == "__main__":
    main()
