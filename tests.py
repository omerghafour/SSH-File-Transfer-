import unittest
import pexpect
import os

class SSHTestCase(unittest.TestCase):
    
    def test_file_copy(self):
	copy_file_using_scp()
	source = read_file_to_string("/home/joe/testcase/source/source_file.txt")
	destnition = read_file_to_string("/home/joe/testcase/destination/destination_transferred.txt")
    	self.assertTrue(compare_strings(source,destnition))


    def test_ssh_login(self):
        pp = pexpect.spawn("ssh", ["-l", "testuser", "localhost", "echo",
                                   "foo"])

        # Respond to password authentication and possible problem with hostkey.
        while True:
            ind = pp.expect([r"to continue connecting \(yes/no\)\? ",
                             "password:"], timeout=10)
            if ind == 0:
                pp.send("yes\n")
            elif ind == 1:
                pp.send("foobar\n")
                break

        # Wait for output to finish.
        pp.expect(pexpect.EOF)

        # Check that output matches what we expect, after stripping extra
        # whitespace.

        # Equality check is too brittle for the terminal...
        # self.assertEqual(pp.before.strip(), "foo")     
	self.assertTrue(pp.before.strip().endswith("foo"))
	

# HINT: For the SCP test case, you need to check that the file transferred
# ok.  You can do that by reading both files in and verifying that the
# contents match.
def read_file_to_string(path):
    if os.path.exists(path):	
    	return open(path).read()
    else:
	# When the file path  dose not exist
	return ""

# Compare content of the source and destination 
def compare_strings(str1, str2):
    if str1 == str2: 
	return True
    else:
	return False

# Copy files from source to destination
def copy_file_using_scp():
    create_directories_file()
    os.system("scp ~/testcase/source/source_file.txt joe@localhost:~/testcase/destination/destination_transferred.txt")


# Create directory structure and a test file with some text content
def create_directories_file():
    source = "source"
    destination = "destination"
    if not os.path.exists(source):	
	os.makedirs(source)	

    if not os.path.exists(destination):
	os.makedirs(destination)

    file = open("source/source_file.txt", "w+") 
    file.write("Some text content for the test file") 
    file.close() 

