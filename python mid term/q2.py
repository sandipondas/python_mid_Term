class Star_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, columns, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.columns = columns
        self.hall_no = hall_no
        self.entry_hall(self)

hall1 = Hall(5,6,101)
hall2 = Hall(10,6,102)
#print(Star_Cinema.hall_list[0].hall_no)
for obj in Star_Cinema.hall_list:
    print(obj.hall_no)
