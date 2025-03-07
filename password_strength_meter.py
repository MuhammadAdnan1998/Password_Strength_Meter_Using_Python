import re
import streamlit as st

def check_password_strength(password):
    """
    Evaluatesthe strength of a given password based on specify security requirements.
    
    Parameters:
        password (str): The password entered by the user.
    
    Returns:
        None (Prints messages based on the password strength)
    """
    score = 0 # Initialize the password strength score
    feedback = [] # Initialize the feedback list

    # Check if the password is at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Check if the password contains both uppercase and lowercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters in your password.")
    
    # Check if the password contains at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9) to your password.")
    
    # Check if the password contains at one one special character
    if re.search(r"[ !@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*) in your password.")
    
    #Provide feedback based on the score
    if score == 4:
        return "✅ Great! Your password is strong."
    elif score == 3:
        return "⚠️ Your password is moderate. Consider making it stronger."
    else:
        return "❌ Your password is weak - Improve it using the suggestions above."

# Streamlit UI
def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter your password:", type="password")

    if st.button("Check Password Strength"):
        result = check_password_strength(password)
        st.write(result)

if __name__ == "__main__":
    main()