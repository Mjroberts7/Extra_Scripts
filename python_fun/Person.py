import random 
class Person():
    list: color = [black, red, blue, green, white, pink, purple]
    def __init__(self, name, body_type):
        self.name = name
        self.body_type = body_type

    def head(self, nose, ears, eyes):
        self.nose = nose
        self.ears = ears
        self.eyes = eyes

    def hands(self, fingers):
        self.fingers = fingers
        number_of_fingers = 10
        fingers_per_hand = 5

    def feet(self, toes):
        self.toes = toes
        number_of_toes = 10
        toes_per_foot = 5
    
    def outfit(self, pants, shirt, shoes):
        self.pants = pants
        self.shirt = shirt
        self.shoes = shoes

def pick_color(cloth):
    color_of_cloth = random.choice(cloth)
    return color_of_cloth
