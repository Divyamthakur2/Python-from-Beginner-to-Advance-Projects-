# Goal: Track game score using a global variable

score = 20  # global variable

def add_points(points):
    global score
    score = score + points
    print(f"Added {points} points. Total: {score}")

def reset_score():
    global score
    score = 0
    print("Score reset to 0")

# Test it
add_points(10)
add_points(25)
add_points(5)
reset_score()
add_points(50)