# BMI-Calculator

Overview
This project is a BMI (Body Mass Index) Calculator that collects user information, calculates the BMI, translates it into a health status, and saves all the information in an Excel file using the openpyxl library.

Features
Collects user information (name, height, and weight).
Calculates BMI based on user input.
Translates BMI into a health status (Underweight, Normal weight, Overweight, Obesity).
Saves user information and BMI status into an Excel file.
Simple command-line interface for user interaction.
Prerequisites
Python 3.x
openpyxl library
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/bmi-calculator.git
cd bmi-calculator
Install required Python packages:

bash
Copy code
pip install openpyxl
Usage
Run the application:

bash
Copy code
python bmi_calculator.py

The script will calculate your BMI and display your health status.
Your information and BMI status will be saved in an Excel file named bmi_records.xlsx.
Code Overview
The main functionality is divided into several parts:

bmi_calculator.py
Handles user interaction, BMI calculation, status translation, and saving data to an Excel file.



