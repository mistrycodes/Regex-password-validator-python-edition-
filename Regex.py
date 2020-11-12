

from playsound import playsound
import random
import re

count = 0
pattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
# a random sound will play from this list
soundlist = ["ramsay.wav", "ramsay2.wav", "cet.mp3", "laughing.mp3"]

print("Welcome to the regex password validator (python edition)")
print("The requirements are simple, your password must be 8 characters long, which includes upper and lower case lettering along with some numbers.")
print("feel free to change the regex to your liking, enjoy!")

task = input("please enter in your password:")

while not re.search(pattern, task):
    count += 1
    print("Your count has been added on by %d" % count)
    print("Thats not what I asked for")

    playsound(random.choice(soundlist))
    task = input("please enter in your password:")

    if count == 3:
        print("you have exceeded your attempts")
        playsound("ramsay3.mp3")
        break


else:
    print("thank you %s" % task)
    print("here are your number of attempts: %d" % count)
    playsound("borat.mp3")
