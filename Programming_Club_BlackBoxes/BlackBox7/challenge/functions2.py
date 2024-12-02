import subprocess

# Path to the executable
exe_path = r"C:\\Users\\USER\\Desktop\\CTF_challenges\\Programming_Club_BlackBoxes\\BlackBox7\\challenge\\secret2.exe"

# Input to send to the program
input_data = "1"
for i in range(1, 301):
    print(i)
    input_data = str(i)
    # Run the executable and provide input
    process = subprocess.Popen(
        exe_path,
        stdin=subprocess.PIPE,  # Allows sending input
        stdout=subprocess.PIPE, # Captures the output
        stderr=subprocess.PIPE  # Captures errors
    )

    # Send input to the program and get the output
    output, errors = process.communicate(input=input_data.encode('utf-8'))

    # Print the output and any errors
    #print("Output:")
    #print(output.decode('utf-8'))

    #if errors:
    #    print("Errors:")
    #    print(errors.decode('utf-8'))

    if not ("Wrong checksum" in output.decode('utf-8')):
        print(output)
        break
    