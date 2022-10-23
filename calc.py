MidtermRawGrade = input("Midterm Grade: ")

MidtermRawGrade = float(MidtermRawGrade)

FinalRawGrade = input("Final Grade: ")

FinalRawGrade = float(FinalRawGrade)

HomeworkRawGrade = input("Homework Grade: ")

HomeworkRawGrade = float(HomeworkRawGrade)

FinalGrade = (MidtermRawGrade * 0.35) + (FinalRawGrade * 0.45) + (HomeworkRawGrade * 0.2)
print("Final grade is: ", FinalGrade)