# Google Calendar For Expenses
Easily calculating expenses according to events in google. For now it's simple but I'm still improving the project.

## Setting up

### Google Calendar
1. You need a google calendar account
2. At least one calendar for expenses and incomes (I like to set each source of income and expense as a calendar).
3. Add events on you calendars according to expenses and incomes. Make sure that its title ends with "$" plus the value like "rent - $100.20"
4. That's It!

### Your machine
1. Clone this repo `git clone https://github.com/gabrielBlankenburg/google-calendar-for-expenses`
2. Open it `cd google-calendar-for-expenses/`
3. Add the config file `mv Config/Calendar.py.example Config/Calendar.py`
4. Replace the values of Config/Calendar.py with your calendar income and expenses ids. If you don't know the calendar id just go to the settings of you calendar and at the section "Integrate Calendar" there is a field "Calendar ID", just copy that email.
5. install the google api library `pip install --upgrade google-api-python-client oauth2client`

### Google Developer
Well this is step is better explained by Google itself so just go to [Google Quick Start](https://developers.google.com/calendar/quickstart/python) and follow the first step only. Download the credentials to Config/credentials.json

### Run it!
Now just `python app.py` and it will show you the available money between day 20 of last month and 21 of the next month based on your events.