from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from Services.Calendar import Start
from Services.Calendar.Events.Manager import Manager
from Services.Financial.Financial import Financial
from Formatter.Calendar import Calendar as Formatter
from Config import Calendar

def main():
    service = Start.start()

    eventManager = Manager()

    lastMonth, nextMonth = getDates(20, 21)

    income_events = eventManager.getMultipleCalendarsEvents(service, 
                        Calendar.Calendars.get('INCOME_CALENDARS'), lastMonth, nextMonth)

    expense_events = eventManager.getMultipleCalendarsEvents(service, 
                        Calendar.Calendars.get('EXPENSE_CALENDARS'), lastMonth, nextMonth)

    formatter = Formatter()

    income = []
    expenses = []
    
    for i in income_events:
        for event in income_events[i]:
            money = formatter.moneyFromCalendarEvent(event['summary'])
            income.append(money)

    for i in expense_events:
        for event in expense_events[i]:
            money = formatter.moneyFromCalendarEvent(event['summary'])
            expenses.append(money)

    financial = Financial()
    diff = financial.calculate(income=income, expenses=expenses)

    print('available money: {}'.format(diff))

def getDates(lastMonthDay=20, nextMonthDay=21):
    today = datetime.date.today()

    lastMonthDigit = today.month - 1
    lastMonthYearDigit = today.year

    if lastMonthDigit == 0:
        lastMonthDigit = 12
        lastMonthYearDigit = today.year - 1

    lastMonth = today.replace(day=lastMonthDay, month=lastMonthDigit, year=lastMonthYearDigit)

    nextMonthDigit = today.month + 1
    nextMonthYearDigit = today.year

    if nextMonthDigit == 13:
        nextMonthDigit = 1
        nextMonthYearDigit = today.year + 1

    nextMonth = today.replace(day=nextMonthDay, month=nextMonthDigit, year=nextMonthYearDigit)

    time = datetime.time(0, 0)

    lastMonth = datetime.datetime.combine(lastMonth, time).isoformat() + 'Z'
    nextMonth = datetime.datetime.combine(nextMonth, time).isoformat() + 'Z'

    return (lastMonth, nextMonth)

if __name__ == '__main__':
    main()