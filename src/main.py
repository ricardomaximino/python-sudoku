from typing import List
from manager import Manager
from grid_manager import GridManager
# New
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Easy
grid = [
    [0, 0, 3, 5, 0, 0, 4, 9, 0],
    [7, 6, 0, 0, 0, 0, 5, 0, 1],
    [0, 5, 4, 0, 7, 3, 6, 0, 8],
    [0, 1, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 7, 2, 6, 1, 0, 0, 0],
    [2, 0, 6, 0, 9, 0, 0, 1, 4],
    [6, 3, 2, 8, 5, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 2, 8, 0, 6],
    [8, 0, 5, 0, 0, 7, 2, 0, 0]]

# Hard
# grid = [
#     [0, 0, 0, 1, 3, 0, 0, 0, 0],
#     [0, 0, 0, 0, 9, 0, 3, 0, 0],
#     [4, 0, 0, 6, 2, 5, 1, 7, 0],
#     [0, 0, 0, 8, 7, 0, 0, 0, 0],
#     [5, 0, 9, 0, 0, 0, 0, 4, 0],
#     [0, 0, 7, 0, 0, 3, 0, 0, 9],
#     [0, 7, 0, 0, 0, 6, 0, 0, 3],
#     [0, 5, 0, 0, 4, 0, 6, 0, 0],
#     [0, 0, 4, 5, 0, 0, 7, 0, 0]]

# # Extremely Hard
grid = [
    [0, 0, 7, 0, 0, 0, 0, 3, 5],
    [0, 1, 0, 0, 4, 0, 0, 8, 0],
    [0, 0, 0, 3, 0, 0, 1, 0, 0],
    [5, 0, 0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 2, 6, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [8, 0, 0, 7, 6, 5, 0, 9, 0],
    [0, 7, 0, 1, 3, 9, 0, 0, 0]]


# Dificil
# grid = [
#     [0, 5, 3, 7, 6, 9, 0, 0, 0],
#     [0, 4, 0, 2, 8, 0, 0, 1, 6],
#     [8, 0, 0, 4, 0, 0, 9, 0, 0],
#     [9, 0, 0, 0, 4, 0, 0, 6, 0],
#     [2, 6, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 9, 0, 8, 5, 7],
#     [0, 0, 0, 0, 7, 4, 0, 3, 9],
#     [0, 0, 0, 0, 0, 8, 0, 0, 0],
#     [5, 9, 0, 3, 0, 0, 0, 2, 0]]

def solve_as_human():
    while len(grid_manager.grid_manager) != 0:
        manager_size = len(grid_manager.grid_manager)
        print("Before")
        print(f"Grid size: {manager_size}")

        for cell_key in grid_manager.grid_manager:
            print(
                f"{grid_manager.grid_manager[cell_key].position} {grid_manager.grid_manager[cell_key].possible_numbers}")
            if len(grid_manager.grid_manager[cell_key].possible_numbers) == 1:
                grid_manager.grid_manager[cell_key].try_number(grid_manager.grid_manager[cell_key].possible_numbers[0])

        print("After")
        grid_manager.print_grid()
        grid_manager.grid_manager = {}
        grid_manager.init()
        print(f"Grid size: {manager_size}")
        if len(grid_manager.grid_manager) == manager_size:
            for cell_key in grid_manager.grid_manager:
                print(f"""
                Cell: {grid_manager.grid_manager[cell_key].position}
                Possible Numbers to try: {grid_manager.grid_manager[cell_key].possible_numbers}""")
                for possible in grid_manager.grid_manager[cell_key].possible_numbers:
                    possible_once = True
                    lines = grid_manager.grid_manager[cell_key].related_cells_in_line + grid_manager.grid_manager[
                        cell_key].related_cells_in_column
                    for position in lines:
                        try:
                            if possible in grid_manager.grid_manager[position].possible_numbers:
                                print(
                                    f"The possible Number {possible} is inside of {grid_manager.grid_manager[position].position} {grid_manager.grid_manager[position].possible_numbers}")
                                possible_once = False
                                break
                        except KeyError:
                            pass
                    # print(f"The number {possible} is int the related managesr {possible_once}")
                    if possible_once:
                        grid_manager.grid_manager[cell_key].try_number(possible)

        print("After")
        grid_manager.print_grid()
        grid_manager.grid_manager = {}
        grid_manager.init()
        print(f"Grid size: {manager_size}")


def print_grid(solution):
    print("Sudoku")
    for row in range(9):
        for column in range(9):
            print(solution[row][column], end=" ")
        print()
    print()


def solve_as_machine(grid_manager):
    print_grid(grid_manager.grid)
    grid_manager.solve()




gm = GridManager(grid)

solve_as_machine(gm)


