def play_game():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    num_moves = 0
    cells_selected = 0
    
    while cells_selected < 9:
        print("Current matrix:")
        for row in matrix:
            print(row)

        row_choice = int(input("Choose a row (1-3): ")) - 1
        col_choice = int(input("Choose a column (1-3): ")) - 1
        
        if matrix[row_choice][col_choice] == 'X':
            print("Error: cell already selected, choose again.")
            continue
        else:
            matrix[row_choice][col_choice] = 'X'
            num_moves += 1
            cells_selected += 1

    print("Congratulations! You have selected all cells in", num_moves, "moves.")
