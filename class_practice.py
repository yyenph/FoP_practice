class Taxicab:
    def __init__(self, current_x,current_y):
        self._current_x=current_x
        self._current_y=current_y
        current_odormeter=0
    def get_x_coord(self):
        return self._current_x
    
    def get_y_coord(self):
        return self._current_y
    def get_odormeter(self):
        return (self._current_x,self._current_y)
    
    def move_x(self,num):
        self._current_x +=num

    def move_y(self,numy):
        self._current_y +=numy


cab=Taxicab(5,-8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odormeter())


     
