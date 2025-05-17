import re
from collections import Counter
import math

def check_password_strength_ultimate(password):
    """
    Checks the strength of a password 
    Args:
        password (str): The password to check.

    Returns:
        tuple: A tuple containing:
            - str: A string indicating the password strength.
            - list: A list of feedback messages for the user.
    """
    score = 0
    feedback = []

    if not password:
        return "Empty", ["Password cannot be empty."]

    length = len(password)
    score += length_score(length, feedback)

    has_upper, has_lower, has_digit, has_special = check_char_types(password, feedback)
    score += character_type_score(has_upper, has_lower, has_digit, has_special, feedback)

    score += check_common_patterns(password, feedback)
    score += check_repetitive_chars(password, feedback)
    score += check_sequential_chars(password, feedback)
    score += check_keyboard_patterns(password, feedback)
    score += check_entropy(password, feedback) # Check password entropy

    strength = calculate_strength(score)
    return strength, feedback

def length_score(length, feedback):
    """Calculates score based on password length"""
    score = 0
    if length < 8:
        feedback.append("Consider making your password longer (at least 8 characters).")
    elif length >= 8:
        score += 1
        feedback.append("Good length!")
    if length >= 12:
        score += 2
        feedback.append("Very good length!")
    if length >= 16:
        score += 3  # Give more weight to very long passwords
        feedback.append("Excellent length!")
    if length >= 20:
        score += 2
        feedback.append("Superb length!")
    return score

def check_char_types(password, feedback):
    """Checks for different character types in the password"""
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[^a-zA-Z0-9\s]", password))

    if not has_upper:
        feedback.append("Consider adding uppercase letters.")
    else:
        feedback.append("Contains uppercase letters.")
    if not has_lower:
        feedback.append("Consider adding lowercase letters.")
    else:
        feedback.append("Contains lowercase letters.")
    if not has_digit:
        feedback.append("Consider adding numbers.")
    else:
        feedback.append("Contains numbers.")
    if not has_special:
        feedback.append("Consider adding special characters.")
    else:
        feedback.append("Contains special characters.")

    return has_upper, has_lower, has_digit, has_special
def character_type_score(has_upper, has_lower, has_digit, has_special, feedback):
    """Calculates score based on character types"""
    score = 0
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    unique_char_types = sum([has_upper, has_lower, has_digit, has_special])
    if unique_char_types >= 3:
        score += 2
        feedback.append("Good mix of character types!")
    if unique_char_types == 4:
        score += 3  # Give a bigger bonus for using all types
        feedback.append("Excellent mix of character types!")
    return score

def check_common_patterns(password, feedback):
    """Checks for common password patterns"""
    score = 0
    common_passwords = ["password", "123456", "qwerty", "admin", "guest", "user", "123456789"]
    if password.lower() in common_passwords:
        feedback.append("Avoid common and easily guessable passwords.")
        score -= 3 #Penalize common passwords
    return score

def check_repetitive_chars(password, feedback):
    """Checks for repeating characters in the password"""
    score = 0
    for char, count in Counter(password).items():
        if count > 2:
            score -= (count - 2)  # Penalize repeating characters
            feedback.append(f"Avoid repeating the character '{char}' {count} times.")
    return score

def check_sequential_chars(password, feedback):
    """Checks for sequential characters (e.g., "abc", "123") in the password"""
    score = 0
    for i in range(len(password) - 2):
        sub = password[i:i + 3].lower()
        if sub.isalpha() and (ord(sub[0]) + 1 == ord(sub[1]) and ord(sub[1]) + 1 == ord(sub[2])):
            score -= 2
            feedback.append("Avoid sequential letter patterns like 'abc'.")
            break
        if sub.isdigit() and (int(sub[0]) + 1 == int(sub[1]) and int(sub[1]) + 1 == int(sub[2])):
            score -= 2
            feedback.append("Avoid sequential number patterns like '123'.")
            break
    return score

def check_keyboard_patterns(password, feedback):
    """Checks for common keyboard patterns (e.g., "qwerty", "asdfgh")
    """
    score = 0
    keyboard_patterns = [
        "qwerty", "asdfgh", "zxcvbn",
        "qwertz", "asdfghj", "yxcvbnm",  # German keyboard
        "azerty", "qsdfgh", "wxcvbn",  # French keyboard
    ]
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            score -= 3
            feedback.append("Avoid common keyboard patterns.")
            break
    return score

def check_entropy(password, feedback):
    """
    Calculates the entropy of the password and provides feedback.
    Entropy is a measure of the randomness and unpredictability of the password.
    A higher entropy generally indicates a stronger password.
    """
    entropy = 0
    if not password:
        return entropy

    char_counts = Counter(password)
    total_chars = len(password)
    for count in char_counts.values():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)

    if entropy < 3:
        feedback.append("Password has low entropy.  Consider using a wider variety of characters.")
    elif entropy < 4:
        feedback.append("Password has moderate entropy.  Adding more randomness would improve strength.")
    else:
        feedback.append("Password has good entropy.")
    return entropy
def calculate_strength(score):
    """Calculates the overall password strength based on the score"""
    if score <= 0:
        return "Very Weak"
    elif score <= 3:
        return "Weak"
    elif score <= 6:
        return "Moderate"
    elif score <= 9:
        return "Strong"
    elif score <= 12:
        return "Very Strong"
    else:
        return "Excellent"

def get_password_input_enhanced():
    """Gets the password input from the user"""
    while True:
        try:
            password = input("Enter your password: ")
        except EOFError:
            print("\nNo input received. Exiting.")
            return ""
        if not password:
            print("Password cannot be empty. Please enter a password.")
        else:
            return password

def main_enhanced():
    """Main function to run the enhanced password strength checker program"""
    password = get_password_input_enhanced()
    if password == "":
        return
    strength, feedback = check_password_strength_ultimate(password)
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nFeedback:")
        for msg in feedback:
            print(f"- {msg}")

if __name__ == "__main__":
    main_enhanced()

