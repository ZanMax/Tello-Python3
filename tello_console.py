from tello import Tello
from utils import print_log, banner

tello = Tello()

banner('Tello console v.0.1')

tello.send_command('command')
response = tello.get_log()
print_log(response)

while True:
    command = input("Command: ")
    if command == "help":
        print("TODO help ...")
    if command != '' and command != '\n' and command != 'help':
        command = command.rstrip()
        if command == "exit":
            break
        tello.send_command(command)
        response = tello.get_log()
        print_log(response)
