"""
In this program, you start by either signing in with a previously created account or creating an account.
If you choose to create an account you enter a username and a password then the program checks to see if it has
already been taken.  If not it stores and hashes your password and stores a plain text username in separate files.
It also creates a .txt file for you to receive messages from other users. then you get logged in. If you choose to
log in with a previously made account it checks to see if the username exists and then hashes the password and
checks to see if it exists with the username. If everything matches then you log in. When you log in you can message
another user, read messages sent to you and you are given the option to log out. If you choose to message someone
it asks whom you want to message. It then checks with its file for usernames to check if it exists. If it does then
it lets you write a title and a main message. Then it appends the message with who sent it, a time stamp and other
formatting to the user you are messagings read file. If you choose to read your messages the program opens the text
file with your username on it and prints all the messages. Then you get an option to clear your inbox and if you
press yes it wipes the text file of all the messages. If you choose to log out it asks you to confirm then if you do
it asks if you want to send the session. If you don't it logs you out and takes you back to the sign in menu. If
you do end the session it ends the program.
"""

import os, sys
import time
import datetime
import hashlib


def sign_in():  # this function is used when signing in and creating an account
    temp_list = []
    username = input("enter username  ")
    temp_list.append(username)
    password = input("enter password  ")
    temp_list.append(password)  # the function adds the inputs to the list to return
    return temp_list


restart = 1
while restart == 1:
    ts = datetime.datetime.now()  # defines the variable that is used as a time stamp
    program_log_out = 1  # defines variables in case you don't end the session
    log_in_success = 0
    current_user = ""

    while log_in_success == 0:
        file1 = ""
        file2 = ""

        account_selection = input("sign in with preexisting account _1 or create new account _2")  # input for log in or create account
        while account_selection != "1" and account_selection != "2":  # defencive coding
            print("error")
            account_selection = input("sign in with preexisting account _1 or create new account _2")
        try:  # opens the files to read to see if a username exists and write new usernames and passwords
            file1 = open("passwordsave.txt", "r+")
            file2 = open("usernamesave.txt", "r+")
        except IOError:
            print("error 404 / files not found")  # defencive coding

        if account_selection == "1":
            temp_list = sign_in()  # calls the function
            account_username = temp_list[0]  # the first part of the list is the username input
            current_user = account_username  # sets the current user as the input
            hasher = hashlib.md5()  # the hasher import is called
            hasher.update(temp_list[1].encode('utf-8'))  # the hasher is hashing the password input from the list
            account_password = hasher.hexdigest()  # the hashed password is linked to account_password string
            x = file1.read()
            if str(account_username) + ", " + str(account_password) in x:  # the program checks to see if the username and password exists together
                log_in_success = 1  # ends the loop
            else:
                print("error 404 / account not found ")

        elif account_selection == "2":
            temp_list = sign_in()  # calls the function
            new_username = temp_list[0]  # the first part of the list is the username input
            current_user = new_username  # sets the current user as the input
            new_password = temp_list[1]  # the second part of the list is the password input
            x = file1.read()  # reads the username and password save file
            y = file2.read()
            if str(new_username) + ", " + str(new_password) in x or str(new_username) in y:  # checks to see if the username exists by its self and also if the password exists too
                print("error / account already exists")
            elif new_username not in x or new_password not in x:  # if its not in the save files then it saves the information to them
                hasher = hashlib.md5()  # the hasher import is called
                hasher.update(new_password.encode('utf-8'))  # the hasher is hashing the password input from the list
                hasher.hexdigest()
                file1.write("\n" + str(new_username) + ", " + str(hasher.hexdigest()))  # the password is saved with the username
                file2.write("\n" + str(new_username))  # the username is saved
                new_file = open("newfile.txt", "x")  # craetes a new file for the user to recive messages to
                newfile = current_user + ".txt"  # creates a name for the users file with their chosen username
                os.rename("newfile.txt", str(newfile))  # renames the file with their chosen username
                print("new account saved")
                new_file.close()  # closes file
                log_in_success = 1  # ends the loop

        file1.close()  # closes file
        file2.close()

    print("")
    print(" __          __  _                          ")
    time.sleep(0.2)
    print(" \ \        / / | |                         ")
    time.sleep(0.2)
    print("  \ \  /\  / /__| | ___ ___  _ __ ___   ___ ")
    time.sleep(0.2)
    print("   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ")
    time.sleep(0.2)
    print("    \  /\  /  __/ | (_| (_) | | | | | |  __/")
    time.sleep(0.2)
    print("     \/  \/ \___|_|\___\___/|_| |_| |_|\___|")
    time.sleep(0.2)
    print("")
    print(current_user)
    print("")

    while program_log_out == 1:
        message_choice = ""
        home_choice = input("Do you want to message_1 or read messages_2 or log out_3")  # input for the users choice on what they want to do

        if home_choice == "1":
            file2 = ""
            message_choice = input("who do you want to message? ")  # takes the users input
            try:
                file2 = open("usernamesave.txt", "r")  # opens the file with saved username to read
            except IOError:
                print("error 404 / files not found")  # defencive coding
            usercheck = False
            user_file = file2.readlines()  # reads all the usernames per line and checks to see in the username exists
            for userx in user_file:
                holder = userx.strip()
                if message_choice == holder:
                    usercheck = True
                    break
            if usercheck == True:
                sendfile = str(message_choice) + ".txt"  # creats a sting with the name of the file that the user is sending to
                try:
                    writefile = open(str(sendfile), "a")  # opens the file to append to
                    title = input("input your title    ")  # takes inputs for what the user wants to message
                    message = input("input your message    ")
                    writefile.write('\n' + "From " + current_user + " " + str(ts) + '\n' + "     " + title + '\n' + message + '\n')  # append the formatted version of the users input
                    writefile.close()  # closes file
                    print("success")
                except IOError:
                    print("error 404 / user files not found")  # defencive coding

            elif message_choice not in file2:  # defencive coding
                print("error user not found")
            file2.close()

        if home_choice == "2":
            try:
                read_file = open(current_user + ".txt", "r")  # opens the currnet users message file
                print("")
                print(read_file.read())  # prints the currnet users message file
                print("")
                read_file.close()  # closes file
                clearing_input = input("would you like to clear your inbox? [y/n]")  # takes the users input
                while clearing_input != "y" and clearing_input != "n":  # defencive coding
                    print("error")
                    clearing_input = input("would you like to clear your inbox? [y/n]")
                if clearing_input == "y":
                    read_file = open(current_user + ".txt", "w")  # opens the users message file in write mode
                    read_file.write("")  # write nothing to erase the rest of the files contents
                    read_file.close()  # closes file
                    print("cleared")
                if clearing_input == "n":
                    print("ok")  # does nothing
                read_file.close()  # closes file
            except IOError:
                print("error 404 / user files not found")  # defencive coding

        if home_choice == "3":
            log_out = input("do you want to log out: yes_1 or no_2  ")  # input for logging out
            while log_out != "1" and log_out != "2":  # defencive coding
                print("error")
                log_out = input("do you want to log out: yes_1 or no_2  ")
            if log_out == "1":
                program_log_out = program_log_out + 1  # ends loop
            elif log_out == "2":
                program_log_out = program_log_out + 0  # does nothing

        elif home_choice != "1" and home_choice != "2" and home_choice != "3":  # defencive coding
            print("error")

    print("")
    print("   _____                 _ _                ")
    time.sleep(0.2)
    print("  / ____|               | | |               ")
    time.sleep(0.2)
    print(" | |  __  ___   ___   __| | |__  _   _  ___ ")
    time.sleep(0.2)
    print(" | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ ")
    time.sleep(0.2)
    print(" | |__| | (_) | (_) | (_| | |_) | |_| |  __/")
    time.sleep(0.2)
    print("  \_____|\___/ \___/ \__,_|_.__/ \__, |\___|")
    time.sleep(0.2)
    print("                                  __/ |     ")
    time.sleep(0.2)
    print("                                 |___/      ")
    print("")

    restart_input = input("end session [y/n]   ")  # input for ending the program
    while restart_input != "y" and restart_input != "n":  # defencive coding
        print("error")
        restart_input = input("end session [y/n]   ")
    if restart_input == "y":
        restart = restart + 1  # ends program
        sys.exit()  # makes sure the program ends
    if restart_input == "n":
        print("logging you out")
