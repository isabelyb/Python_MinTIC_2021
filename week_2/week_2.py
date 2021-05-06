def qualify (paper, carton):
    if (paper == True and carton == True):
        qualify = True
    if (paper == True and carton == False):
        qualify = False
    if (paper == False and carton == True):
        qualify = False
    if (paper == False and carton == False):
        qualify = False
    if (qualify == False):
        response = "sad face"
    if (qualify == True):
        response = "smile face"

    return f"The qualify is: {response}"

print(qualify(True, True))