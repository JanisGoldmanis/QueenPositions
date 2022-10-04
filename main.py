import Board
import Cost
import Positions

# positions = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1','I1','J1','K1','L1']
positions = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
xy_list = Positions.convert_to_xy(positions)

n = 8
cost_evolution = []
cost_evolution.append(Cost.cost_of_board(xy_list))

print(positions)
print(xy_list)

board = Board.draw_board(n, xy_list)

print('Cost:', Cost.cost_of_board(xy_list))


def move_piece(all_positions, piece_index, amount, size):
    temp_positions = []
    for position in all_positions:
        temp_position = []
        for value in position:
            temp_position.append(value)
        temp_positions.append(temp_position)

    # print('Temp positions -', temp_positions)
    # print('Moving queen', piece_index,amount+1,'Places')
    # print('Moving piece from:', temp_positions[piece_index])
    temp_positions[piece_index][1] = ((temp_positions[piece_index][1] + amount + 1)) % size
    # print('To:', temp_positions[piece_index])
    return temp_positions


best_result = Cost.cost_of_board(xy_list)

for number in range(300):
    # moving i queen, n - size of the board, number of queens
    index = number % n
    print('Moving queen', index)
    solutions = []
    # generate local results based on moving i queen, solutions are all possible positions vertically
    for num in range(n - 1):
        solutions.append(move_piece(xy_list[:], index, num, n))
    # checking all solutions, if any solution is better than current best solution. If solutions are equally good,
    # most bottom position is picked.
    for solution in solutions:
        # print('Cost:', Cost.cost_of_board(solution))
        # Board.draw_board(n, solution)
        if Cost.cost_of_board(solution) <= Cost.cost_of_board(xy_list):
            xy_list = solution
            Board.draw_board(n, xy_list)
            print('Cost of Board:', Cost.cost_of_board(xy_list))
            cost_evolution.append(Cost.cost_of_board(xy_list))
    # Cost for particular iteration
    # print('Final Cost:', Cost.cost_of_board(xy_list))
    if Cost.cost_of_board(xy_list) == 0:
        print('Solution Achieved in ', number, 'iterations', number * n, 'Boards checked')
        break

board = Board.draw_board(n, xy_list)
print(xy_list)
print(cost_evolution)
# print('Cost:', Cost.cost_of_board(xy_list))
