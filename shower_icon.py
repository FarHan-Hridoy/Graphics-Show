import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np  # Import numpy for mathematical functions

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the pipe (top vertical rectangle)
pipe = patches.Rectangle((0.45, 1.05), 0.1, 0.2, color='black')
ax.add_patch(pipe)

# Draw the shower head (semi-circle)
head = patches.Wedge(center=(0.5, 0.95), r=0.2, theta1=0, theta2=180, color='black')
ax.add_patch(head)

# Water drops setup (all starting from shower head)
drop_radius = 0.018
head_center_x = 0.5
head_center_y = 0.95

initial_drops = [
    [0.3, head_center_y], [0.5, head_center_y], [0.7, head_center_y],
    [0.35, head_center_y], [0.5, head_center_y], [0.65, head_center_y],
    [0.4, head_center_y], [0.5, head_center_y], [0.6, head_center_y],
    [0.45, head_center_y], [0.5, head_center_y], [0.55, head_center_y]
]

# Create circle patches for drops
drops = [plt.Circle((x, y), drop_radius, color='blue') for x, y in initial_drops]
for drop in drops:
    ax.add_patch(drop)

# Animation function to update the position of drops
def animate(frame):
    for i, drop in enumerate(drops):
        x, y = drop.center
        
        # Add slight horizontal movement based on position
        wobble = 0.002 * np.sin(2 * np.pi * (frame/30 + i/len(drops)))
        x = initial_drops[i][0] + wobble
        
        # Accelerating fall speed
        speed = 0.008 * (1 + 0.1 * (head_center_y - y))
        y -= speed
        
        # Reset position to shower head when drops reach bottom
        if y < 0:
            y = head_center_y
            x = initial_drops[i][0]
        
        # Make drops more transparent as they fall
        alpha = 1.0 - (head_center_y - y) * 0.5
        drop.set_alpha(max(0.3, alpha))
        
        drop.center = (x, y)
    return drops

# Set axis properties
plt.xlim(0, 1)
plt.ylim(0, 1.3)
plt.axis('off')
ax.set_aspect('equal', adjustable='box')
plt.title("Animated Shower Icon")

# Create the animation
ani = animation.FuncAnimation(
    fig, 
    animate,
    frames=400,  # More frames for smoother animation
    interval=30,  # Faster updates
    blit=True    # Better performance
)

# Save the animation as a GIF (requires pillow library)
ani.save('shower_animation.gif', 
         writer='pillow',
         fps=30)

print("Animation saved as 'shower_animation.gif'. Open this file to view the animation.")
