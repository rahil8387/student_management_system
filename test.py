# math_tools.py

def add(a, b):
    return a + b

# This block will ONLY run if you run `python math_tools.py` directly.
# It will NOT run if you type `import math_tools` in another file.
if __name__ == "__main__":
    print("Testing the add function...")
    result = add(5, 3)
    print(f"5 + 3 = {result}")