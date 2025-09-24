from semantic_router import Route

MENU_INQUIRY_ALL_ROUTE = Route(
    name="MENU_INQUIRY_ALL",
    utterances=[
        "What is on the menu?",
        "Show me the menu",
        "What food do you have?",
        "What are the menu options?",
    ],
)


SPECIFIC_MENU_INQUIRY_ROUTE = Route(
    name="SPECIFIC_MENU_INQUIRY",
    utterances=[
        "Do you have any vegan options?",
        "Are there gluten-free dishes?",
        "What vegetarian meals are available?",
        "What is the price of Rice?"
        "Can you recommend me a desert?"
        "What is the most popular dish?",
        "Do you have Halal Noodles?",
        "Do you have vegan desserts?",
    ],
)

RESERVATIONS_ROUTE = Route(
    name="RESERVATIONS",
    utterances=[
        "I would like to make a reservation",
        "Can I book a table for two?",
        "I need a reservation for tonight",
        "Do you have any available tables?",
        "Can I reserve a spot for tomorrow?",
        "Is there a table available at 7 PM?",
        "Can I make a reservation for this weekend?",
    ],
)

COMPLAINTS_ROUTE = Route(
    name="COMPLAINTS",
    utterances=[
        "I want to file a complaint",
        "The food was cold",
        "My order was incorrect",
        "The service was slow",
        "I am not satisfied with my meal",
        "The restaurant was too noisy",
        "I had to wait too long for my food",
    ],
)

routes = [MENU_INQUIRY_ALL_ROUTE,SPECIFIC_MENU_INQUIRY_ROUTE,RESERVATIONS_ROUTE,COMPLAINTS_ROUTE]
