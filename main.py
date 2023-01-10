command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Start the car!")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("Stop the car")
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to quit program
        """)
    elif command == "quit":
        break
    else:
        print("We don't understand this!")
