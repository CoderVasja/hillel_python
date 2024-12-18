class Figure:

    def __init__(self, side_a, angle_b, angle_a):
        self.side_a = side_a
        self.angle_b = angle_b
        self.angle_a = angle_a

    def __setattr__(self, key, value):

        if key == 'side_a':
            if value <= 0:
                raise AttributeError('Side A should be bigger than 0')

        elif key == 'angle_b':
            if value <= 0 or value >= 179:
                raise AttributeError('Angle should be bigger than 0 and less than 179')

        elif key == 'angle_a':
            if value <= 0 or value >= 179:
                raise AttributeError('Angle should be bigger than 0 and less than 179')

        super().__setattr__(key, value)


        if hasattr(self, 'angle_a') and hasattr(self, 'angle_b'):
            self.correct_angle_sum()

    def correct_angle_sum(self):

        if self.angle_a + self.angle_b != 180:
            if self.angle_a > self.angle_b:
                self.angle_b = 180 - self.angle_a
            else:
                self.angle_a = 180 - self.angle_b


romb1 = Figure(10, 120, 80)
print(f'\nSide A: {romb1.side_a}\nAngle A: {romb1.angle_a}\nAngle B: {romb1.angle_b}')


romb1.angle_a = 170
print(f'\nSide A: {romb1.side_a}\nAngle A: {romb1.angle_a}\nAngle B: {romb1.angle_b}')


romb1.angle_b = 90
print(f'\nSide A: {romb1.side_a}\nAngle A: {romb1.angle_a}\nAngle B: {romb1.angle_b}')
