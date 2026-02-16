from datetime import datetime

class Participant:
    def __init__(self, first_name, last_name, money_earned,
                 successful_claims, rejected_claims, join_date):

        self.first_name = first_name
        self.last_name = last_name
        self.money_earned = money_earned
        self.successful_claims = successful_claims
        self.rejected_claims = rejected_claims
        self.join_date = datetime.strptime(join_date, "%Y-%m-%d")

    @property
    def total_submissions(self):
        return self.successful_claims + self.rejected_claims

    def sort_key(self):
        """
        Sorting priority:
        1) Least rejected claims
        2) Most money earned
        3) Most successful claims
        4) Earliest join date
        5) Alphabetical by first name
        """
        return (
            self.rejected_claims,
            -self.money_earned,
            -self.successful_claims,
            self.join_date,
            self.first_name
        )

    def __repr__(self):
        return (f"{self.first_name} {self.last_name} | "
                f"${self.money_earned} | "
                f"Valid: {self.successful_claims} | "
                f"Rejected: {self.rejected_claims}")
