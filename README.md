# Password Strength Meter 🔐

## Overview
The **Password Strength Meter** is a Python-based application that evaluates the security strength of a given password. The program uses various password security rules and provides real-time feedback to help users create stronger passwords. This project is built with **Streamlit** to offer an interactive and user-friendly experience.

## Features
- ✅ Checks password length (minimum 8 characters)
- ✅ Validates the presence of uppercase and lowercase letters
- ✅ Ensures inclusion of at least one numeric digit
- ✅ Requires at least one special character (!@#$%^&*)
- ✅ Provides instant feedback on password strength (Weak, Moderate, Strong)
- ✅ Simple and interactive **Streamlit UI**

## Installation & Setup
To run this application on your local machine, follow these steps:

### Prerequisites
Ensure you have **Python 3.x** installed. You can check your Python version by running:
```sh
python --version
```

### Install Dependencies
Use the following command to install the required dependencies:
```sh
pip install streamlit
```

### Run the Application
To launch the Password Strength Meter, execute:
```sh
streamlit run password_strength_meter.py
```

## Usage
1. Enter a password in the input field.
2. Click on the **Check Strength** button.
3. The application will analyze your password and display a **strength rating** along with **suggestions for improvement** if necessary.

## Example Output
### Weak Password:
```
❌ Password should be at least 8 characters long.
❌ Include both uppercase and lowercase letters.
❌ Add at least one number (0-9).
❌ Include at least one special character (!@#$%^&*).
```
### Strong Password:
```
✅ Strong Password!
```

## Enhancements & Future Improvements
- 🔹 **Password Generator**: Suggests a strong random password
- 🔹 **Blacklist Feature**: Blocks commonly used weak passwords
- 🔹 **Advanced Scoring System**: Assigns weighted scores for different security factors
- 🔹 **UI Enhancements**: Improve user experience with better design and visual indicators

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request with any improvements.

## License
This project is licensed under the **MIT License**.

## Author
Developed by **Muhammad Adnan** 🚀

