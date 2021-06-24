# SendReportByEmail
This application sends reports as emails, the reports could add images or attached files. This simple 
tool uses an Excel file to configure each report (emails and templates).

In addition, using some text processing inside the [send_report](/reports.py) function one may create custom reports.

## How to configurate:

1. Install all the [needed packages](/installer) (execute installer.bat if you are on Windows)
2. Open the [setting's file](/settings/config.py) and configure the Mail Server IP. If your email server 
needs an user's account to send emails then configure *from_email* and *password* parameters otherwise you 
may continue with the next step.
3. Open the [report's settings file](/settings/file_config.xlsx) where you should identify each report to 
send by an unique identification. There you may specify users and templates:
![user_and_template_configurations](/documents/email_report_configuration.png?raw=true)

4. Edit/create the HTML template that you need in the [template's folder](/templates). Don't forget to make 
the correspondence between the Excel File and the name of the template.
5. Executing the [test file](/test.py) you should send mails to the test's users, 
and executing the [main file](/main.py) you should send mails to the user group.

## Things to consider:

1. If you setup the **sender account** (mail and password) configurations in the [setting's file](/settings/config.py), 
they will overwrite the Excel configuration.

2. If you want to make dynamic changes in the report, consider to change the [send_report function](/reports.py) using 
the replace function as is used in [here](https://github.com/Borreguin/SendReportByEmail/blob/a1d710371053cdd62cad39c07174a9a9e3e8439d/reports.py#L62)  

Finally, I hope you can use this simple tool for something more complex. If you believe there is a chance 
to add some other functionality, let me know... there is always room for improvement.