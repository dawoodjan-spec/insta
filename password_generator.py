import itertools

# Words to use for generating passwords
words = ["areeba", "yasin", "ayn", "2002" , "blacklove"]

# File to save the generated passwords
output_file = "passwords.txt"

# Function to generate passwords
def generate_passwords():
    try:
        with open(output_file, "w") as file:
            # Generate combinations of different lengths (1 to 4 words)
            for r in range(1, len(words) + 1):
                for combination in itertools.permutations(words, r):
                    # Join the combination into a password
                    password = "".join(combination)
                    file.write(password + "\n")

            # Generate passwords with separators (e.g., areeba2002, ayn-yasin)
            for r in range(1, len(words) + 1):
                for combination in itertools.permutations(words, r):
                    for separator in ["", "-", "_", ".", "@"]:
                        password = separator.join(combination)
                        file.write(password + "\n") ; 

        print(f"Passwords generated and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the password generator
if __name__ == "__main__":
    generate_passwords()
