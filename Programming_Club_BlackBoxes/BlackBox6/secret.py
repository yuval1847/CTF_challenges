import os
import sys
import base64 
import re
import socket
# Get the absolute path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

def change_your_score():
    # Construct the absolute path to conf.txt using the current directory
    file_path = os.path.join(current_directory, 'admin/conf.txt')

    # Open the file in binary read mode
    with open(file_path, 'rb') as file:
        # Read the first byte
        first_byte = file.read(1)
        
        # Check if any byte was read
        if first_byte:
            # Convert the byte to decimal value and print it
            decimal_value = ord(first_byte)
            if decimal_value != 100:
                print("Opss, your score is only {}.".format(decimal_value))
                print("In order to pass to the next stage, your score needs to be 100!")
                sys.exit()
        else:
            print("File is empty or couldn't read the first byte.")            
            sys.exit()
    print("Good Score!")

def read_password(conf_file_path):
    # Read the string from the end of 'conf.txt' until the first NULL character
    with open(conf_file_path, 'rb') as conf_file:
        # Move the file pointer to the end of the file
        conf_file.seek(0, os.SEEK_END)
        file_size = conf_file.tell()

        # Start reading from the end of the file
        index = file_size - 1
        conf_file.seek(index)

        while index >= 0:
            conf_file.seek(index)
            byte = conf_file.read(1)

            if byte == b'\x00':
                break

            index -= 1

        # Read the string until the first NULL character from the end
        conf_file.seek(index + 1)  # Move to the beginning of the string
        string_from_end = conf_file.read(file_size - index - 1)

    return string_from_end.decode('utf-8')



def read_username(conf_file_path):
    chunks = []
    current_chunk = b''

# Read content from the file
    with open(conf_file_path, 'r') as file:
        content = file.read()

    chunks = []
    current_chunk = b''

    # Iterate through the content byte by byte
    for byte in content.encode('utf-8'):
        if byte == 0:
            # If a NULL byte is encountered, check if there's data in the current chunk
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = b''
        else:
            # If not a NULL byte, continue adding to the current chunk
            current_chunk += bytes([byte])

    # Decode and print the second chunk (first base64 encoded string)
    if len(chunks) >= 2:
        second_chunk = chunks[1]
        decoded_chunk = base64.b64decode(second_chunk).decode('utf-8')
        return decoded_chunk
    else:
        print("No valid second chunk found.")
        return ""

def validate_password(password, input_password):
        # Convert bytes to string and strip leading 'b' character
    input_string = password.decode('utf-8').lstrip('b')    

    # Validate the input structure using regular expressions
    pattern = r'^pass=[\w\d]+$'
    if re.match(pattern, input_string):
        # Extract 'pass' key and its value
        key, value = input_string.split('=')

        # Check if the key is 'pass' and print the value
        if key != 'pass':
            print("Input doesn't contain 'pass' key.")
            return False
        elif value != input_password:
            print(f"Wrong password was given as an input.")
            return False
        else:
            print("Good password.")
            return True
    else:
        print("Input does not match the specified structure.")
        return False
    

def parse_checksum(checksum_string):
    # Split the string to extract the hexadecimal value
    parts = checksum_string.split('=')
    
    if len(parts) == 2 and parts[0] == 'CheckSum':
        try:
            # Convert the hexadecimal value to decimal
            checksum_decimal = int(parts[1], 16)
            return checksum_decimal
        except ValueError:
            print("Invalid checksum format. Must be in the format 'CheckSum=0x...'")

    else:
        print("Invalid checksum format. Must be in the format 'CheckSum=0x...'")

    return None  # Return None if parsing fails
    
def validate_checksum(checksum, execpted_checksum):        
    # Check if checksums match
    if checksum != execpted_checksum:
        # Create a socket for UDP communication
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Define server address and port
        server_address = ('127.0.0.1', 8080)

        # Message to be sent
        message = "Incorrect checksum. Checksum calculation is incorrect.\n The checksum calculation is: the sum of all the bytes that thier value can be divided by 3 without a reminder."

        try:
            # Send UDP packet
            udp_socket.sendto(message.encode(), server_address)
            print("UDP packet sent using loopback: Incorrect checksum notification.")
        except socket.error as e:
            print(f"Error sending UDP packet: {e}")
        finally:
            udp_socket.close()
            return False
    else:
        return True

def total_sum_bytes(file_path):
        # Initialize the sum of bytes
    total_byte_sum = 0

    # Open the file in binary read mode
    with open(file_path, 'rb') as file:                        
            byte = file.read(1)
            while byte:
                # Get the byte value
                byte_value = ord(byte)
                
                # Check if the byte value is divisible by 3
                if byte_value % 3 == 0:
                    # Add the byte value to the total sum
                    total_byte_sum += byte_value                    
                byte = file.read(1)               
    return total_byte_sum


def read_checksum(conf_file_path):
       # Read content from the file
    with open(conf_file_path, 'r') as file:
        content = file.read()

    chunks = []
    current_chunk = b''

    # Iterate through the content byte by byte
    for byte in content.encode('utf-8'):
        if byte == 0:
            # If a NULL byte is encountered, check if there's data in the current chunk
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = b''
        else:
            # If not a NULL byte, continue adding to the current chunk
            current_chunk += bytes([byte])

    # Decode and return the third chunk (second base64 encoded string)
    if len(chunks) >= 3:
        third_chunk = chunks[2]  # Index 2 for the third chunk
        decoded_chunk = base64.b64decode(third_chunk).decode('utf-8')
        return decoded_chunk
    else:
        print("No valid third chunk found.")
        return ""


def login(username, input_password, user_folder, conf_file_path):        
    if not (os.path.exists(user_folder) and os.path.isdir(user_folder)):
        print(f"Error: Folder for user '{username}' does not exist.")
        sys.exit()
    elif not os.path.exists(conf_file_path):
        print(f"Error: 'conf.txt' file not found in the folder for user '{username}'.")
        sys.exit()
    else:
        with open(conf_file_path, 'rb') as conf_file:
            first_byte = conf_file.read(1)
        
        if not first_byte:
            print("Error: 'conf.txt' file is empty.")
            sys.exit()

        password = read_password(conf_file_path)
        password = base64.b64decode(password)
        if not validate_password(password, input_password):
            sys.exit()            
        conf_username = read_username(conf_file_path)            
        if conf_username == "":
            print("Username not found in conf file, parsing error")
            sys.exit()            
        elif conf_username != username:
            print("Wrong username, please make your username is the same as the folder name. not '{}'".format(conf_username))
            sys.exit()
        elif username != "admin":
            print("The user has to be admin")
            sys.exit()
        else:
            # Read content from the file
            with open(conf_file_path, 'r') as file:
                content = file.read()                                  
                if len(content) != 60:
                    print("Error: Content length is not 60 characters.")
                    sys.exit()                                            



if len(sys.argv) != 3:
    print("Error: Please provide both username and password as arguments.")
    print("Usage: python script.py <username> <password>")
    sys.exit()

        # Extract username and password from command line arguments
username = sys.argv[1]
input_password = sys.argv[2]
user_folder = os.path.join(current_directory, username)
conf_file_path = os.path.join(user_folder, 'conf.txt')


login(username, input_password, user_folder, conf_file_path)
change_your_score()
input_chehcksum = read_checksum(conf_file_path)
input_chehcksum = parse_checksum(input_chehcksum)
calculated_checksum = total_sum_bytes(conf_file_path)
result = validate_checksum(input_chehcksum, calculated_checksum)
print("Good Fucking Job!!! This wasn't easy at all...")
print("Your password for the next zip is pclub432")


