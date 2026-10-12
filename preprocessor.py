"""Preprocesses form responses to meet a standard format."""

def clean_data(responses):
    """Returns a normalized, deduped version of the response data."""
    cleaned = []
    for response in responses:
        cleaned.append(normalize(response))

    return remove_duplicates(cleaned)

def normalize(response):
    """Returns a normalized version of the response for easy comparison."""
    fields = response.lower().split(",")

    # Cap monograms at three letters.
    fields[-2] = fields[-2][:3].upper()

    if "green" not in fields and "pink" not in fields and "blue" not in fields:
        fields.insert(3, "green")
    
    return ",".join(fields)

def remove_duplicates(responses):
    """Returns a new list that removes any responses with repeated names."""
    num=0#stting thhis to 0 for later use
    name_list=[] #making a list of names so that I can check which names are repeated
    updated_responses=[]
    for response in responses:
        split_response=response.split(",") #splitting up responce so that name is the first index and I can just take it out
        num+=1 #making it so for every responce it adds a number for later use
        if split_response[0] in name_list:#checking if the name is already in the name list, if it is it continues, no need for that value to be present if someone already filled out their name
            continue
        else: #making sure that the name is added to the name list if it is not already in the list
            name_list.append(split_response[0]) #adding the names to the end of name_list
            updated_responses.append(response) #adds the response to the end of updated responses
    
    return updated_responses
