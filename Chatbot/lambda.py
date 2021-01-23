### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta
​
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
​
​
def get_investment_recommendation(risk_level):
    """
    Returns an initial investment recommendation based on the risk profile.
    """
    risk_levels = {
        "none": "100% bonds (AGG), 0% equities (SPY)",
        "very low": "80% bonds (AGG), 20% equities (SPY)",
        "low": "60% bonds (AGG), 40% equities (SPY)",
        "medium": "40% bonds (AGG), 60% equities (SPY)",
        "high": "20% bonds (AGG), 80% equities (SPY)",
        "very high": "0% bonds (AGG), 100% equities (SPY)",
    }
​
    return risk_levels[risk_level.lower()]
​
​
def validate_data(age, investment_amount, intent_request):
    """
    Validates the data provided by the user.
    """
​
    # Validate the retirement age based on the user's current age.
    # An retirement age of 65 years is considered by default.
    if age is not None:
        age = parse_int(
            age
        )  # Since parameters are strings it's important to cast values
        if age < 0:
            return build_validation_result(
                False,
                "age",
                "Your age is invalid, can you provide an age greater than zero?",
            )
        elif age >= 65:
            return build_validation_result(
                False,
                "age",
                "The maximum age to contract this service is 64, "
                "can you provide an age between 0 and 64 please?",
            )
​
    # Validate the investment amount, it should be >= 5000
    if investment_amount is not None:
        investment_amount = parse_int(investment_amount)
        if investment_amount < 5000:
            return build_validation_result(
                False,
                "investmentAmount",
                "The minimum investment amount is $5,000 USD, "
                "could you please provide a greater amount?",
            )
​
    return build_validation_result(True, None, None)
​
​
### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]
​
​
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
​
​
def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """
​
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }
​
​
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
​
​
### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """
​
    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]
​
    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        slots = get_slots(intent_request)
​
        validation_result = validate_data(age, investment_amount, intent_request)
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
    initial_recommendation = get_investment_recommendation(risk_level)
​
    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """{} thank you for your information;
            based on the risk level you defined, my recommendation is to choose an investment portfolio with {}
            """.format(
                first_name, initial_recommendation
            ),
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
    if intent_name == "RecommendPortfolio":
        return recommend_portfolio(intent_request)
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