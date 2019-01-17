f = open("demofile.txt", "r")
# r (Read), w (Write), a (Append), r+ (Read/Write)
print(f.read())  # -reads the whole file
print(f.read(5))  # -reads the first 5 characters
print(f.readline())  # -reads a whole line
print(f.readlines())  # -reads every line


f = open("demofile.txt", "a") #append to the end
f.write("\nNow the file has one more line!")

f = open("demofile.txt", "w") #write to the file
f.write("Woops! I have deleted the content!")

f = open("myfile.txt", "x") #creates the file


file = open("demofile.txt", "r")#read
file = open("demofile.txt", "w")#write
file = open("demofile.txt", "r+")#read/write
file = open("demofile.txt", "a")#append
file = open("demofile.txt", "x")#create
file.close()


try:
   f = open("samplefile.txt", "a")
   print(f.read())
except:
   print("What happened")

try:
   f = open("samplefile.txt", "a")
   print(f.read())
except IOError:
   print("What happened")

try:
   f = open("samplefile.txt", "a")
   print(f.read())
except IOError:
   print("What happened to my file")
except ArithmeticError:
   print("Don’t even try to divide by zero")

try:
   f = open("samplefile.txt", "a")
   print(f.read())
except IOError:
   print("What happened to my file")
except ArithmeticError:
   print("Don’t even try to divide by zero")
else:
   print("Success!")



import os

os.remove("demofile.txt")
os.rename("samplefile.txt", "demofile.txt")

# We can use .mkdir() to make a new directory
os.mkdir("FileIOFolder")
# We can use .rmdir() to remove an EMPTY folder
os.rmdir("FileIOFolder")
# We can use .chdir() to change the folder
os.chdir("FileIOFolder")
# We can use .getcwd() to get the current working directory
os.getcwd()


x = open("demofileOS.txt", "x")
os.remove("demofileOS.txt")

os.mkdir("DemoOSFolder")
y = open("demofileOS.txt", "x")
os.remove("demofileOS.txt")
os.rmdir("DemoOSFolder")

f = open("demofileOS.csv", "r")
print(f.read())


try:
   f = open("samplefile.csv", "r")
   print(f.read())
except:
   print("ERROR")


1976, Chevrolet, Impala
2002, Mini, Cooper
1981, Ford, Bronco

list1 = []
list1.append()

f.write("\n" + str(name) + ", " + str(score))



# ask if wanting to create existing account or make new one
# ask if want to message or read messages
# ask who you want to message (if don't exist error)
# save message in a .txt for person to see
# randomly encrypt message with the users password

def log_out_account():
   log_out = input("do you want to log out: yes_1 or no_2  ")
   while log_out != "1" and log_out != "2":  # defencive coding
      print("error")
      log_out = input("do you want to log out: yes_1 or no_2  ")
   if log_out == "1":
      return program_log_out + 1
   elif log_out == "2":
      return program_log_out + 0