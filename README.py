def display(board):
    txt = ""
    for row in board:
        for col in row:
            txt += col + " "
        txt += "\n"
    print(txt)

def get_user_input(turn):
    label = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    print("Please input a number:")
    display(label)
    selected_cell = input(turn + " select: ")
    pos = convert_input_to_cell_position(selected_cell)
    return pos

def convert_input_to_cell_position(numStr):
    mapping = {
        "1": [0, 0], "2": [0, 1], "3": [0, 2],
        "4": [1, 0], "5": [1, 1], "6": [1, 2],
        "7": [2, 0], "8": [2, 1], "9": [2, 2]
    }
    return mapping.get(numStr, None)

def play(turn, state):
    cell = get_user_input(turn)
    if is_cell_occupied(cell, state):
        return None
    y, x = cell
    state[y][x] = turn
    next_turn = "X" if turn == "O" else "O"
    return [state, next_turn]

def is_cell_occupied(cell_pos, state):
    y, x = cell_pos
    return state[y][x] != '-'

def check(state, turn):
    # Check rows, columns, and diagonals for a win
    # turn is O and 
        #  column -> ???
        #  row,
        #  dia 3 connected
    '''
    1 2 3
    4 5 6 = column -> 1,4,7 or 2,5,8 or 3,6,9
    7 8 9
    '''
    # view: split editor
    # if turn == "O" and
    
    # check column
    for i in range(3):
        first =  state[0][i]
        second = state[1][i]
        thrid =  state[2][i]
        
        if first == second and first == thrid and second == thrid and first == turn:
            return True
    # check row
    for i in range(3):
        first =  state[i][0]
        second = state[i][1]
        thrid =  state[i][2]

        if first == second and first == thrid and second == thrid and first == turn:
            return True
    # check diagonal
    # X - -
    # O correct -
    # O - -
    first = state[0][0]==turn  #what that logic? X == O
    second = state[1][1]==turn # correct == O 
    thrid = state[2][2]==turn  # - == O 
    if first == second == thrid == True: 
        return True

    # - - X
    # - X -
    # X - -
    # code here
    # first = true or false
    if state[0][2] == turn and state[1][1] == turn and state[2][0] == turn:
        return True

    return False

def need_continue() -> bool: 
    while True:
        yes_and_no=input('what to retry?(yes/no)')

        if yes_and_no == 'no':
            return False
        elif yes_and_no == 'yes':
            return True

    

def run():
    state = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    turn = 'O'
    while True:
        display(state)
        output = play(turn, state)
        if output is None:
            print("\n!!! CANNOT place on that cell, it's already occupied !!!\n")
            continue
        state = output[0]
        turn = output[1]
        
        if check(state, "X"):
            display(state)
            print("X wins!")
            if not need_continue():
                break
            output = reset_state()
            state = output[0]
            turn = 'O'
        elif check(state, "O"):
            display(state)
            print("O wins!")
            if not need_continue():
                break
            output = reset_state()
            state = output[0]
            turn = 'O'
        elif all(cell != '-' for row in state for cell in row):
            display(state)
            print("It's a draw! you 2 are suck >:(.please try again")
            if not need_continue():
                return False
            output = reset_state()
            state = output[0]
            turn = 'O'

def reset_state():
    state = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    turn = 'O'
    return state, turn

def test_check_win():
    case1 = [["O", "-", "-"], ["O", "correct", "-"], ["O", "-", "-"]]
    case2 = [["X", "-", "-"], ["O", "correct", "-"], ["O", "-", "-"]]
    case3 = [["X", "-", "-"], ["X", "correct", "-"], ["X", "-", "-"]]
    case4 = [["X", "-", "-"], ["X", "correct", "-"], ["O", "-", "-"]]
    case5 = [["X", "-", "-"], ["X", "correct", "-"], ["X", "-", "-"]]
    case6 = [["-", "O", "-"], ["-", "O", "-"], ["-", "O", "-"]]
    case7 = [["-", "X", "-"], ["-", "X", "-"], ["-", "X", "-"]]
    case8 = [["-", "-", "O"], ["-", "-", "O"], ["-", "-", "O"]]
    case9 = [["-", "-", "-"], ["O", "O", "O"], ["-", "-", "O"]]
    case10 = [["O", "-", "-"], ["O", "O", "O"], ["-", "-", "O"]]
    case11 = [["-", "-", "O"], ["O", "O", "O"], ["O", "-", "-"]]
    case12 = [["-", "-", "X"], ["-", "X", "-"], ["X", "-", "-"]]
    case13 = [["-", "-", "O"], ["-", "O", "-"], ["O", "-", "-"]]
    assert check(case1, 'O') == True
    assert check(case2, 'O') == False
    assert check(case3, 'X') == True
    assert check(case4, 'X') == False
    assert check(case5, 'X') == True
    assert check(case6, 'O') == True
    assert check(case7, 'X') == True
    assert check(case8, 'O') == True
    assert check(case9, 'O') == True
    assert check(case10, 'O') == True
    assert check(case11, 'O') == True
    assert check(case12, 'X') == True
    assert check(case13, 'O') == True

    # print(res)
    # assert res == True
    print('passed')

run()
