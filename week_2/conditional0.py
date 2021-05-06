def qualify (paper, carton):
    if (paper == True and carton == True):
        qualify = "smile face"
    else:
        qualify = "sad face"
    
    return f"The qualify is: {qualify}"

print(qualify(True, True))