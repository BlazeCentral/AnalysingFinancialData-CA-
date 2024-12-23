last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
#Below features some code activties like appending lists and setting them up
subjects = ["physics","calculus","poetry","history"]
grades = [98, 97, 85, 88]
gradebook = [["physics",	98],
["calculus",	97], ["poetry",	85],["history",	88]]
gradebook.append(["computer science", 100])
gradebook.append(["visual_arts", 93])
gradebook[5][1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)


full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

