# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import EventType

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class FormDataCollect(FormAction):
    def name(self)-> Text:
        return "Form_Info"
    
    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["name","phone_num","email","addr","credit_card","cvv"]

    def slot_mapping(self) -> Dict[Text, Union[Dict, List[Dict[Text,Any]]]]:
        return {
            "name": [self.from_text()],
            "phone_num" : [self.from_entity(entity="phone_num")],
            "email" : [self.from_entity(entity="email")],
            "addr": [self.from_text()],
            "credit_card": [self.from_text()],
            "cvv": [self.from_text()]
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message("Please confirm if the information provided is correct?\nName: {0},\nPhone Number: {1},\nEmail: {2},\nCredit Card Number: {3},\nCVV {4},".format(
            tracker.get_slot("name"),
            tracker.get_slot("phone_num"),
            tracker.get_slot("email"),
            tracker.get_slot("addr"),
            tracker.get_slot("credit_card"),
            tracker.get_slot("cvv"),
        ))
        return []
