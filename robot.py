class Robot(object):

    def __init__(self,width,height,direction,position):
        self.width=width
        self.height=height
        self.direction=direction
        self.center_position=position


    def run(self):
        self.center_position=(self.center_position[0], self.center_position[1]+.2)
