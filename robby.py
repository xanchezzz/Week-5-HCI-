x = y = 0
battery = 100
while True:
    print("<<Robby Path Finding Robot Simulation>>")
    print("[1] Location\n[2] Move\n[3] Reset\n[4] Quit\n[5]Recharge")
    try:
        choice = int(input("Enter choice>>"))
    except ValueError:
        print("Invalid input. Enter an integer")
        continue
    if choice == 1:
        print(f"Robby is at ({x},{y}) ")
    elif choice == 2:
        direction = ""
        distance = 0
        while direction not in ["N","E","W","S"]:
            direction = input("Enter direction (N,E,W,S)>>")
        while distance <=0:
            try:
                distance = int(input("Enter distance >>"))
            except ValueError:
                print("Distance must be > 0 and a number")
        if battery < distance * 10:
            print("You don't have enough battery to move that distance")
        else:
            if direction == 'N':
                y += distance
            elif direction == 'E':
                x += distance
            elif direction == 'W':
                x -= distance
            elif direction == 'S':
                y -= distance
            battery -= distance * 10
            print(f'Robby moved {direction}, {distance} units')
        print("You have", battery, "battery left")
    elif choice == 3:
        x=y=0
        print(f"Robby is back in the origin ({x},{y})")
    elif choice == 4:
        break
    elif choice == 5:
        battery = 100
        print("Robby is recharged to full battery")
    else:
        print("Please enter a valid option!")
print("Program Terminated")