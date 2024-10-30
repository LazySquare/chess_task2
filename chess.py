LETTERS = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
NUMS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
WHITE_FIGURES = {'R', 'N', 'B', 'Q', 'K', 'P'}
BLACK_FIGURES = {'r', 'n', 'b', 'q', 'k', 'p'}
AREA = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]


def sign(param):
    if param < 0:
        return -1
    if param > 0:
        return 1
    return 0


def draw(area):
    print()
    print('   A B C D E F G H   ')
    print()
    for i in range(8):
        print(8 - i, '', *area[i], '', 8 - i)
    print()
    print('   A B C D E F G H   ')
    print()


def is_figure(let, num):
    return AREA[num][let] != '.'


def is_empty(let, num):
    return AREA[num][let] == '.'


def color(let, num):
    figure = AREA[num][let]
    if figure.islower():
        return 'black'
    return 'white'


def is_enemy(start_let, start_num, fin_let, fin_num):
    return color(start_let, start_num) != color(fin_let, fin_num) and is_figure(fin_let, fin_num)


def cell_to_tuple(cell):
    return LETTERS[cell[0]], 7 - NUMS[cell[1]]


def coord_to_cell(let, num):
    return chr(97 + let) + str(8 - num)


def get_in_place(start_num, start_let, finish_num, finish_let):
    figure = AREA[start_num][start_let]
    if is_empty(finish_let, finish_num):
        AREA[finish_num][finish_let] = figure
        AREA[start_num][start_let] = '.'
        return True
    if is_enemy(start_let, start_num, finish_let, finish_num):
        AREA[finish_num][finish_let] = figure
        AREA[start_num][start_let] = '.'
        return True
    return impossible_move()


def possible_moves_pawn(let, num):
    ways = []
    if color(let, num) == 'black':
        div1, div2, start_row = 1, 2, 1
    else:
        div1, div2, start_row = -1, -2, 6
    if is_empty(let, num + div1):
        ways += [coord_to_cell(let, num + div1)]
        if num == start_row and is_empty(let, num + div2):
            ways += [coord_to_cell(let, num + div2)]
    if let > 0 and is_enemy(let, num, let - 1, num + div1):
        ways += [coord_to_cell(let - 1, num + div1)]
    if let < 7 and is_enemy(let, num, let + 1, num + div1):
        ways += [coord_to_cell(let + 1, num + div1)]
    return sorted(ways)


def possible_moves_king(let, num):
    ways = []
    for x in -1, 0, 1:
        for y in -1, 0, 1:
            if 0 <= let + x <= 7 and 0 <= num + y <= 7:
                if is_empty(let + x, num + y) or is_enemy(let, num, let + x, num + y):
                    ways += [coord_to_cell(let + x, num + y)]
    return sorted(ways)


def possible_moves_rook(let, num):
    ways = []
    for x in range(let + 1, 8):
        if is_figure(x, num):
            if is_enemy(let, num, x, num):
                ways += [coord_to_cell(x, num)]
            break
        ways += [coord_to_cell(x, num)]
    for x in range(let - 1, -1, -1):
        if is_figure(x, num):
            if is_enemy(let, num, x, num):
                ways += [coord_to_cell(x, num)]
            break
        ways += [coord_to_cell(x, num)]
    for y in range(num + 1, 8):
        if is_figure(let, y):
            if is_enemy(let, num, let, y):
                ways += [coord_to_cell(let, y)]
            break
        ways += [coord_to_cell(let, y)]
    for y in range(num - 1, -1, -1):
        if is_figure(let, y):
            if is_enemy(let, num, let, y):
                ways += [coord_to_cell(let, y)]
            break
        ways += [coord_to_cell(let, y)]
    return sorted(ways)


def possible_moves_bishop(let, num):
    ways = []
    directions = (-1, 1)
    for i in range(4):
        for x in range(1, 8):
            y = directions[i // 2] * x
            x = directions[i % 2] * x
            if 0 <= let + x <= 7 and 0 <= num + y <= 7:
                if is_figure(let + x, num + y):
                    if is_enemy(let, num, let + x, num + y):
                        ways += [coord_to_cell(let + x, num + y)]
                    break
                ways += [coord_to_cell(let + x, num + y)]
    return sorted(ways)


def possible_moves_queen(let, num):
    ways1 = possible_moves_bishop(let, num)
    ways2 = possible_moves_rook(let, num)
    return sorted(ways1 + ways2)


def possible_moves_knight(let, num):
    ways = []
    direction = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
    for x, y in direction:
        if 0 <= let + x <= 7 and 0 <= num + y <= 7:
            if is_empty(let + x, num + y) or is_enemy(let, num, let + x, num + y):
                ways += [coord_to_cell(let + x, num + y)]
    return sorted(ways)


def possible_moves_for_everyone(start_let, start_num):
    figure = AREA[start_num][start_let]
    possible_ways = []
    if figure == 'P' or figure == 'p':
        possible_ways = possible_moves_pawn(start_let, start_num)
    if figure == 'R' or figure == 'r':
        possible_ways = possible_moves_rook(start_let, start_num)
    if figure == 'K' or figure == 'k':
        possible_ways = possible_moves_king(start_let, start_num)
    if figure == 'B' or figure == 'b':
        possible_ways = possible_moves_bishop(start_let, start_num)
    if figure == 'Q' or figure == 'q':
        possible_ways = possible_moves_queen(start_let, start_num)
    if figure == 'N' or figure == 'n':
        possible_ways = possible_moves_knight(start_let, start_num)
    return possible_ways


def possible_moves(command, colour):
    let, num = cell_to_tuple(command)
    if color(let, num) != colour:
        return []
    return [x for x in possible_moves_for_everyone(let, num)]


def figures_under_attack(command, colour):
    let, num = cell_to_tuple(command)
    if color(let, num) != colour:
        return []
    return [x for x in possible_moves_for_everyone(let, num) if is_enemy(let, num, *cell_to_tuple(x))]


def is_command(command, colour):
    if command[0] in LETTERS and command[1] in NUMS:
        if len(command) == 2:
            array = figures_under_attack(command, colour)
            print('enemy figures under attack: ', end='')
            if len(array):
                print(*array, sep=', ')
            else:
                print('none')
            return False
        elif len(command) == 3 and command[2] == '-':
            array = possible_moves(command, colour)
            print('possible moves: ', end='')
            if len(array):
                print(*array, sep=', ')
            else:
                print('none')
            return False
    if len(command) != 5 or command[0] not in LETTERS or command[1] not in NUMS or command[2] != '-' or command[
        3] not in LETTERS or command[4] not in NUMS:
        print('Error. Type: Wrong input format.')
        return False
    return True


def impossible_move():
    print('Error. Type: The piece cannot make the specified move.')
    return False


def moves(command, colour):
    start, finish = command.split('-')
    start_let, start_num = cell_to_tuple(start)
    finish_let, finish_num = cell_to_tuple(finish)
    if colour != color(start_let, start_num):
        return impossible_move()
    if is_empty(start_let, start_num):
        return impossible_move()
    if not is_empty(finish_let, finish_num):
        if not is_enemy(start_let, start_num, finish_let, finish_num):
            return impossible_move()
    possible_ways = possible_moves_for_everyone(start_let, start_num)
    if coord_to_cell(finish_let, finish_num) in possible_ways:
        return get_in_place(start_num, start_let, finish_num, finish_let)
    return impossible_move()


def game():
    count_moves = 2
    while True:
        colour = 'white' if count_moves % 2 == 0 else 'black'
        print(colour, ' ', count_moves // 2, ':', sep='')
        command = input()
        if command == 'exit':
            break
        elif command == 'draw':
            draw(AREA)
        else:
            if is_command(command, colour):
                if moves(command, colour):
                    count_moves += 1


if __name__ == '__main__':
    game()
