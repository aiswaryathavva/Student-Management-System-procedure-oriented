def get_valid_age(message):
    while True:
        try:
            age = int(input(message))
            if age > 0:
                return age
            print("Enter a positive age.")
        except ValueError:
            print("Please enter a valid integer.")


def get_valid_marks(message):
    while True:
        try:
            marks = int(input(message))
            if 0 <= marks <= 100:
                return marks
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")
def get_non_empty_input(message, field_name):
    while True:
        value = input(message).strip()

        if value:
            return value

        print(f"{field_name} cannot be empty.")