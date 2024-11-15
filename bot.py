import tkinter as tk
import random

class RobotEyesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute Anime Robot Eyes")

        # Set the window size
        self.root.geometry("300x300")

        # Create a canvas with a black background
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='black')
        self.canvas.pack()

        # Draw robot head (soft, round shape for cuteness)
        self.canvas.create_oval(50, 50, 250, 250, fill='#333333', outline='#333333', width=3)

        # Draw larger, expressive robot eyes
        self.left_eye = self.canvas.create_oval(70, 70, 130, 130, fill='white', outline='black', width=3)
        self.right_eye = self.canvas.create_oval(170, 70, 230, 130, fill='white', outline='black', width=3)

        # Draw pupils (larger pupils for cuteness)
        self.left_pupil = self.canvas.create_oval(90, 90, 110, 110, fill='black')
        self.right_pupil = self.canvas.create_oval(190, 90, 210, 110, fill='black')

        # Add shiny highlights to the eyes for an anime effect
        self.left_highlight = self.canvas.create_oval(100, 95, 110, 105, fill='white', outline='white')
        self.right_highlight = self.canvas.create_oval(200, 95, 210, 105, fill='white', outline='white')

        # Make the smile smaller
        self.mouth = self.canvas.create_arc(120, 170, 180, 200, start=0, extent=-180, style=tk.ARC, width=5, outline='white')

        # Add event listener to follow mouse
        self.root.bind('<Motion>', self.follow_mouse)

        # Start the animation loop (blinking, etc.)
        self.animate()

    def follow_mouse(self, event):
        """Make pupils follow the mouse cursor"""
        # Coordinates for the centers of the eyes
        left_eye_center = (100, 100)
        right_eye_center = (200, 100)

        # Move left pupil towards the mouse cursor
        self.move_pupil(self.left_pupil, left_eye_center, event.x, event.y)

        # Move right pupil towards the mouse cursor
        self.move_pupil(self.right_pupil, right_eye_center, event.x, event.y)

    def move_pupil(self, pupil, eye_center, mouse_x, mouse_y):
        """Move pupil towards the mouse position but with some random 'jerk' effect"""
        eye_x, eye_y = eye_center

        # Calculate the direction to the mouse position
        delta_x = mouse_x - eye_x
        delta_y = mouse_y - eye_y

        # Add some randomness to simulate the eyes "jerking" or "twitching"
        delta_x += random.uniform(-2, 2)
        delta_y += random.uniform(-2, 2)

        # Limit pupil movement to stay within the eye bounds
        max_distance = 12
        distance = (delta_x**2 + delta_y**2)**0.5
        if distance > max_distance:
            factor = max_distance / distance
            delta_x *= factor
            delta_y *= factor

        # Move the pupil
        self.canvas.coords(pupil, eye_x - 10 + delta_x, eye_y - 10 + delta_y, eye_x + 10 + delta_x, eye_y + 10 + delta_y)

    def animate(self):
        """Animate the robot by making it blink and twitch its eyes"""
        # Start blinking at random intervals
        self.blinking()

        # Add random eye twitches or head tilts
        self.random_twitch()

        # Repeat the animation loop
        self.root.after(100, self.animate)

    def blinking(self):
        """Randomly make the robot blink"""
        # Randomly choose whether to blink or not
        if random.random() < 0.02:  # Blink with a low probability
            self.canvas.itemconfig(self.left_pupil, state='hidden')
            self.canvas.itemconfig(self.right_pupil, state='hidden')
            self.canvas.itemconfig(self.left_highlight, state='hidden')
            self.canvas.itemconfig(self.right_highlight, state='hidden')

            # Make it visible again after a short delay
            self.root.after(200, self.open_eyes)

    def open_eyes(self):
        """Open the eyes after blinking"""
        self.canvas.itemconfig(self.left_pupil, state='normal')
        self.canvas.itemconfig(self.right_pupil, state='normal')
        self.canvas.itemconfig(self.left_highlight, state='normal')
        self.canvas.itemconfig(self.right_highlight, state='normal')

    def random_twitch(self):
        """Occasionally move the eyes in a random direction"""
        if random.random() < 0.05:  # 5% chance of twitching
            # Choose a random direction to move the eyes (left/right/up/down)
            direction = random.choice(['left', 'right', 'up', 'down'])
            if direction == 'left':
                self.canvas.move(self.left_eye, -3, 0)
                self.canvas.move(self.right_eye, -3, 0)
            elif direction == 'right':
                self.canvas.move(self.left_eye, 3, 0)
                self.canvas.move(self.right_eye, 3, 0)
            elif direction == 'up':
                self.canvas.move(self.left_eye, 0, -3)
                self.canvas.move(self.right_eye, 0, -3)
            elif direction == 'down':
                self.canvas.move(self.left_eye, 0, 3)
                self.canvas.move(self.right_eye, 0, 3)

            # Return eyes to center after a short delay
            self.root.after(500, self.reset_eye_position)

    def reset_eye_position(self):
        """Reset eyes back to their original position"""
        self.canvas.coords(self.left_eye, 70, 70, 130, 130)
        self.canvas.coords(self.right_eye, 170, 70, 230, 130)

# Create the main window
root = tk.Tk()
app = RobotEyesApp(root)

# Run the application
root.mainloop()
