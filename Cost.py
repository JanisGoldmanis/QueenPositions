def cost_of_board(xy_positions):
    cost = 0

    for index in range(len(xy_positions)):
        # flag = False

        clone_xy_positions = xy_positions[:]
        current_position = clone_xy_positions.pop(index)
        # print(current_position)
        # checking rows
        for position in clone_xy_positions:
            if position[1] == current_position[1]:
                cost += 1
                # flag = True
                # print('row',position,current_position)
        # checking columns
        for position in clone_xy_positions:
            if position[0] == current_position[0]:
                cost += 1
                # flag = True
                # print('column',position,current_position)
        # checking diagonals

        for position in clone_xy_positions:
            if abs(position[0] - current_position[0]) == abs(position[1] - current_position[1]):
                # flag = True
                cost += 1

        # if flag:
        #     cost+=1
        # print(cost)

    return cost
