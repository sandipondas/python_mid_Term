class Star_Cinema:
    hall_list = []
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        item = (id, movie_name, time)
        self.show_list.append(item)
        seat = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = seat

    def book_seats(self, id, seat_l):
        if id in self.seats :
            for row, column in seat_l:
                if self.seats[id][row][column] == 0:
                    self.seats[id][row][column] == 1
                    print('\nsuccessful\n')
                    return
        else:
            return
    def view_show_list(self):
        for i in self.show_list:
            print(f'Show id: {i[0]}, Movie name: {i[1]}, time: {i[2]}')
        return
    def view_available_seats(self, id):
        if id in self.seats:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[id][i][j] == 0:
                        print(f'available seat:{i},{j}')
                        return
        
        return
    
        


counter = Hall(3,3,101)
counter.entry_show(1,'jawan','5:00PM')


    

