def draw_board(n, position_list):
    for y in range(n):
        row = ''
        for x in range(n):
            flag = False
            for value in position_list:
                if [x, y] == value:
                    row += '[x]'
                    flag = True
            if not flag:
                row += '[ ]'
        print(row)
