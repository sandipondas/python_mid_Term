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
        seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seat  


