MidtermRawGrade = input("Midterm Grade: ")

MidtermRawGrade = float(MidtermRawGrade)

FinalRawGrade = input("Final Grade: ")

FinalRawGrade = float(FinalRawGrade)

HomeworkRawGrade = input("Homework Grade: ")

HomeworkRawGrade = float(HomeworkRawGrade)

LabReport = input("Lab Report Grade: ")

LabReport = float(LabReport)

FinalGrade = (MidtermRawGrade * 0.25) + (FinalRawGrade * 0.35) + (HomeworkRawGrade * 0.15) + (LabReport * 0.25)

print("Your Composited grade is: ", FinalGrade)