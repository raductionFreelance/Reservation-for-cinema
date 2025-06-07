class CinemaHall:
    def __init__(self, row, number_chairs):
        self.row=row
        self.number_chairs=number_chairs
        self.size=self.row*self.number_chairs
        self.chairs=[0]*self.size
    def take_order(self, place):
        if self.chairs[place-1]==0:
            self.chairs[place-1]=1
        else:
            print("This place isn't avaible")
    def cancel_order(self, place):
        if self.chairs[place-1]==1:
            self.chairs[place-1]=0
    def cout(self):
        print(self.chairs)
