# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch
import random
import os

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

    def __init__(self):
        dirname = os.path.dirname("actions")
        print("DIR NAME ",dirname)
        filename = os.path.join(dirname, './mymodel.pth')
        print("file name ",filename)
        model_checkpoint = "facebook/blenderbot-400M-distill"
        self.tokenizer = BlenderbotTokenizer.from_pretrained(model_checkpoint)
        #model
        self.load_model = BlenderbotForConditionalGeneration.from_pretrained(model_checkpoint)
        self.load_model.load_state_dict(torch.load(filename))
        self.load_model.eval()
    
    def name(self) -> Text:
        return "action_test_rasa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        back_to_conv_responses=["I am sorry, these details are not enough for a refund. Please provide the details requested accurately.",
                            "Getting back to the issue at hand.","Let's complete processing the refund and get back to this.","Back to helping you with the refund",
                            "Please let me complete my task. We can discuss this later."]

        logger.info(dir(tracker.latest_message))
        logger.info(tracker.latest_message['text'])

        # tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        # model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

        # Pre-process the input text
        input_text = tracker.latest_message['text']
        # input_ids = tokenizer.encode(input_text, return_tensors="pt")
        inputs = self.tokenizer([input_text], return_tensors="pt")
        reply_ids = self.load_model.generate(**inputs)

        # Generate a response
        # output = model.generate(input_ids, max_length=100, do_sample=True)
        # response = tokenizer.decode(output[0], skip_special_tokens=True)
        response= self.tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        print("HUGGING FACE RESPONSE", response)

        output_msg=response
        dispatcher.utter_message(text=output_msg)
        dispatcher.utter_message(text=random.choice(back_to_conv_responses))

        return []


