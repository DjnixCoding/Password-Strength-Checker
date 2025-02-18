def checkStrength(password):
    length = len(password)
    if length < 6:
        return "Weak: Password is too short!"
    elif length < 10:
        return "Moderate: Consider using a longer password."
    else:
        return "Strong: Good password length!"
    
if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        strength = checkStrength(password)
        if "Weak" in strength:
            print(strength, "Please enter a longer password.")
        else:
            print(strength)
            break
