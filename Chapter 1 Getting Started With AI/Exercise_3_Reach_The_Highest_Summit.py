import math
import random


# Generate random mountains
w = [.05, random.random() / 3, random.random() / 3]
h = [1 + math.sin(1 + x / .6) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in range(100)]


def climb(x, h):
    # Keep climbing until a summit is reached
    summit = False

    while not summit:
        summit = True  # Stop unless there's a way up

        # Check five steps to the left and right
        for step in range(-5, 6):
            new_x = x + step
            if 0 <= new_x < 100 and h[new_x] > h[x]:
                x = new_x
                summit = False  # Found a higher point, keep climbing
                break  # Stop checking after finding an upward step

    return x


def main(h):
    # Start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x


if __name__ == "__main__":
    start, end = main(h)
    print(f"Start: {start}, End: {end}")
