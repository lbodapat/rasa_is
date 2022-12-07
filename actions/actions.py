# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import logging
logger= logging.getLogger(__name__)

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionTestRasa(Action):

    def name(self) -> Text:
        return "action_test_rasa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # logger.info("Console log Tracker.......", tracker)
        logger.info("Console log Tracker.......", dir(tracker))
        logger.info(".........................................")
        # logger.info("Console log domain.......", domain)
        logger.info("Console log domain.......", dir(domain))
        dispatcher.utter_message(text="Testing rasa!")

        return []


