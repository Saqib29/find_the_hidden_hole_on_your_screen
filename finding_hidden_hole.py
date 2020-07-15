from win32api import GetSystemMetrics
import mouse
import random

print("Instruction:")
print('''       There is a hidden hole on the screen of your desktop.
      You just need to move your mouse pointer over your screen
       and search the hidden hole. Once you get the hole you will
       be Won!''')


def get_the_hole():
    screenSize = GetSystemMetrics(0), GetSystemMetrics(1)
    x = random.randint(0, screenSize[0]-80)
    y = random.randint(0, screenSize[1]-80)
    return x, y

def finding_the_hole(x,y):
    while True:
        mouse_pos = mouse.get_position()

        if mouse_pos[0] >= x and mouse_pos[0] <= (x+80) and mouse_pos[1] >= y and mouse_pos[1] <= (y+80):
            print("\n\nYou found the Hole!")
            print((x,y), (x+80,y))
            print((x,y+80),(x+80,y+80))
            print("\n\nCongratulation!\n\n")
            break
        #print(mouse_pos)



ans = input("Are you ready?(y/n)").lower()
if ans == 'y':
    print("Good Luck!")
    print("Now move your mouse pointer trhough the whole screen to find the hole.")
    x, y = get_the_hole()
    finding_the_hole(x,y)
else:
    print("To play again run the code again.")
