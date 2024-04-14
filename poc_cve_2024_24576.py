import subprocess
 

 def run_bat_file(bat_file_path, second_argument):
 	try:
 		subprocess.run([bat_file_path, second_argument], shell=True, check=True)
 	except subprocess.calledProcessError as er:
 		print(f"Error occured while running the bat file": {er})
 	except FileNotFoundError:
 		print(f"Bat file'{bat_file_path}' not found.")



 #usages:
 bat_file_path = "test.bat" # Provide the path of bat file i.e. c:\Users\lucy\Desktop\test.bat
 second_argument = input("Enter Payload : ")

 run_batch_file(bat_file_path, second_argument)
