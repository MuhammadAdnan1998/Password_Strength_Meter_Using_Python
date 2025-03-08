# 🔐 Password Strength Meter  

## Overview  
The **Password Strength Meter** is a Python-based application that evaluates the security of a password based on predefined strength criteria. It provides real-time feedback and suggestions to help users create strong passwords. This application is built using **Streamlit**, offering a modern and interactive user interface.  

## Features  
- ✅ **Strength Assessment**: Evaluates password length, character diversity, and complexity.  
- ✅ **Real-Time Feedback**: Provides instant suggestions for improvement.  
- ✅ **Common Weak Password Detection**: Identifies commonly used weak passwords.  
- ✅ **Repeated Character Check**: Warns against excessive character repetition.  
- ✅ **Dark Mode Support**: Allows users to switch to dark mode for a better visual experience.  
- ✅ **Progress Bar Visualization**: Displays password strength using a progress bar.  
- ✅ **Strong Password Generator**: Generates secure random passwords for better security.  

## Installation & Setup  

### Prerequisites  
Ensure you have **Python 3.x** installed on your system. You can check your Python version with:  
```sh
python --version
```

### Install Dependencies  
Use the following command to install the required dependencies:  
```sh
pip install streamlit
```

### Run the Application  
To launch the **Password Strength Meter**, execute:  
```sh
streamlit run password_strength_meter.py
```

## Usage  
1. **Enter a password** in the input field.  
2. **Click "Check Password Strength"** to analyze your password.  
3. The application will display:  
   - A **strength rating** (Weak, Moderate, or Strong).  
   - A **progress bar** indicating password strength.  
   - **Suggestions for improvement** if necessary.  
4. If the password is weak, a **random strong password** suggestion will be provided.  

## Example Output  

### **Weak Password**  
```
❌ Password must be at least 8 characters long.  
❌ Include both uppercase and lowercase letters.  
❌ Add at least one number (0-9).  
❌ Include at least one special character (!@#$%^&*).  
```
  
### **Strong Password**  
```
✅ Great! Your password is strong.
```

## Future Enhancements 🚀  
- 🔹 **Password Reveal Toggle**: Option to view/hide the entered password.  
- 🔹 **Copy to Clipboard**: One-click copy for generated passwords.  
- 🔹 **Customizable Password Strength Rules**: User-defined security settings.  
- 🔹 **Integration with Security APIs**: Check if a password has been compromised in data breaches.  

## Contributions  
Contributions are welcome! Feel free to fork this repository and submit a pull request with any improvements.  

## License  
This project is licensed under the **MIT License**.  

## Author  
Developed by **Muhammad Adnan** 🚀 