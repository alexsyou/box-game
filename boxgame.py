import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
TITLE = "BoxGame"

class Wall(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("images/wall.png")
        self.center_x=x
        self.center_y=y

    def update(self):
        pass

class Box(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("images/box.png")
        self.scale=.5
        self.center_x=x
        self.center_y=y

    def update(self):
        pass

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to BOXGAME", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.GREEN_YELLOW, font_size=70, anchor_x="center")
        arcade.draw_text("Use a mouse press to begin", SCREEN_WIDTH/2, SCREEN_HEIGHT*.30, arcade.color.GO_GREEN, font_size=40, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.time_taken=0
        self.box_list = arcade.SpriteList
        self.wall_list = arcade.SpriteList
        self.finish_list = arcade.SpriteList

    def setup(self):
        self.wall_list.append(Wall(500,500))

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        Box(200,300).draw()



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()