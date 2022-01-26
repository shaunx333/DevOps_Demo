# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#import requests

from rasa_sdk.events import SlotSet
from datetime import datetime, timedelta, date
import datetime
from . import database_connectivity


#
#class ActionHelloWorld(Action):
#
#    def name(self) -> Text:
#        return "action_hello_world"
#                              
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        print("Hey there u have sucessfully implemented action server")
#        dispatcher.utter_message(text="Hello World! This Shaun's action server")
#
#        return []
#    
#    
    
    
    

class ActionTime(Action):

    def name(self) -> Text:
        return "action_time_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #now = datetime.now()
        entities = tracker.latest_message['entities']
        print("The last message now is ", entities)
        now = datetime.datetime.now()
        print ("Current date and time : ")
        time=now.strftime("%I:%M %p")
        day=now.strftime("%A")
        date=now.strftime("%B %d %Y")
        month=now.strftime("%B")

        period = None
        
        for e in entities:
            if e['entity'] == "period":
                period = e['value']
                if period.casefold() == "time":
                    dispatcher.utter_message(text="The time is "+ time)
                elif period.casefold() == "date":
                    dispatcher.utter_message(text="The date is "+ date)
                elif period.casefold() == "day":
                    dispatcher.utter_message(text="The day is "+ day)
                elif period.casefold() == "month":
                    dispatcher.utter_message(text="The month is "+ month)


        return []
    
       
        
    
    
class Actiongreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #now = datetime.now()
        entities = tracker.latest_message['entities']
        print("The last message now is ", entities)
        period = None
        
        for e in entities:
            if e['entity'] == "event":
                period = e['value']
                if "morning" in period.casefold():
                    dispatcher.utter_message(text="Hey good morning ")
                elif "afternoon" in period.casefold():
                    dispatcher.utter_message(text="Hey good afternoon")
                elif "evening" in period.casefold():
                    dispatcher.utter_message(text="Hey there good evening")
        if period == None:
            dispatcher.utter_message(text="Hello there")
        
        return []
    
    
    
    
    
    
    
    
    
    
    
class ActionEntry(Action):

    def name(self) -> Text:
        return "action_book_name"
                                 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print("The last message now is ", entities)
        
        period = None
        
        for e in entities:
            if e['entity'] == "name":
                period = e['value']
        
        
       

        return [SlotSet("name", period)]
    
    
    
    
class ActionTime(Action):

    def name(self) -> Text:
        return "action_book_time"
                                 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print("The last message now is ", entities)
        
        time = None
        day = None
        
        for e in entities:
            if e['entity'] == "time":
                time = e['value']
                
        for e in entities:
            if e['entity'] == "day":
                day = e['value']
        
        def strToDay(argument):
          switcher = {
    	      "Today": -2,
	      "Tod": -2,
	      "tom": -1,
              "tomorrow": -1,
     	      "mon":0,
    	      "monday":0,
              "tuesday":1,
              "tues": 1,
              "wed": 2,
              "wednesday": 2,
              "thu": 3,
              "thursday": 3,
              "fri": 4,
              "friday": 4,
              "sat": 5,
              "saturday": 5,
              "sun": 6,
              "sunday": 6,
           }
 
          return switcher.get(argument, -2)

        def next_weekday(weekday):
	        d=date.today()
	        if weekday == -1:
		        return d+timedelta(1)
	        elif weekday == -2:
	 	        return d
	        else:
		        days_ahead = weekday - d.weekday()
		        if days_ahead <= 0:
			        days_ahead += 7
		        return d + timedelta(days_ahead)


        day = next_weekday(strToDay(day.lower()))
        day = str(day)

        
        
       

        return [SlotSet("day", day), SlotSet("time", time)]
    
    #SlotSet("day", day)
    
    
class ActionShow(Action):

    def name(self) -> Text:
        return "action_show"
                                 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Working")
        
        name = tracker.get_slot("name")
        time = tracker.get_slot("time")
        day = tracker.get_slot("day")   
        
        
        if database_connectivity.DataUpdate(name, day, time):
            dispatcher.utter_message(text=f"{name} your appointment has been booked for {day} at {time}")
        else:
            dispatcher.utter_message(text=f"Slot is already booked ")
            
       

        return []
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
