"""Static reference data used to keep report submissions grounded in Toronto."""

TORONTO_NEIGHBOURHOODS = [
    "Yonge-Eglinton",
    "The Annex",
    "Kensington-Chinatown",
    "Liberty Village",
    "Cabbagetown-South St. James Town",
    "Leslieville",
    "The Beaches",
    "High Park North",
    "Junction Area",
    "North York Centre",
    "Scarborough Village",
    "Etobicoke City Centre",
    "Yorkville",
    "Regent Park",
    "Distillery District",
    "Parkdale",
    "Rosedale-Moore Park",
    "Downsview",
    "Agincourt",
    "Mimico",
]

CRIME_CATEGORIES = [
    "assault",
    "break_and_enter",
    "robbery",
    "auto_theft",
    "theft",
    "vandalism",
    "shooting",
    "fraud",
    "other",
]

# Approximate bounding box for the City of Toronto, used for light validation
# of user-submitted coordinates.
TORONTO_BOUNDS = {
    "min_lat": 43.58,
    "max_lat": 43.86,
    "min_lng": -79.64,
    "max_lng": -79.12,
}
