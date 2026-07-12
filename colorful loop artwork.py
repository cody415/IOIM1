import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colourful Loop Artwork")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed

# Function to draw a petal
def draw_petal(radius, angle):
    pen.circle(radius, angle)
    pen.left(180 - angle)
    pen.circle(radius, angle)
    pen.left(180 - angle)

# Generate a list of colours using HSV
colors = []
num_colors = 36
for i in range(num_colors):
    hue = i / num_colors
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    colors.append(color)

# Draw the pattern
for i in range(num_colors):
    pen.color(colors[i])
    draw_petal(100, 60)
    pen.left(360 / num_colors)

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
