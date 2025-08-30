import random
import string

# Function to generate a random key with "ABIR" included
def generate_key():
    prefix = "mr"  # static part
    number = random.randint(100, 10000)  # random number between 100 and 10000
    custom_text = "ABIR"  # fixed part you wanted
    suffix = ''.join(random.choices(string.ascii_uppercase, k=4))  # random 4 letters
    tool_tag = "TOOL-PAID"  # static suffix
    
    key = f"{prefix}{number}{custom_text}{suffix}.{tool_tag}"  # Format the key
    return key

# Example of generating 5 keys
for _ in range(5):
    print(generate_key())  # Correct function name
