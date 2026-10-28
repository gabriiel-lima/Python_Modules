import random


def gen_player_achievements(achievement: set, how_many: int) -> set:
    achievement_list = random.sample(list(achievement), how_many)
    return (set(achievement_list))


def main() -> None:
    achievements = {
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
    }

    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements(achievements, 4)
    bob = gen_player_achievements(achievements, 6)
    charlie = gen_player_achievements(achievements, 7)
    dylan = gen_player_achievements(achievements, 5)
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", dylan)
    print("\nAll distinct achievements: ", set.union(
        alice, bob, charlie, dylan)
    )
    print("\nCommom achievements: ", alice & bob & charlie & dylan)
    print("\nOnly Alice has: ", alice.difference(bob, charlie, dylan))
    print("Only Bob has: ", bob.difference(alice, charlie, dylan))
    print("Only Charlie has: ", charlie.difference(bob, alice, dylan))
    print("Only Dylan has: ", dylan.difference(bob, charlie, alice))
    print("\nAlice is missing: ", achievements.difference(alice))
    print("Bob is missing: ", achievements.difference(bob))
    print("Charlie is missing: ", achievements.difference(charlie))
    print("Dylan is missing: ", achievements.difference(dylan))


if __name__ == "__main__":
    main()
