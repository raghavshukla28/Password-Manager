# Password-Manager
This Password Manager application is a Python-based tool developed with the tkinter library for the graphical user interface. The program enables users to store, retrieve, and generate secure passwords for different websites, ensuring convenience and enhanced security. The passwords are stored locally in a JSON file.

Features
Password Generator
Generates a random, strong password containing letters, numbers, and special characters, which can be directly copied to the clipboard.

Save Passwords
Stores credentials (website, username, and password) in a JSON file (data.json). Existing data is updated seamlessly.

Retrieve Passwords
Allows searching for saved passwords by entering the website name. Displays the stored username and password in a dialog box.

Data Validation
Prevents saving incomplete entries by checking for empty fields.

User-Friendly Interface
Simple and intuitive design with color-coded buttons for different functions.

Requirements
Python 3.x
Required Python Modules:
tkinter (standard library)
pyperclip (clipboard handling)
json (for data storage)
random (for password generation)
How to Use
Clone the Repository
Clone this project or download the code files.

Install Required Module
Install pyperclip if not already available:

bash
Copy code
pip install pyperclip
Run the Application
Execute the script by running:

bash
Copy code
python password_manager.py
Features Usage

Enter the website name and username in the respective fields.
Click Generate Password to generate a random password.
Click Add to save the data into the JSON file.
Use the Search button to retrieve saved credentials for a specific website.
File Details
password_manager.py: The main application script.
data.json: Stores saved passwords in JSON format. Automatically created upon saving passwords if it does not exist.
logo.png: Application logo displayed in the GUI.
Customization
Default Email/Username
Update the email_entry.insert() line to set a preferred default username/email.

Design
Modify colors, fonts, and layout by editing the window.config() and Label/Button parameters.

Notes
This application stores passwords locally without encryption. It is recommended to implement encryption for higher security.
Ensure data.json is not publicly accessible.
Contact
Feel free to reach out for suggestions or queries.
