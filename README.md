# SSH-File-Transfer-

# Test Case from SSH to for an job interview 

Automating File Transfer between two Linux/Unix based instances
	

	There are several ways to automate files transfer between two Linux/Unix instances, here for simplicity we consider using:
		-Python script
		-SCP
		-Crontab
		-Linux - Debian

	Steps:
	Create a python script file ‘copy_job.py’ with below content

		import os
		def_copy_job():
		os.system(“scp ~/path/to/your/file user@host:~/path/for/destination/file

	Make a CRON schedule to execute the ‘copy_job.py’ script
		-Run crontab -e
		-Enter 00 08 * * *  python /path/to/copy_job.py
		-Save
	This will execute the script every day at 8am
		-Running the script in this state will require the user to enter the password
		-Since we are automating this process, we can effort to enter the password every time
		-We can’t store the password in the remote host (plain text) or file
		-So we need to generate private and public keys
			-ssh-keygen -t rsa
			-Enter a filename to save the key in
			-Enter a passphrase, you can leave empty if you like
			-Reenter the passphrase
			-Enter
	It will create two files (public and private key)
		-Copy your public key to the remote host
		-Use the key in your scripts and commands
	That is it. 


	Notes:
	For the test case, I used the same VM as a source and destination to copy the file.
		-A python  function to create a source, destination and a test file for our operation
		-A python function to run SCP copy commands to copy from source to destination
		-A test case to compare files in both source and destination directories after the copy.
	The test passes or fails based on the result of the compare function


