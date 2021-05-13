def student_notes(name, note1, note2, note3, note4, note5):
    note_average = round(((note1 + note2 + note3 + note4 + note5) / 5),2)
    maximum = max(note1, note2, note3, note4, note5) 
    minimum = min(note1, note2, note3, note4, note5)

    if (note_average < 3):
        qualification = "low"
    elif (note_average >= 3 and note_average < 4):
        qualification = "medium"
    elif (note_average >= 4):
        qualification = "high"

    return f"The {name}'s average note is {note_average}, the maximun note is {maximum} and \
         the minimum note is {minimum}. The qualification is {qualification}"


print (student_notes("Juan", 4.5, 4.8, 2.3, 4.2, 0.5)) 
print (student_notes("María", 0.5, 2.8, 3.3, 1.2, 1.5)) 
print (student_notes("Pedro", 0.3, 1.8, 2.5, 2.2, 0.9)) 
print (student_notes("Juana", 4.5, 4.8, 4.3, 4.2, 4.5)) 