import tkinter as tk
import math


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
RADIUS = 200
CENTER_X = CANVAS_WIDTH // 2
CENTER_Y = CANVAS_HEIGHT // 2
INITIAL_SPEED = 0.003
SPEED_CHANGE = 0.001


class MovingPointCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Point Canvas")

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.angle = 0
        self.speed = INITIAL_SPEED
        self.direction = 1  # 1 против часовой, -1 по часовой

        self.canvas.bind("<B1-Motion>", self.draw_point)

        self.add_buttons()
        self.draw_circle()
        self.move_point()

    def add_buttons(self):
        button_configurations = [
            ("Increase Speed", self.increase_speed),
            ("Decrease Speed", self.decrease_speed),
            ("Change Direction", self.change_direction),
        ]

        self.buttons = {}
        for text, command in button_configurations:
            btn = tk.Button(self.root, text=text, command=command)
            btn.pack()
            self.buttons[text] = btn

    def draw_circle(self):
        x0 = CENTER_X - RADIUS
        y0 = CENTER_Y - RADIUS
        x1 = CENTER_X + RADIUS
        y1 = CENTER_Y + RADIUS
        self.canvas.create_oval(x0, y0, x1, y1, outline="black")

    def move_point(self):
        x = CENTER_X + RADIUS * math.cos(self.angle)
        y = CENTER_Y + RADIUS * math.sin(self.angle)
        self.canvas.delete("point")
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue", tags="point")

        self.angle -= self.direction * self.speed
        self.root.after(10, self.move_point)

    def draw_point(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def change_speed(self, change):
        if self.speed > 0:
            self.speed += change
        else:
            self.speed -= change

        self.update_button_state()

    def decrease_speed(self):
        self.change_speed(-SPEED_CHANGE)

    def increase_speed(self):
        self.change_speed(SPEED_CHANGE)

    def change_direction(self):
        self.direction *= -1

    def update_button_state(self):
        if self.speed == 0:
            self.buttons["Decrease Speed"]["state"] = "disabled"
            self.buttons["Change Direction"]["state"] = "disabled"
            self.show_message("Speed is zero")
        else:
            self.buttons["Decrease Speed"]["state"] = "normal"
            self.buttons["Change Direction"]["state"] = "normal"
            self.show_message("")

    def show_message(self, message):
        self.canvas.delete("message")
        self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT - 20, text=message, tags="message")


if __name__ == "__main__":
    root = tk.Tk()
    app = MovingPointCanvas(root)
    root.mainloop()
