Automated Web Portal Bot


1. Project Overview

This project is a technical demonstration inspired by the Robotic Process Automation (RPA) services provided by InnoBot Health.
Its purpose is to showcase the ability to build a "bot" that automates routine, web-based tasks, similar to those in the healthcare Revenue Cycle Management (RCM) space.

This bot uses Python and Selenium to:
Launch a web browser.
Navigate to a mock login page.
Enter credentials and submit a login form.
On a subsequent page, enter a patient ID and submit another form.
Scrape the resulting data ("Status: APPROVED") from the page.
Print the successful result to the console.



2. Core Technologies

Python 3: The core language for the automation script.
Selenium: The primary tool used for web browser automation and testing.
HTML/CSS: Used to create the simple, local mock web pages (login.html, patient_status.html) that the bot interacts with.



3. Project Structure

Your project folder should contain the following files:

```bot.py```: The main Python script that contains the automation logic.
```login.html```: The mock "Front Door" login page.
```patient_status.html```: The mock "Secret Room" portal page.
 

 
4. Setup and Installation

Before running the bot, you will need to set up the environment.

Prerequisites
Python 3
Google Chrome (browser)
ChromeDriver

Important: Your chromedriver version must match your Google Chrome browser version.
Place the chromedriver (or chromedriver.exe for Windows) executable in the same folder as bot.py.
Install Python Libraries
Open your terminal or command prompt.
Navigate to the project folder (e.g., cd Desktop/MyBotProject).
Install the required libraries using the requirements.txt file:
```
pip install -r requirements.txt
```



5. How to Run

After completing the setup, you can run the bot.
Make sure your chromedriver executable is in the same folder as bot.py.
From your terminal (while inside the project folder), run the following command:
```
python bot.py
```


You will see a new Chrome window open and perform the login and status check steps automatically. The terminal will print the bot's progress and, finally, the success message: ```SUCCESS!: 'Status: APPROVED'. ```

Author: Sasanka Hemakumara

