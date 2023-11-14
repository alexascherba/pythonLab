import tkinter as tk
from tkinter import ttk
import pygame
from snake import *
import sys
from food import Food
#test commit/ new new nnnn
def button_clicked(number):
    if number == 1:
        print(f"Button 1 clicked!")
        root.destroy()  # Close the window after button click
    elif number == 2:
        root.destroy()  # Close the window after button click

        pygame.init()
        bounds = (700, 400)
        window = pygame.display.set_mode(bounds)
        pygame.display.set_caption("Snake")
        block_size = 20
        snake = Snake(block_size, bounds)
        food = Food(block_size, bounds)
        font = pygame.font.SysFont('Calibri', 100, True)

        while True:
            pygame.time.delay(110)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                snake.steer(Direction.LEFT)
            elif keys[pygame.K_RIGHT]:
                snake.steer(Direction.RIGHT)
            elif keys[pygame.K_DOWN]:
                snake.steer(Direction.DOWN)
            elif keys[pygame.K_UP]:
                snake.steer(Direction.UP)
            snake.move()
            snake.check_for_food(food)
            if snake.check_bounds() == True or snake.check_tail_collision() == True:
                text = font.render('Game Over:(', True, (255, 255, 255))
                window.blit(text, (15, 100))
                pygame.display.update()
                pygame.time.delay(2000)
                snake.respawn()
                food.respawn()
            window.fill((0, 0, 0))
            snake.draw(pygame, window)
            food.draw(pygame, window)
            pygame.display.flip()


    elif number == 3:
        print(f"Button 3 clicked!")
        root.destroy()  # Close the window after button click
    elif number == 4:
        print(f"Button 4 clicked!")
        root.destroy()  # Close the window after button click

# Создаем основное окно
root = tk.Tk()
root.title("Minigames with love")

# Устанавливаем фиксированный размер окна
root.geometry("700x400")

# Устанавливаем фоновый цвет
root.configure(bg="#8AAEBC")

# Создаем и размещаем надпись "MINIGAMES"
label = tk.Label(root, text="MINIGAMES", font=("Anonymous Pro", 60), fg="#EAE0DB", bg="#8AAEBC")
label.grid(row=0, column=1, pady=20, columnspan=2)

# Создаем стиль для кнопок
button_style = ttk.Style()
button_style.configure("TButton", font=("Anonymous Pro", 32), background="#EAE0DB", foreground="#8AAEBC", padding=(20, 10))

# Создаем кнопки с разными надписями
button_labels = ["Tetris", "Snake", "Game 3", "Game 4"]
buttons = []
for i, label_text in enumerate(button_labels, start=1):
    button = ttk.Button(root, text=label_text, style="TButton", command=lambda num=i: button_clicked(num))
    buttons.append(button)

# Размещаем кнопки в виде сетки
buttons[0].grid(row=1, column=1, padx=20, pady=20)
buttons[1].grid(row=1, column=2, padx=20, pady=20)
buttons[2].grid(row=2, column=1, padx=20, pady=20)
buttons[3].grid(row=2, column=2, padx=20, pady=20)

# Запускаем основной цикл обработки событий
root.mainloop()
