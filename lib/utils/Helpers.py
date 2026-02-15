# lib/utilities/helpers.py

# -------------------------
# Requirements
# -------------------------
from datetime import datetime


# -------------------------
# ID generation
# -------------------------

def generate_id(collection):
    # Generate the next available ID based on the current collection
    if not collection:
        return 1
    return max(obj.id for obj in collection) + 1