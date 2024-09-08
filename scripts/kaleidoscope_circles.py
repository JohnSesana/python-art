import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black
screen.title("Kaleidoscope Circles")

# Set the screen size
screen.setup(width=800, height=800)  # Set the width and height of the window

# Calculate the center of the screen
center_x = 0
center_y = 200

# Create a turtle object
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed
artist.hideturtle()  # Hide the turtle icon

def draw_rotated_circles(radius, num_circles, angle_step, color):
    """Draw a series of concentric circles with each rotated slightly, centered in the middle of the screen."""
    artist.color(color)  # Set the turtle color
    for i in range(num_circles):
        # Calculate the angle to rotate the turtle for the current circle
        angle = i * angle_step
        
        artist.penup()
        artist.goto(center_x, center_y - radius)  # Move the turtle to the starting position for the circle
        artist.pendown()
        artist.setheading(angle)  # Set the direction of the turtle
        
        # Draw the circle with the current angle
        artist.circle(radius)

def main():
    radius = 100  # Radius of each circle
    num_circles = 36  # Number of circles
    angle_step = 10  # Angle step for rotating each circle
    i = 0
    colors = ["red", "green", "blue", "yellow", "white", "purple", "cyan", "orange"]

    while True:
        i = i + 1
        if i == 10:
            artist.clear()
        # Draw the rotated circles with random colors
        color = random.choice(colors)  # Pick a random color from the list
        draw_rotated_circles(radius, num_circles, angle_step, color)

# Start drawing
main()

# Keep the window open until closed by the user
turtle.done()