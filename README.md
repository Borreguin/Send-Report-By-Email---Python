# SendReportByEmail
This application sends reports as emails, the reports could add images or attached files.

In addition, using some text processing inside the send_report function one may create custom reports.

## How to configurate:

1. Install all the [needed packages](/installer/installer.py) (execute installer.bat if you are Windows)
2. Open the [setting's file](/settings/config.py) and configure the Mail Server IP. If your email server 
needs an user's account to send emails then configure *from_email* and *password* parameters otherwise you 
may continue with the next step.
3. Open the [report's settings file](/settings/file_config.xlsx) where you should identify each report to 
send by an unique identification. There you may specify users and templates:

![user_and_template_configurations](/documents/email_report_configuration.png?raw=true)
 