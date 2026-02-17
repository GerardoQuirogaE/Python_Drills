from leaderboard_manager import LeaderboardManager

def main():
    manager = LeaderboardManager("data/participants.json")

    manager.load_data()
    manager.sort_leaderboard()
    manager.display_leaderboard()

if __name__ == "__main__":
    main()