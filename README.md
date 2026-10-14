# 🔐 Password Strength Checker

A Python command-line tool that evaluates how strong a password is. It checks length, character complexity, and common weak passwords, then gives a score out of 105 with a rating and recommendations.

## Features

- Checks the minimum length (8 characters)
- Checks for uppercase letters, lowercase letters, numbers, and special characters
- Detects common passwords and common words such as `password`, `admin`, and `welcome`
- Gives an overall score with a rating: 🟢 STRONG, 🟡 MODERATE, or 🔴 WEAK
- Shows recommendations to improve a weak password
- Has an interactive menu
- Needs no external libraries (pure Python 3)

## Requirements

- Python 3.6 or newer

## Installation

```bash
git clone https://github.com/<your-username>/password-strength-checker.git
cd password-strength-checker
```

## Usage

```bash
python password_checker.py
```

You will see a menu:

```
Options:
1. Check a password
2. Generate password requirements
3. Exit
```

- **Option 1** asks for a password and shows the analysis.
- **Option 2** shows tips for creating a strong password.
- **Option 3** exits the program.

## Example Output

```
==================================================
PASSWORD STRENGTH ANALYSIS
==================================================

✔ Length OK (9 characters)

Complexity Requirements:
 ✔ Uppercase letter
 ✔ Lowercase letter
 ✔ Number
 ✔ Special character

✔ Not in common password list

==================================================
OVERALL STRENGTH: 🟢 STRONG (105/105)
==================================================

Recommendations:
```

## How the Score Works

| Check | Points |
|-------|--------|
| Length of at least 8 characters | 25 |
| Each complexity type (uppercase, lowercase, number, special) | 15 each (max 60) |
| Not a common password | 20 |
| **Maximum total** | **105** |

| Score | Rating |
|-------|--------|
| 80 or more | 🟢 STRONG |
| 60 to 79 | 🟡 MODERATE |
| Below 60 | 🔴 WEAK |

## Project Structure

```
password-strength-checker/
├── password_checker.py
└── README.md
```

## Using the Functions in Your Own Code

```python
from password_checker import check_length

print(check_length("abc"))
# (False, '✘ Too short (need at least 8 characters)')
```

## Security Note

This tool runs entirely on your computer and does not store or send passwords anywhere. It is made for learning purposes. A high score does not guarantee a password is safe, so use a password manager and unique passwords for every account.

## Contributing

Suggestions and pull requests are welcome. Ideas for improvement:

- Load a larger list of common passwords from a file
- Add checks for keyboard patterns such as `qwerty` or `asdf`
- Hide the password while typing with `getpass`

## License

This project is licensed under the MIT License.
