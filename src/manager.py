class Manager:

    right_number = 0
    related_cells_in_line = []
    related_cells_in_column = []
    related_cells_managers = []
    related_cells_sub_box = []
    possible_numbers = []

    def __init__(self, position, grid, grid_manager):
        self.grid = grid
        self.grid_manager = grid_manager
        self.position = position

    def try_number(self, number):
        response = False
        print(f"Number: {number}")
        self.grid[self.position[0]][self.position[1]] = number
        self.possible_numbers = []
        for position in self.related_cells_managers:
            try:
                if number in self.grid_manager[position].possible_numbers:
                    self.grid_manager[position].possible_numbers.remove(number)
                    # print(self)
                    response = True
            except KeyError:
                response = False
        # self.print_grid()
        return response


    def __str__(self):
        return f"""
        Position: {self.position}
        Possible Numbers:               {self.possible_numbers}
        Possible Numbers Size:          {len(self.possible_numbers)}
        Related Cells Managers:         {self.related_cells_managers}
        Related Cells Managers Size:    {len(self.related_cells_managers)}
        Related Cells In Line:          {self.related_cells_in_line}
        Related Cells In Column:        {self.related_cells_in_column}
        Related Cells In Sub Box:       {self.related_cells_sub_box}"""

    def print_grid(self):
        for row in range(9):
            for column in range(9):
                print(self.grid[row][column], end=" ")
            print()
        print()
