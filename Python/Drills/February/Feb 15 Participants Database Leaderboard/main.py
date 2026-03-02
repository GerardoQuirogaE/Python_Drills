import os
from leaderboard_manager import LeaderboardManager

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.abspath(
        os.path.join(base_dir,"../../../Data/Participants/participants.json")
        )

    manager = LeaderboardManager(data_path)

    manager.load_data()
    manager.sort_leaderboard()
    manager.display_leaderboard()

if __name__ == "__main__":
    main()