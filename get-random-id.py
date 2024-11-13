#!/bin/python3
import random
import string

def generate_random_id():
    # Define the allowed characters (lowercase letters and numbers)
    allowed_chars = string.ascii_lowercase + string.digits
    
    # Length of the target ID (32 characters like your example)
    id_length = 32
    
    # Generate random ID
    random_id = ''.join(random.choice(allowed_chars) for _ in range(id_length))
    
    return random_id

if __name__ == "__main__":
    # Generate and print a random ID
    print("Random ID: " + generate_random_id())
