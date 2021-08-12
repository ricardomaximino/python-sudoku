from manager import Manager


def column_related_list(row_number, column_number):
    column_list = []
    for x in range(9):
        if x != row_number:
            column_list.append((x, column_number))
    return column_list


def box_related_list(row_number, column_number):
    box_list = []
    position = (row_number, column_number)
    sub_box_line = row_number

    if sub_box_line % 3 != 0:
        sub_box_line = sub_box_line - (sub_box_line % 3)
    for sub_box_line in range(sub_box_line, sub_box_line + 3):

        sub_box_column = column_number
        if sub_box_column % 3 != 0:
            sub_box_column = sub_box_column - (sub_box_column % 3)

        for sub_box_column in range(sub_box_column, sub_box_column + 3):
            sub_box_position = (sub_box_line, sub_box_column)
            if position != sub_box_position:
                box_list.append(sub_box_position)
    return box_list


def row_related_list(row_number, column_number):
    row_list = []

    for y in range(9):
        if y != column_number:
            row_list.append((row_number, y))
    return row_list


class GridManager:
    grid_manager = {}
    grid_solution = []
    count = 0

    def __init__(self, grid):
        self.grid = grid
        self.init()

    def init(self):
        self.generate_manager_grid()
        self.find_possible_numbers()

    def generate_manager_grid(self):
        for row in range(9):
            for column in range(9):
                if self.grid[row][column] == 0:
                    position = (row, column)
                    manager = Manager(position, self.grid, self.grid_manager)
                    manager.related_cells_in_line = row_related_list(row, column)
                    manager.related_cells_in_column = column_related_list(row, column)
                    manager.related_cells_sub_box = box_related_list(row, column)
                    manager.related_cells_managers = manager.related_cells_in_line + manager.related_cells_in_column + manager.related_cells_sub_box
                    self.grid_manager[position] = manager

    def find_possible_numbers(self):
        for cell_key in self.grid_manager:
            possible_list = []
            for num in range(1, 10):
                contains = False
                for line_cell in self.grid_manager[cell_key].related_cells_managers:
                    if self.grid[line_cell[0]][line_cell[1]] == num:
                        contains = True
                        break
                if not contains:
                    possible_list.append(num)
            self.grid_manager[cell_key].possible_numbers = possible_list

    def __str__(self):
        return f"""
                Grid Manager Size: {len(self.grid_manager)}"""

    def print_grid(self):
        for row in range(9):
            for column in range(9):
                print(self.grid[row][column], end=" ")
            print()
        print()

    def possible(self, x, y, n):
        for i in range(9):
            if self.grid[i][y] == n:
                return False

        for i in range(9):
            if self.grid[x][i] == n:
                return False

        x0 = x - (x % 3)
        y0 = y - (y % 3)
        for box_x in range(x0, x0 + 3):
            for box_y in range(y0, y0 + 3):
                if self.grid[box_x][box_y] == n:
                    return False
        return True

    def count_empty(self):
        total = 0
        for row in self.grid:
            total += row.count(0)
        return total

    def solve(self):
        self.count += 1
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.grid[x][y] = n
                            if self.count_empty() == 0:
                                print(f"Sudoku Solved in {self.count} interactions")
                                self.print_grid()
                                return
                            self.solve()
                            self.grid[x][y] = 0

                    return
