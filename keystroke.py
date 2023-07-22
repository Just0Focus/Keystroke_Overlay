import tkinter as tk
import pygame
from pygame.locals import *

def light_up(event):
    key = event.char.lower()
    if key == 'a':
        box_a.config(bg='yellow')
    elif key == 's':
        box_s.config(bg='yellow')
    elif key == 'd':
        box_d.config(bg='yellow')
    elif key == 'w':
        box_w.config(bg='yellow')
    elif key == 'f' or key == 'y':
        box_f.config(bg='yellow')

def turn_off(event):
    key = event.char.lower()
    if key == 'a':
        box_a.config(bg='white')
    elif key == 's':
        box_s.config(bg='white')
    elif key == 'd':
        box_d.config(bg='white')
    elif key == 'w':
        box_w.config(bg='white')
    elif key == 'f' or key == 'y':
        box_f.config(bg='white')

# Create the window
window = tk.Tk()
window.title("Key Light Up")
window.attributes("-alpha", 0.8)  # Set transparency (0.0 to 1.0)

# Set Discord-colored background
background_color = '#2C2F33'
window.config(bg=background_color)
font = ('Arial', 18)

light_grey = '#d3d3d3'
bg = light_grey

# Create the boxes
box_w = tk.Label(window, text='W', width=10, height=5, bg=bg, font=font)
box_w.grid(row=1, column=2)

box_blank1 = tk.Label(window, text='', width=10, height=5, bg=background_color)
box_blank1.grid(row=2, column=0)

box_a = tk.Label(window, text='A', width=10, height=5, bg=bg, font=font)
box_a.grid(row=2, column=1)
box_s = tk.Label(window, text='S', width=10, height=5, bg=bg, font=font)
box_s.grid(row=2, column=2)
box_d = tk.Label(window, text='D', width=10, height=5, bg=bg, font=font)
box_d.grid(row=2, column=3)

box_blank2 = tk.Label(window, text='', width=10, height=5, bg=background_color)
box_blank2.grid(row=2, column=4)

box_f = tk.Label(window, text='F', width=10, height=5, bg=bg, font=font)
box_f.grid(row=2, column=5)

box_blank3 = tk.Label(window, text='', width=10, height=6, bg=background_color)
box_blank3.grid(row=2, column=6)

# Create the movement display
movement_display = tk.Canvas(window, width=300, height=200, bg=bg)
movement_display.grid(row=1, column=7, rowspan=2)

box_blank4 = tk.Label(window, text='', width=10, height=6, bg=background_color)
box_blank4.grid(row=2, column=8)

# Initialize pygame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Bind key press and release events
window.bind('<KeyPress>', light_up)
window.bind('<KeyRelease>', turn_off)

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

    size = 10
    
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

'''
The script stops listening to 'a', 's', 'd', 'w', 'f', and 'y' when a game controller is connected.

'''
