class Sprites:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.items = []
        self.obstacles = []

    def add_player(self, player_sprite):
        self.player = player_sprite

    def add_enemy(self, enemy_sprite):
        self.enemies.append(enemy_sprite)

    def add_item(self, item_sprite):
        self.items.append(item_sprite)

    def add_obstacle(self, obstacle_sprite):
        self.obstacles.append(obstacle_sprite)

def get_default_sprites():
    sprites = Sprites()
    sprites.add_player("default_player_sprite.png")
    sprites.add_enemy("default_enemy_sprite.png")
    sprites.add_item([])
    sprites.add_obstacle([])
    return sprites

customize_character: str = input("Would you like to customize your character? (yes/no): ")

if (customize_character.lower() == "yes"):
    player_sprite_name = input("Enter the filename for your custom player sprite: ")
    sprite = Sprites().add_player(player_sprite_name)
else:
    sprite = get_default_sprites()