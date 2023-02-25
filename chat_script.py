import random
import os

# List of possible lines for each line of the poem
line1 = ["The sun sets low", "A lone bird sings", "Autumn leaves fall"]
line2 = ["The wind whispers softly", "In the distance, a train's horn", "Stars twinkle bright"]
line3 = ["All is quiet", "The world is at peace", "Nature's beauty surrounds us"]

# Select a random line from each list to form the poem
poem = f"{random.choice(line1)}\n{random.choice(line2)}\n{random.choice(line3)}"

# Print the poem to the console
print(poem)

# Use the espeak command to convert the poem to speech
os.system(f"espeak '{poem}'")