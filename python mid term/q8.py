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

    def book_seats(self, id, seat_l):
        if id in self.seats:
            for row, column in seat_l:
                if row < 0 or row >= self.rows or column < 0 or column >= self.cols:
                    print(f"Invalid seat: ({row}, {column})")
                    return  
                
                if self.seats[id][row][column] == 0:
                    self.seats[id][row][column] = 1  
                    print("Booking successful ")
                else:
                    print("The seat is already booked.")
                    return  
        else:
            print("This show is not found")
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
        else:
            print("Chang the show id and try again")
    


counter = Hall(5,5,101)
counter.entry_show(1,'jawan','5:00PM')
run = True
while run :
    print("options: \n 1.view all shows that are running \n 2.view available seats in a show \n  3.Book a ticket: \n 4.exit: \n\n")
    q = int(input("enter : "))
    if q==1:
        counter.view_show_list()
    elif q==2:
        id = int(input("enter show id: "))
        counter.view_available_seats(id)
    elif q==3:
        id = int(input("enter show id: "))
        num = int(input("how many seat you need: "))

        seat_l = []
        for i in range(0,num):
            a = int(input("seat row: "))
            b = int(input("seat cls: "))
            seat_l.append((a,b))
        print(counter.book_seats(id,seat_l))
    else:
        break
    

    

