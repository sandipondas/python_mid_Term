class Star_Cinema:
    hall_list = []
    def entry_hall(self,hall):
        self.hall_list.append(hall)

hall1 = Hall(5,6,101)
Star_Cinema.entry_hall(hall1)