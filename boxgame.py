import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
TITLE = "BoxGame"
LEVEL = 1

class Wall(arcade.Sprite):
    def __init__(self, x, y, r, a, b, c):
        super().__init__("images/wall.png")
        self.center_x = x
        self.center_y = y
        self.angle = r
        self.velocity = [a, b]
        self.scale = c
        self.boundary_bottom = 0
        self.boundary_top = SCREEN_HEIGHT
        self.boundary_left = 0
        self.boundary_right = SCREEN_WIDTH
        self.left = self.center_x - (10*self.scale)
        self.right = self.center_x + (10*self.scale)
        self.bottom = self.center_y - (180*self.scale)
        self.top = self.center_y + (180*self.scale)
        self.original_x = self.center_x
        self.original_y = self.center_y

    def change_x(self, a):
        self.center_x = a

    def change_y(self, a):
        self.center_y = a

    def update_velocity(self, a, b):
        self.velocity = [a, b]

    def update(self):
        self.center_x += self.velocity[0]
        self.center_y += self.velocity[1]
        if self.left < self.boundary_left or self.right > self.boundary_right or self.bottom < self.boundary_bottom or self.top > self.boundary_top:
            self.velocity = [0, 0]
            self.center_x = self.original_x
            self.center_y = self.original_y


class Box(arcade.Sprite):
    def __init__(self, x, y, a, b, c):
        super().__init__("images/box2.png")
        self.scale = .5
        self.center_x = x
        self.center_y = y
        self.velocity = [a, b]
        self.scale = c
        self.boundary_bottom = 0
        self.boundary_top = SCREEN_HEIGHT
        self.boundary_left = 0
        self.boundary_right = SCREEN_WIDTH
        self.left = self.center_x - (64 * self.scale)
        self.right = self.center_x + (64 * self.scale)
        self.bottom = self.center_y - (64 * self.scale)
        self.top = self.center_y + (64 * self.scale)

    def update_velocity(self, a, b):
        self.velocity = [a, b]

    def change_x(self, a):
        self.center_x = a

    def change_y(self, a):
        self.center_y = a

    def update(self):
        self.center_x += self.velocity[0]
        self.center_y += self.velocity[1]
        if self.left < self.boundary_left or self.right > self.boundary_right or self.bottom < self.boundary_bottom or self.top > self.boundary_top:
            self.velocity = [0, 0]
        if self.left < self.boundary_left:
            self.center_x = 64*self.scale
        if self.right > self.boundary_right:
            self.center_x = SCREEN_WIDTH-(64*self.scale)
        if self.bottom < self.boundary_bottom:
            self.center_y = 64*self.scale
        if self.top > self.boundary_top:
            self.center_y = SCREEN_HEIGHT-(64*self.scale)

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to BOXGAME", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.GREEN_YELLOW, font_size=70, anchor_x="center")
        arcade.draw_text("Use a mouse press to begin", SCREEN_WIDTH/2, SCREEN_HEIGHT*.30, arcade.color.GO_GREEN, font_size=40, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        next_view = LevelView(1)
        self.window.show_view(next_view)

class LevelView(arcade.View):
    def __init__(self, a):
        super().__init__()

        self.level = a
        self.background = None
        self.background = arcade.load_texture("images/cloud_scene.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        if self.level == 1:
            arcade.draw_text("Let's begin with Level One", SCREEN_WIDTH/2, SCREEN_HEIGHT*.5, arcade.color.BLACK_OLIVE, font_size=45, anchor_x="center")
        elif self.level == 2:
            arcade.draw_text("Good Job! Now onto Level Two", SCREEN_WIDTH / 2, SCREEN_HEIGHT * .5, arcade.color.BLACK_OLIVE, font_size=45, anchor_x="center")
        elif self.level == 3:
            arcade.draw_text("Here's the last one! Let's do Level Three", SCREEN_WIDTH / 2, SCREEN_HEIGHT * .5, arcade.color.BLACK_OLIVE, font_size=45, anchor_x="center")
        elif self.level == 4:
            arcade.draw_text("Good Job! Mouse Press to continue", SCREEN_WIDTH/2, SCREEN_HEIGHT*.5, arcade.color.BLACK_OLIVE, font_size=45, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.level == 1:
            next_view = GameView(1)
        elif self.level == 2:
            next_view = GameView(2)
        elif self.level == 3:
            next_view = GameView(3)
        elif self.level == 4:
            next_view = EndView()
        self.window.show_view(next_view)



class GameView(arcade.View):
    def __init__(self, a):
        super().__init__()

        self.level = a
        self.time_taken = 0
        self.box_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.finish_list = arcade.SpriteList()
        self.flag = arcade.Sprite("images/flag.png")
        self.background = None
        self.background = arcade.load_texture("images/cloud_scene.png")
        if a == 1:
            self.flag.center_x = SCREEN_WIDTH * .8
            self.flag.center_y = SCREEN_HEIGHT * .3
            self.wall_list.append(Wall(180, 10, 90, 0, 0, 1))
            self.wall_list.append(Wall(10, 180, 0, 0, 0, 1))
            self.wall_list.append(Wall(10, 500, 0, 0, 0, 1))
            self.wall_list.append(Wall(700, 550, 90, 0, 0, 1))
            self.box_list.append(Box(84, 84, 0, 0, 1))
        if a == 2:
            self.flag.center_x = SCREEN_WIDTH * .8
            self.flag.center_y = SCREEN_HEIGHT * .7
            self.wall_list.append(Wall(10, 500, 0, 0, 0, 1))
            self.wall_list.append(Wall(180, 680, 90, 0, 0, 1))
            self.wall_list.append(Wall(350, 500, 0, 0, 0, 1))
            self.wall_list.append(Wall(180, 100, 90, 0, 0, 1))
            self.wall_list.append(Wall(360, 100, 90, 0, 0, 1))
            self.wall_list.append(Wall(10, 180, 0, 0, 0, 1))
            self.box_list.append(Box(84, 606, 0, 0, 1))
        if a == 3:
            self.flag.center_x = SCREEN_WIDTH * .1
            self.flag.center_y = SCREEN_HEIGHT * .3
            self.wall_list.append(Wall(5, 90, 0, 0, 0, .5))
            self.wall_list.append(Wall(995, 610, 0, 0, 0, .5))
            self.wall_list.append(Wall(910, 695, 90, 0, 0, .5))
            self.wall_list.append(Wall(500, 695, 90, 0, 0, .5))
            self.wall_list.append(Wall(550, 300, 0, 0, 0, .5))
            self.wall_list.append(Wall(400, 300, 0, 0, 0, .5))
            self.wall_list.append(Wall(550, 210, 0, 0, 0, .5))
            self.wall_list.append(Wall(460, 125, 90, 0, 0, .5))
            self.wall_list.append(Wall(370, 125, 90, 0, 0, .5))
            self.wall_list.append(Wall(285, 215, 0, 0, 0, .5))
            self.wall_list.append(Wall(150, 400, 90, 0, 0, .5))
            self.box_list.append(Box(958, 658, 0, 0, .5))




    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.wall_list.draw()
        self.box_list.draw()
        self.flag.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            for i in self.wall_list:
                i.update_velocity(0, 2)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            for i in self.wall_list:
                i.update_velocity(0, -2)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            for i in self.wall_list:
                i.update_velocity(2, 0)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            for i in self.wall_list:
                i.update_velocity(-2, 0)
        elif key == arcade.key.R:
            next_view = GameView(self.level)
            self.window.show_view(next_view)

    def on_update(self, delta_time):
        self.wall_list.update()
        self.box_list.update()
        for i in range(0, len(self.wall_list)):
            if abs(self.wall_list[i].center_x - self.wall_list[i].original_x) > SCREEN_WIDTH*.05 or abs(self.wall_list[i].center_y - self.wall_list[i].original_y) > SCREEN_HEIGHT*.05:
                self.wall_list[i].center_x = self.wall_list[i].original_x
                self.wall_list[i].center_y = self.wall_list[i].original_y
                self.wall_list[i].velocity = [0, 0]
        if arcade.check_for_collision(self.box_list[0], self.flag):
            next_view = LevelView(self.level + 1)
            self.window.show_view(next_view)
        for i in self.wall_list:
            if arcade.check_for_collision(self.box_list[0], i):
                [a, b] = i.velocity
                self.box_list[0].update_velocity(a, b)

class EndView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Congrats on beating BOXGAME", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.GREEN_YELLOW, font_size=55, anchor_x="center")
        arcade.draw_text("Use a mouse press to restart", SCREEN_WIDTH/2, SCREEN_HEIGHT*.30, arcade.color.GO_GREEN, font_size=40, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        next_view = LevelView(1)
        self.window.show_view(next_view)



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()