import random


def rps():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'


def is_win(player, opponent):
    # return true of the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def main():
    print(rps())


if __name__ == "__main__":
    main()
