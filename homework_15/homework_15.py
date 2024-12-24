class Figure:

    def __init__(self, side_a, angle_a, angle_b):

        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b

    def __setattr__(self, key, value):

        if key == 'side_a':
            if value <= 0:
                raise AttributeError('Side A should be bigger than 0')
        elif key == 'angle_a':
            if value <= 0 or value > 179:
                raise AttributeError('Angle should be bigger than 0 and less than 179')


        super().__setattr__(key, value)


        if key == 'angle_a':
            object.__setattr__(self, 'angle_b', 180 - value)

        if key == 'angle_b':
            object.__setattr__(self, 'angle_a', 180 - value)

        if hasattr(self, 'angle_a') and hasattr(self, 'angle_b'):
            if self.angle_a + self.angle_b != 180:
                raise AttributeError('Sum of angles should be 180')


romb1 = Figure(5, 80,110)
print(romb1)

romb1.angle_a = 60
print(f'\nSide A: {romb1.side_a}\nAngle B: {romb1.angle_b}\nAngle A: {romb1.angle_a}')

romb1.angle_b = 10
print(f'\nSide A: {romb1.side_a}\nAngle B: {romb1.angle_b}\nAngle A: {romb1.angle_a}')




