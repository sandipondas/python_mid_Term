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
            for r, c in seat_l:
                if self.seats[id][r][c] == 0:
                    self.seats[id][r][c] == 1
                else:
                    print(f'the seat is booked')
        else:
            print("Chang the show id and try again")
    def view_show_list(self):
        for i in self.show_list:
            print(f'Show id: {i[0]}, Movie name: {i[1]}, time: {i[2]}')
 