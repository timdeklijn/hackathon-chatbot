# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests


class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # =================

        response = requests.get("https://www.metaweather.com/api/location/727232/")
        data = response.json()
        temp = data["consolidated_weather"][0]["the_temp"]
        state = data["consolidated_weather"][0]["weather_state_name"]
        visibility = data["consolidated_weather"][0]["visibility"]

        utter_message = f"""
- It currently is {temp} degrees Celcius with {state}.
- The visibility is {visibility*1.6:4.2f} km
"""

        # =================

        dispatcher.utter_message(text=utter_message)

        return []
