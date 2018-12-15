class Manager:
	def getMultipleCalendarsEvents(self, service, ids, timeMin, timeMax, 
		maxResults=2500, singleEvents=True, orderBy='startTime'):
		calendarsEvents = {}
		for calendarId in ids:
			calendarsEvents[calendarId] = self.getCalendarEvents(service = service, calendarId=calendarId, 
										timeMin=timeMin, timeMax=timeMax, maxResults=maxResults, 
										singleEvents=singleEvents, orderBy=orderBy)
		return calendarsEvents

	def getCalendarEvents(self, service, calendarId, timeMin, timeMax,
		maxResults=2500, singleEvents=True, orderBy='startTime'):
			eventsResult = service.events().list(calendarId=calendarId, timeMin=timeMin,
                                        timeMax=timeMax, maxResults=maxResults, 
                                        singleEvents=singleEvents, orderBy=orderBy).execute()	
			return eventsResult.get('items', [])	

