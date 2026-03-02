from datetime import datetime

class Participant:
    def __init__(self, first_name, last_name, cash_collected,
                 good_calls, missed, rejected_calls, join_date):

        self.first_name = first_name
        self.last_name = last_name
        self.cash_collected = cash_collected
        self.good_calls = good_calls
        self.missed_calls = missed
        self.rejected_calls = rejected_calls
        self.join_date = datetime.strptime(join_date, "%Y-%m-%d")

    @property
    def total_submissions(self):
        return self.good_calls + self.missed_calls + self.rejected_calls

    def sort_key(self):
        """
        Sorting priority:
        1) Least rejected claims
        2) Most successful claims
        3) Most money earned
        4) Earliest join date
        5) Alphabetical by first name
        """
        return (
            self.rejected_calls,
            -self.good_calls,
            -self.cash_collected,
            self.missed_calls,
            self.join_date,
            self.first_name
        )

    def __repr__(self):
        return (f"{self.first_name} {self.last_name} | "
                f"${self.cash_collected} | "
                f"Good Calls: {self.good_calls} | "
                f"Bad Calls: {self.rejected_calls} | "
                f"Missed Calls: {self.missed_calls}")
