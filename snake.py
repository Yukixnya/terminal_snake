import os
import time
import random
import keyboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    clear_screen()
    for row in grid:
        print(''.join(row))
    print("\nUse Arrow Keys to move. Press 'Q' to quit.")

def create_grid(rows, cols, snake, food):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        grid[0][j] = '#'
        grid[rows - 1][j] = '#'
    for i in range(rows):
        grid[i][0] = '#'
        grid[i][cols - 1] = '#'
    for x, y in snake:
        grid[x][y] = 'O'
    grid[food[0]][food[1]] = '*'
    return grid

def move_snake(snake, direction):
    head_x, head_y = snake[-1]
    if direction == 'up':
        new_head = (head_x - 1, head_y)
    elif direction == 'down':
        new_head = (head_x + 1, head_y)
    elif direction == 'left':
        new_head = (head_x, head_y - 1)
    elif direction == 'right':
        new_head = (head_x, head_y + 1)
    else:
        new_head = (head_x, head_y)
    return new_head

def place_food(rows, cols, snake):
    while True:
        food = (random.randint(1, rows - 2), random.randint(1, cols - 2))
        if food not in snake:
            return food

def main():
    rows, cols = 20, 40
    snake = [(10, 20)]
    direction = 'right'
    food = place_food(rows, cols, snake)
    score = 0

    while True:
        grid = create_grid(rows, cols, snake, food)
        print_grid(grid)
        print(f"Score: {score}")
        time.sleep(0.1)
        if keyboard.is_pressed('up') and direction != 'down':
            direction = 'up'
        elif keyboard.is_pressed('down') and direction != 'up':
            direction = 'down'
        elif keyboard.is_pressed('left') and direction != 'right':
            direction = 'left'
        elif keyboard.is_pressed('right') and direction != 'left':
            direction = 'right'
        elif keyboard.is_pressed('q'):
            print("Thanks for playing! Goodbye!")
            break

        new_head = move_snake(snake, direction)
        if (new_head[0] == 0 or new_head[0] == rows - 1 or
            new_head[1] == 0 or new_head[1] == cols - 1 or
            new_head in snake):
            print("Game Over! You crashed!")
            break

        snake.append(new_head)
        if new_head == food:
            score += 1
            food = place_food(rows, cols, snake)
        else:
            snake.pop(0)

if __name__ == "__main__":
    main()
