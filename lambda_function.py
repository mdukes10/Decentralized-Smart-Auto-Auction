import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account
from pathlib import Path
from getpass import getpass
import json as json

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")
​
def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}
​
    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }

def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]
    
def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """
​
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }

def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """
​
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }
    
def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """
​
    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }
​
    return response
    
### Intents Handlers ###
def seller_info(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """
​
    address = get_slots(intent_request)["address"]
    accidents = get_slots(intent_request)["accidents"]
    carType = get_slots(intent_request)["carType"]
    initial_value = get_slots(intent_request)["initialValue"]
    source = intent_request["invocationSource"]
​
    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        slots = get_slots(intent_request)
​
        validation_result = validate_data(address, accidents, carType, initial_value, source)
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot
​
            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )
​
        # Fetch current session attibutes
        output_session_attributes = intent_request["sessionAttributes"]
​
        return delegate(output_session_attributes, get_slots(intent_request))
​
    # Get the initial investment recommendation
    #initial_recommendation = get_investment_recommendation(risk_level)
​
    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """ thank you for your information;
            """#.format(
                #first_name, initial_recommendation
            #),
        },
    )
​
​
### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
​
    intent_name = intent_request["currentIntent"]["name"]
​
    # Dispatch to bot's intent handlers
    if intent_name == "SellCar":
        return seller_info(intent_request)
​
    raise Exception("Intent with name " + intent_name + " not supported")
​
​
### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
​
    return dispatch(event)
