import tkinter as tk
import random

class RobotEyesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Eyes")

        # Set the window size
        self.root.geometry("300x300")

        # Create a canvas to draw the robot eyes
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='white')
        self.canvas.pack()

        # Draw robot head (optional)
        self.canvas.create_oval(50, 50, 250, 250, fill='gray', outline='black', width=5)

        # Draw robot eyes
        self.left_eye = self.canvas.create_oval(70, 70, 130, 130, fill='white', outline='black', width=3)
        self.right_eye = self.canvas.create_oval(170, 70, 230, 130, fill='white', outline='black', width=3)

        # Draw pupils (initial position)
        self.left_pupil = self.canvas.create_oval(90, 90, 110, 110, fill='black')
        self.right_pupil = self.canvas.create_oval(190, 90, 210, 110, fill='black')

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
        delta_x += random.uniform(-5, 5)
        delta_y += random.uniform(-5, 5)

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

            # Make it visible again after a short delay
            self.root.after(200, self.open_eyes)

    def open_eyes(self):
        """Open the eyes after blinking"""
        self.canvas.itemconfig(self.left_pupil, state='normal')
        self.canvas.itemconfig(self.right_pupil, state='normal')

    def random_twitch(self):
        """Occasionally move the eyes in a random direction"""
        if random.random() < 0.05:  # 5% chance of twitching
            # Choose a random direction to move the eyes (left/right/up/down)
            direction = random.choice(['left', 'right', 'up', 'down'])
            if direction == 'left':
                self.canvas.move(self.left_eye, -5, 0)
                self.canvas.move(self.right_eye, -5, 0)
            elif direction == 'right':
                self.canvas.move(self.left_eye, 5, 0)
                self.canvas.move(self.right_eye, 5, 0)
            elif direction == 'up':
                self.canvas.move(self.left_eye, 0, -5)
                self.canvas.move(self.right_eye, 0, -5)
            elif direction == 'down':
                self.canvas.move(self.left_eye, 0, 5)
                self.canvas.move(self.right_eye, 0, 5)

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
