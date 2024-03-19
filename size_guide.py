# Guide to help the user to pick a right size while online shopping
print("Size guide")

# Default is centimeters, this code will convert the values into inches:
def convert_cm_to_inches(self, value):
    return value * 0.393701

# Creating a dictionary for user data:
user_data = {
    1: {'Userame': 'wilma', 'Password': 'wilma12345', 'Email address': 'wilma@wilma.wilma', 'Measurements': []},
    2: {'Userame': 'test', 'Password': 'test123', 'Email address': 'test@gmail.com', 'Measurements': []},
    3: {'Userame': 'test2', 'Password': 'test1232', 'Email address': 'test2@gmail.com', 'Measurements': []}
}

# Class to manage user creation, login, and storing user objects.
class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, email):
        if username in self.users:
            print("Username already exists.")
            return None
        new_user = User(username, email)
        self.users[username] = new_user
        print(f"User {username} created.")
        return new_user

    def get_user(self, username):
        return self.users.get(username, None)
    
def main():
    user_manager = UserManager()
    current_user = None
    
    while True:
        if not current_user:
            action = input("Choose action: sign in (si), create account (ca), or quit (q): ").lower()
            if action == "q":
                break
            elif action == "si":
                username = input("Username: ")
                current_user = user_manager.get_user(username)
                current_user = username
                print(current_user)
                if not current_user:
                    print("User not found.")
                    continue
            elif action == "ca":
                username = input("Choose a username: ")
                email = input("Email: ")
                current_user = user_manager.create_user(username, email)
        else:
            print(f"\nWelcome, {current_user.username}.")
            action = input("Choose action: update measurements (um), shop garments (sg), make order (mo), sign out (so): ").lower()
            if action == "so":
                current_user.sign_out()
                current_user = None
            elif action == "um":
                current_user.update_measurements()
            elif action == "ab":
                item = input("Enter item to add to basket: ")
                current_user.add_to_basket(item)
            elif action == "mo":
                current_user.make_order()

# Class to hold user information and measurements:
class User:
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.measurements = {}
        self.basket = []
    
    while True:
        user_choice_measurement = input("Please choose centimeters or inches (cm/in) ").lower().strip()
        user_choice_garment = input("Please choose a garment for which you would like to check the correct size (top/bottom/dress): ").lower().strip()
        bust_measurement = 0
        waist_measurement = 0
        hip_measurement = 0

            # user input to choose the type of clothing
        if user_choice_garment == "top":
            print("Please enter your measurements to find the right size for your top.")
            bust_measurement = float(input("Bust: "))
            waist_measurement = float(input("Waist: "))
        elif user_choice_garment == "bottom":
            print("Please enter your measurements to find the right size for your bottom.")
            waist_measurement = float(input("Waist: "))
            hip_measurement = float(input("Hips: "))
        elif user_choice_garment == "dress":
            print("Please enter your measurements to find the right size for your dress.")
            bust_measurement = float(input("Bust: ")) 
            waist_measurement = float(input("Waist: "))
            hip_measurement = float(input("Hips: "))
        else:
            print("Unfortunately an error occurred. Please enter a valid input (top/bottom/dress): ")
            continue  # Skip the rest of the loop and ask the user for input again

        # Convert inches to centimeters if necessary
        if user_choice_measurement == "in":
            bust_measurement = convert_cm_to_inches(bust_measurement)
            waist_measurement = convert_cm_to_inches(waist_measurement)
            hip_measurement = convert_cm_to_inches(hip_measurement)
        # the application calculates the average of two different values and the recommendation is given according to it.
        top_average = (bust_measurement + waist_measurement) / 2
        bottom_average = (waist_measurement + hip_measurement) / 2
        dress_average = (waist_measurement + hip_measurement + bust_measurement) / 3
        if user_choice_garment == "top":
            if bust_measurement <= 86:
                print("The recommended size for top is XS")
            elif bust_measurement <= 92:
                print("The recommended size for top is S")
            elif bust_measurement <= 98:
                print("The recommended size for top is M")
            elif bust_measurement <= 104:
                print("The recommended size for top is L")
            elif bust_measurement > 105:
                print("The recommended size for top is XL") 
        elif user_choice_garment == "bottom":
            if bottom_average <= 78:
                print("The recommended size for bottom is XS")
            elif bottom_average <= 84:
                print("The recommended size for bottom is S")
            elif bottom_average <= 90:
                print("The recommended size for bottom is M")
            elif bottom_average <= 96:
                print("The recommended size for bottom is L")
            elif bottom_average >= 97:
                print("The recommended size for bottom is XL") 
        elif user_choice_garment == "dress":
            if dress_average <= 80.66:
                print("The recommended size for the dress is XS")
            elif dress_average <= 86.66:
                print("The recommended size for the dress is S")
            elif dress_average <= 92.66:
                print("The recommended size for the dress is M")
            elif dress_average <= 98.66:
                print("The recommended size for the dress is L")
            elif dress_average > 98.66:
                print("The recommended size for the dress is XL")
        def update_measurements(self):
            unit = input("Do you prefer centimeters or inches? (cm/in): ").lower().strip()
            bust = float(input("Bust: "))
            waist = float(input("Waist: "))
            hips = float(input("Hips: "))
            if unit == "in":
                bust = self.convert_cm_to_inches(bust)
                waist = self.convert_cm_to_inches(waist)
                hips = self.convert_cm_to_inches(hips)
            self.measurements = {'bust': bust, 'waist': waist, 'hips': hips}
            print(f"{self.username}'s measurements updated.")
            return


        if __name__ == "__main__":
            main()
            another_clothing = input("Do you want to check the size for another clothing? (y/n): ").lower().strip()
            if another_clothing != "y":
                print("Thank you for using our size guide. Have a great day!")
