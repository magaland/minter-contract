import time
import os

# Dimensions of the table
TABLE_WIDTH = 20
TABLE_HEIGHT = 10

# Ball positions
cue_ball = {"x": 5, "y": 5}
target_ball = {"x": 15, "y": 5}


def draw_table(cue_ball, target_ball):
    """Draw the table with balls."""
    os.system("cls" if os.name == "nt" else "clear")
    for y in range(TABLE_HEIGHT):
        for x in range(TABLE_WIDTH):
            if x == cue_ball["x"] and y == cue_ball["y"]:
                print("O", end="")  # Cue ball
            elif x == target_ball["x"] and y == target_ball["y"]:
                print("X", end="")  # Target ball
            else:
                print(".", end="")  # Empty space
        print()
    print("\nUse W/A/S/D to move the cue ball and try to hit the target ball!")


def move_ball(ball, direction):
    """Move the ball in the specified direction."""
    if direction == "w" and ball["y"] > 0:
        ball["y"] -= 1
    elif direction == "s" and ball["y"] < TABLE_HEIGHT - 1:
        ball["y"] += 1
    elif direction == "a" and ball["x"] > 0:
        ball["x"] -= 1
    elif direction == "d" and ball["x"] < TABLE_WIDTH - 1:
        ball["x"] += 1


def check_collision(cue_ball, target_ball):
    """Check if the cue ball hits the target ball."""
    return cue_ball["x"] == target_ball["x"] and cue_ball["y"] == target_ball["y"]


# Game loop
while True:
    draw_table(cue_ball, target_ball)
    if check_collision(cue_ball, target_ball):
        print("You hit the target ball! Game over.")
        break

    move = input("Move (W/A/S/D): ").lower()
    if move in ["w", "a", "s", "d"]:
        move_ball(cue_ball, move)
    else:
        print("Invalid input. Please use W/A/S/D.")
    time.sleep(0.1)