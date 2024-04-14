import subprocess

def run_bat_file(bat_path, second_argument):
	try:
		subprocess.run([batch_file_path, second_argument], shell=True, check=True)
	except subprocess.calledProcessError as e:
		print(f"Error occured while running the batch file : ", {e})
	except FileNotFoundError:
		print(f"Batch file'{batch_file_path}' not found.")


#Example usages:
#batch_file_path = "test.bat"
#second_argument = input("Enter Payload : ")

# run_bat_file(batch_file_path, second_argument)

print("Edit this File to run the payload.")
