import re  # Import the regular expression module
import streamlit as st  # Import the Streamlit library
import secrets  # Import secrets module for secure password generation
import string  # Import string module for handling character sets

# Function to check password strength
def check_password_strength(password):
    """
    Evaluates the strength of a given password based on specified security requirements.
    
    Parameters:
        password (str): The password entered by the user.
    
    Returns:
        tuple: A message indicating password strength and a numerical score (0-4).
    """
    score = 0  # Initialize the password strength score
    feedback = []  # List to store feedback messages

    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Check if the password contains both uppercase and lowercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check if the password contains at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check if the password contains at least one special character
    if re.search(r"[ !@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Check if the password is a common weak password
    common_passwords = ["123456", "password", "qwerty", "letmein", "abc123", "111111"]
    if password.lower() in common_passwords:
        feedback.append("❌ Avoid common passwords like '123456' or 'password'.")

    # Check for repeated characters like "aaaaaa" or "111111"
    if re.search(r"(.)\1{3,}", password):  # Detects 4 or more repeated characters
        feedback.append("❌ Avoid using repeated characters (e.g., 'aaaa' or '1111').")

    # Provide feedback based on the score
    if score == 4:
        return "✅ Great! Your password is strong.", score
    elif score == 3:
        return "⚠️ Your password is moderate. Consider making it stronger.", score
    else:
        return "❌ Your password is weak - Improve it using the suggestions above.", score


# Function to generate a strong password suggestion
def generate_strong_password():
    """
    Generates a strong random password of 12 characters.

    Returns:
        str: A strong password containing uppercase, lowercase, digits, and special characters.
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for i in range(12))


# Streamlit UI
def main():
    # Set up the app title and icon
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

    # Dark mode toggle
    dark_mode = st.toggle("🌙 Dark Mode")

    # Apply dark mode styling if enabled
    if dark_mode:
        st.markdown("""
            <style>
            body { background-color: #121212; color: white; }
            .stTextInput label { color: white; }
            .stButton button { background-color: #333; color: white; }
            </style>
        """, unsafe_allow_html=True)

    # UI title
    st.title("🔐 Password Strength Meter")

    # Input field for password
    password = st.text_input("Enter your password:", type="password")

    # Real-time validation
    if password:
        result, score = check_password_strength(password)

        # Display result message
        st.write(result)

        # Display password strength as a progress bar
        progress = st.progress(score * 25)  # Each level (0-4) represents 25% of the bar

        # Show improvement suggestions if the password is weak
        if score < 3:
            st.warning(f"🔹 Suggested Strong Password: {generate_strong_password()}")

# Run the application
if __name__ == "__main__":
    main()
