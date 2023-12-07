max_characters = 5  # Adjust this value to your desired limit

user_input = input(f"Enter a string (max {max_characters} characters): ")
limited_input = user_input[:max_characters]

print("Limited input:", limited_input)