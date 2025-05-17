# Password Complexity Checker

## Overview

This Python script, `password_checker.py`, is a command-line tool that evaluates the strength of a password and provides feedback to the user. It checks for various criteria, including length, character types, common patterns, repetition, sequential characters, keyboard patterns, and entropy.  Essentially, it's a Password Complexity Checker.

## Features

* **Comprehensive Password Evaluation:**
    * Checks password length.
    * Checks for the presence of uppercase letters, lowercase letters, numbers, and special characters.
    * Detects common password patterns.
    * Identifies repeating characters.
    * Looks for sequential character patterns (e.g., "abc", "123").
    * Checks for common keyboard patterns (e.g., "qwerty", "asdfgh").
    * Calculates password entropy.
* **Detailed Feedback:** Provides informative messages to the user about the password's strengths and weaknesses.
* **Clear Strength Indication:** Categorizes password strength into one of the following levels:
    * Very Weak
    * Weak
    * Moderate
    * Strong
    * Very Strong
    * Excellent
* **Command-Line Interface:** Easy-to-use command-line interface for evaluating passwords.

## Code Description

### `check_password_strength_ultimate(password)`

* This is the main function that orchestrates the password strength evaluation process.
* It takes the password string as input.
* It calls various helper functions to check different aspects of the password.
* It calculates an overall score based on the results of the checks.
* It determines the password strength based on the score.
* It returns a tuple containing the password strength (string) and a list of feedback messages.

### Helper Functions

The script includes several helper functions to perform specific checks:

* `length_score(length, feedback)`: Calculates a score based on the password's length.
* `check_char_types(password, feedback)`: Checks for the presence of different character types (uppercase, lowercase, digits, special characters).
* `character_type_score(has_upper, has_lower, has_digit, has_special, feedback)`: Calculates score based on character types.
* `check_common_patterns(password, feedback)`: Checks if the password matches any common password patterns.
* `check_repetitive_chars(password, feedback)`: Checks for repeating characters in the password.
* `check_sequential_chars(password, feedback)`: Checks for sequential character patterns.
* `check_keyboard_patterns(password, feedback)`: Checks for common keyboard patterns.
* `check_entropy(password, feedback)`: Calculates the entropy of the password.
* `calculate_strength(score)`: Determines the overall password strength based on the calculated score.
* `get_password_input_enhanced()`: Gets the password input from the user.
* `main_enhanced()`: Main function to run the program.

## How to Use

1.  **Prerequisites:** Python 3.x
2.  **Run the Script:**

    ```
    python password_checker.py
    ```
3.  **Enter Password:** The script will prompt you to enter a password.
4.  **View Results:** The script will display the password strength and provide feedback messages.

## Example

Enter your password: StrongPass123!

Password Strength: Excellent

Feedback:

* Good length!
* Contains uppercase letters.
* Contains lowercase letters.
* Contains numbers.
* Contains special characters.
* Good mix of character types!

## Developed by

Yuvaprasath

