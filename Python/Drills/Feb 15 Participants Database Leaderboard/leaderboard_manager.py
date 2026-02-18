# This is where the system goes from a simple container to a manager.

import json
# Importing Python’s built-in JSON module.
"""
This because the data is stored in: data/participants.json
JSON is just a text format for structured data.
When Python reads the file with json.load() it becomes
    [
    {
        "first_name": "Mali",
        "last_name": "Imery",
        ...
        }
    ]
Which is a list of dictionaries ready for data manupulation.
"""
from models.participant import Participant
# Importing custom class `Participants`
"""
Instead of writing everything in one giant file
(bad engineering principal because it is not scalable),
I separated:
    1. Data Model → Participant.
    2. Logic Controller → This Manager.
"""

class LeaderboardManager:
    """ 
    This class manages Loading data, Sorting, and Displaying,
    but it does not Store ranking logic (that’s in Participant)
    or Define participant structure (also Participant)
    
    """

    def __init__(self, data_path):
        """
        Constructor Function
        This will automaticaly initialize.

        If there was no constructor fucntion you coudnt have
            manager = LeaderboardManager("data/participants.json")
        because "data/participants.json" is a parameter that you
        have not defined to be able to use.

        This function will store:
            self.data_path = "data/participants.json"
            self.participants = []

        defining `self.participants = []` is inportant because 
        it initializes a list where we will later store Participant objects in. 
        """
        self.data_path = data_path
        self.participants = []

    def load_data(self):

        with open(self.data_path, "r") as file:
            raw_data = json.load(file)
            """
            Step A:
            Open the file
                "r" means read mode.
                with ensures the file closes automatically (important best practice).
            Step B:
            Load JSON
                Now raw_data = list of dictionaries as explained above.
            """
        self.participants = [
            Participant(**entry) for entry in raw_data
        ]
        """
        Step C:
        Convert dictionaries into objects
        Lets Break It Down:
            for entry in raw_data? 
                It loops over each dictionary.
                If raw_data contains 3 participants, this loop runs 3 times.
            Participant(**entry)?
                Each entry is a dictionary:
                    {
                    "first_name": "Mali",
                    "last_name": "Imery",
                    ...
                    }
                The ** operator unpacks the dictionary into keyword arguments.
                So:
                    Participant(**entry)
                Is equivalent to:
                    Participant(
                    first_name="Mali",
                    last_name="Imery",
                    ...
                )
                It matches dictionary keys to parameter names.
                Converted raw data → structured objects.
        """

    def sort_leaderboard(self):
        self.participants.sort(key=lambda p: p.sort_key())

    def display_leaderboard(self):
        """
        This function only handles presentation
        """
        print("\n PARTICIPANT'S LEADERBOARD\n")
        for rank, participant in enumerate(self.participants, start=1):
            print(f"{rank}. {participant}")

    def get_top_n_leaderboard(self, n=10):
        return self.participants[:n]
