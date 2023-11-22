import tkinter as tk
import random


class Drop:
    def __init__(self, canvas, size, speed, color):
        self.canvas = canvas
        self.size = size
        self.speed = speed
        self.color = color
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 200)
        self.id = canvas.create_oval(self.x, self.y, self.x + size, self.y + size * 2, fill=color)

    def move(self):
        self.y += self.speed
        self.canvas.move(self.id, 0, self.speed)

        # Если капля достигла нижней границы, переместите ее вверх с новыми случайными координатами
        if self.y > 400:
            self.y = random.randint(0, 50)
            self.size = random.randint(5, 15)
            self.speed = random.uniform(1, 3)
            self.color = random.choice(["#000080", "#87CEEB", "#808080"])  # Синий, голубой, серый

            self.canvas.itemconfig(self.id, fill=self.color)
            self.canvas.coords(self.id, self.x, self.y, self.x + self.size, self.y + self.size * 2)


class RainAnimation:
    def __init__(self, root, width, height, density):
        self.root = root
        self.width = width
        self.height = height
        self.density = density
        self.root.title("Rain Animation")

        self.canvas = tk.Canvas(root, width=width, height=height, bg="#87CEEB")  # Голубое небо
        self.canvas.pack()

        self.drops = [Drop(self.canvas, random.randint(5, 15), random.uniform(1, 3), random.choice(["#000080", "#87CEEB", "#808080"])) for _ in range(density)]  # Синий, голубой, серый

        self.root.after(10, self.animate)

    def animate(self):
        for drop in self.drops:
            drop.move()

        self.root.after(10, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    width, height = 800, 400
    density = 100

    animation = RainAnimation(root, width, height, density)
    root.mainloop()
