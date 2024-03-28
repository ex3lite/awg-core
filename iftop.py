import time
import subprocess


time.sleep(1)  # Pause for 1 second before repeating the loop
# Infinite loop to continuously monitor network traffic
while True:
    # Execute the iftop command and get the output
    output = subprocess.check_output(["iftop", "-n", "-N", "-t", "-s", "1"], universal_newlines=True)

    # Process the output
    lines = output.split("\n")
    for line in lines:
        print(line)  # Replace this with your own processing logic

    time.sleep(1)  # Pause for 1 second before repeating the loop