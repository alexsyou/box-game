import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
TITLE = "BoxGame"

class Wall(arcade.Sprite):
    def __init__(self, x, y, r, a, b):
        super().__init__("images/wall.png")
        self.center_x = x
        self.center_y = y
        self.angle = r
        self.velocity = [a, b]
        self.boundary_bottom = 0
        self.boundary_top = SCREEN_HEIGHT
        self.boundary_left = 0
        self.boundary_right = SCREEN_WIDTH

    def update_velocity(self, a, b):
        self.velocity = [a, b]

    def update(self):
        self.center_x += self.velocity[0]
        self.center_y += self.velocity[1]


class Box(arcade.Sprite):
    def __init__(self, x, y, a, b):
        super().__init__("images/box.png")
        self.scale = .5
        self.center_x = x
        self.center_y = y
        self.velocity = [a, b]

    def update_velocity(self, a, b):
        self.velocity = [a, b]

    def update(self):
        self.center_x += self.velocity[0]
        self.center_y += self.velocity[1]

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

        self.time_taken = 0
        self.box_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.finish_list = arcade.SpriteList()
        self.wall_list.append(Wall(200, 300, 90, 5, 1))
        self.wall_list.append(Wall(200, 300, 0, 1, 1))
        self.box_list.append(Box(600, 400, 0, 0))

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.box_list.draw()

    def on_update(self, delta_time):
        self.wall_list.update()
        self.box_list.update()
        for i in self.wall_list:
            if arcade.check_for_collision(self.box_list[0], i):
                [a, b] = i.velocity
                [c, d] = self.box_list[0].velocity
                i.update_velocity(c, d)
                self.box_list[0].update_velocity(a, b)






def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()