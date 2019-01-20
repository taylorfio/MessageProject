import os
import time
import datetime


def sign_in():
    temp_list = []
    username = input("enter username  ")
    temp_list.append(username)
    password = input("enter password  ")
    temp_list.append(password)
    return temp_list


ts = datetime.datetime.now()
program_log_out = 1
log_in_success = 0
restart = 1
current_user = ""

while restart == 1:
    while log_in_success == 0:
        file1 = ""
        file2 = ""

        account_selection = input("sign in with preexisting account _1 or create new account _2")
        while account_selection != "1" and account_selection != "2":
            print("error")
            account_selection = input("sign in with preexisting account _1 or create new account _2")
        try:
            file1 = open("passwordsave.txt", "r+")
            file2 = open("usernamesave.txt", "r+")
        except IOError:
            print("error 404 / files not found")

        if account_selection == "1":
            temp_list = sign_in()
            account_username = temp_list[0]
            current_user = account_username
            account_password = temp_list[1]
            x = file1.read()
            if str(account_username) + ", " + str(account_password) in x:
                log_in_success = 1
            else:
                print("error 404 / account not found ")

        elif account_selection == "2":
            temp_list = sign_in()
            new_username = temp_list[0]
            current_user = new_username
            new_password = temp_list[1]
            x = file1.read()
            y = file2.read()
            if str(new_username) + ", " + str(new_password) in x or str(new_username) in y:
                print("error / account already exists")
            elif new_username not in x or new_password not in x:
                file1.write("\n" + str(new_username) + ", " + str(new_password))
                file2.write("\n" + str(new_username))
                new_file = open("newfile.txt", "x")
                newfile = current_user + ".txt"
                os.rename("newfile.txt", str(newfile))
                print("new account saved")
                log_in_success = 1

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
        home_choice = input("Do you want to message_1 or read messages_2 or log out_3")

        if home_choice == "1":
            file2 = ""
            message_choice = input("who do you want to message? ")
            try:
                file2 = open("usernamesave.txt", "r")
            except IOError:
                print("error 404 / files not found")
            user_file = file2.read()

            if message_choice in user_file:
                sendfile = str(message_choice) + ".txt"
                # sendfile = open(str(sendfile), "a")
                try:
                    open(str(sendfile), "a")
                    title = input("input your title    ")
                    message = input("input your message    ")
                    final_message = '\n', "From ", current_user, ts, '\n', title, '\n', message, '\n'
                    sendfile.write(final_message)

                except IOError:
                    print("error 404 / user files not found")

            elif message_choice not in file2:
                print("error user not found")

        if home_choice == "2":
            read_file = ""
            try:
                read_file = open(current_user + ".txt")
                print(read_file.read())
                clearing_input = input("would you like to clear your inbox? [y/n]")

                if clearing_input == "y":
                    read_file.write("")  # how to clear a text file
                if clearing_input == "n":
                    print("ok")
                else:
                    while clearing_input != "y" and "n":
                        print("error")
                        clearing_input = input("would you like to clear your inbox? [y/n]")

            except IOError:
                print("error 404 / user files not found")

        if home_choice == "3":
            log_out = input("do you want to log out: yes_1 or no_2  ")
            while log_out != "1" and log_out != "2":  # defencive coding
                print("error")
                log_out = input("do you want to log out: yes_1 or no_2  ")
            if log_out == "1":
                program_log_out = program_log_out + 1
            elif log_out == "2":
                program_log_out = program_log_out + 0

        elif home_choice != "1" and home_choice != "2" and home_choice != "3":
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

    restart_input = input("end session [y/n]   ")
    if restart_input == "y":
        restart = restart + 1
    if restart_input == "n":
        program_log_out = 1
        log_in_success = 0

