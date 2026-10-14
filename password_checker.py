#!/usr/bin/env python3

"""
Password Strength Checker
A security tool to evaluate password strength
"""

def check_length(password):
    """Check if password meets minimum length requirement"""
    min_length = 8
    if len(password) >= min_length:
        return True, f"✔ Length OK ({len(password)} characters)"
    else:
        return False, f"✘ Too short (need at least {min_length} characters)"

def check_complexity(password):
    """Check password complexity (uppercase, lowercase, digits, special)"""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_+-=[]{};:,.<>?" for char in password)

    checks = {
        "Uppercase letter": has_upper,
        "Lowercase letter": has_lower,
        "Number": has_digit,
        "Special character": has_special
    }

    passed_checks = sum(checks.values())

    results = []
    for check, result in checks.items():
        symbol = "✔" if result else "✘"
        results.append(f" {symbol} {check}")

    return passed_checks >= 3, results, passed_checks

def check_common_passwords(password):
    """Check against common weak passwords"""
    common_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "password123", "admin", "letmein", "welcome", "monkey",
        "1234567890", "password1", "iloveyou"
    ]

    # Check exact match (case-insensitive)
    if password.lower() in [p.lower() for p in common_passwords]:
        return False, "✘ This is a commonly used password"

    # Check if password contains common words
    common_words = ["password", "admin", "welcome", "letmein", "login"]
    for word in common_words:
        if word in password.lower():
            return False, f"✘ Contains common word: '{word}'"

    return True, "✔ Not in common password list"

def calculate_strength(length_pass, complexity_score, common_pass):
    """Calculate overall password strength score"""
    score = 0

    if length_pass:
        score += 25

    score += complexity_score * 15  # 15 points per complexity check

    if common_pass:
        score += 20

    # Determine strength level
    if score >= 80:
        return "STRONG", score, "🟢"
    elif score >= 60:
        return "MODERATE", score, "🟡"
    else:
        return "WEAK", score, "🔴"

def check_password_strength(password):
    """Main function to check password strength"""
    print("\n" + "=" * 50)
    print("PASSWORD STRENGTH ANALYSIS")
    print("=" * 50)

    # Check length 
    length_pass, length_msg = check_length(password)
    print(f"\n{length_msg}")

    # Check complexity 
    complexity_pass, complexity_msgs, complexity_score = check_complexity(password)
    print("\nComplexity Requirements:")
    for msg in complexity_msgs:
        print(msg)

    # Check common passwords
    common_pass, common_msg = check_common_passwords(password)
    print(f"\n{common_msg}")

    # Calculate overall strength
    strength, score, icon = calculate_strength(length_pass, complexity_score, common_pass)

    print("\n" + "=" * 50)
    print(f"OVERALL STRENGTH: {icon} {strength} ({score}/100)")
    print("=" * 50)

    # Recommendations 
    print("\nRecommendations:")
    if not length_pass:
        print(" • Increase password length to at least 8 characters")
    if complexity_score < 4:
        print(" • Add missing character types for better security")
    if not common_pass:
        print(" • Avoid common words and patterns")
    if strength == "WEAK":
        print(" • Consider using a password manager")
        print(" • Use a passphrasse (e.g., 'Coffee-Morning-Sky-42!')")

    return strength, score


def main():
    """Main program loop"""
    print("=" * 50)
    print("PASSWORD STRENGTH CHECKER")
    print("Security Tool v1.0")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Check a password")
        print("2. Generate password requirements")
        print("3. Exit")

        choice = input("\nSelect option (1-3): ")

        if choice == "1":
            password = input("\nEnter password to check: ")
            if password:
                check_password_strength(password)
            else:
                print("Error: Password cannot be empty")

        elif choice == "2":
            print("\n" + "=" * 50)
            print("STRONG PASSWORD REQUIREMENTS")
            print("=" * 50)
            print("• Minimum 8 characters (12+ recommended)")
            print("• Mix of uppercase and lowercase letters")
            print("• Include numbers")
            print("• Include special characters (!@#$%^&*)")
            print("• Avoid common words and patterns")
            print("• Don't use personal information")
            print("\nExample strong password: TR0pic@l-Sunset!2024")

        elif choice == "3":
            print("\nExiting Password Strength Checker. Stay secure!")
            break

        else:
            print("Invalid option. Please select 1-3.")

if __name__ == "__main__":
    main()