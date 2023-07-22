import tkinter as tk
import pygame
from pygame.locals import *



# Create the window
window = tk.Tk()
window.title("JoyStick")
window.attributes("-alpha", 0.8)  # Set transparency (0.0 to 1.0)

# Set Discord-colored background
background_color = '#2C2F33'
window.config(bg=background_color)
font = ('Arial', 18)

light_grey = '#d3d3d3'
bg = light_grey


# box_blank1 = tk.Label(window, text='', width=10, height=5, bg=background_color)
# box_blank1.grid(row=2, column=0)


# Create the movement display
movement_display = tk.Canvas(window, width=300, height=200, bg=background_color)
movement_display.grid(row=1, column=7, rowspan=2)

# Initialize pygame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


def check_game_controller():
    pygame.event.pump()
    x_axis = joystick.get_axis(0)
    right_trigger = joystick.get_axis(5)  # Replace 5 with the correct axis index for the right trigger
    if right_trigger < 0.01:
        right_trigger = 0
    left_trigger = joystick.get_axis(4)   # Replace 4 with the correct axis index for the left trigger
    if left_trigger < 0.01:
        left_trigger = 0

    movement_display.delete("dot")
    dot_x = 150 + (x_axis * 100)
    dot_y = 100 - (right_trigger - left_trigger) * 100

    size = 50
    
    movement_display.create_oval(
        dot_x-size, 
        dot_y-size, 
        dot_x+size, 
        dot_y+size, 
        fill='red', tags="dot")

def game_controller_listener():
    check_game_controller()
    window.after(20, game_controller_listener)

# Start the game controller listener
game_controller_listener()

# Run the window's event loop
window.mainloop()

