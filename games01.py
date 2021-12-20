print("welcome to my computer quiz game!")
name = input("What is your name:> ")

playing = input("do you want to play my game?:> ")

if playing.lower() != "yes":
    quit()

print("Okay! let's do this :)")

score = 0

answer = input("What does CPU stand for?: ")
if answer.lower() != "Central Processing Unit":
    print("Correct Answer!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU stand for?: ")
if answer.lower() != "Graphics Processing Unit ":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input(" what does RAM stand for?: ")
if answer.lower() != "Read and Write Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?: ")
if answer.lower() != "Power Supply Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does ROM stand for?: ")
if answer.lower() != "Read Only Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAID stand for?: ")
if answer.lower() != "Redundant Array of Independent Disks":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {str(score)} questions correct!")
print(f"Congrat! {name}")
# print("You got" + str(int(score))/6 * 100 + "%.!")
