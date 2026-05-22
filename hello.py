import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")

#start_game()

import time

def print_slow(text):
    """Prints text with a short delay for a dramatic game effect."""
    print(text)
    time.sleep(1)

def play_game():
    # Player Setup
    player_health = 100
    player_attack = 15
    inventory = ["Health Potion"]
    
    print_slow("⚔️ WELCOME TO THE SHADOW DUNGEON! ⚔️")
    name = input("Enter your hero's name: ").strip()
    print_slow(f"\nGreetings, {name}. Your quest is to defeat the Dungeon Boss.")

    # Room 1: The Encounter
    print_slow("\n--- ROOM 1: THE ANTECHAMBER ---")
    print_slow("A foul-smelling Goblin blocks your path!")
    
    monster_health = 40
    while monster_health > 0 and player_health > 0:
        print(f"\n[{name}: {player_health} HP] vs [Goblin: {monster_health} HP]")
        action = input("Choose action: (1) Attack (2) Use Potion: ").strip()
        
        if action == "1":
            damage = random.randint(10, player_attack)
            monster_health -= damage
            print(f"💥 You slash the Goblin for {damage} damage!")
        elif action == "2":
            if "Health Potion" in inventory:
                player_health = min(100, player_health + 40)
                inventory.remove("Health Potion")
                print("🧪 You drank a potion and restored 40 HP!")
            else:
                print("❌ Your inventory is empty!")
                continue
        else:
            print("❌ Invalid choice! You hesitated.")

        # Monster Attacks back if alive
        if monster_health > 0:
            monster_damage = random.randint(5, 12)
            player_health -= monster_damage
            print(f"👹 The Goblin bites you for {monster_damage} damage!")

    if player_health <= 0:
        print_slow("\n💀 You perished in the dungeon. GAME OVER.")
        return

    print_slow("\n🎉 You defeated the Goblin! You find a 'Sword Upgrade' on its body.")
    player_attack += 10  # Permanent stat boost

    # Room 2: The Boss
    print_slow("\n--- ROOM 2: THE THRONE ROOM ---")
    print_slow("The Giant Shadow Dragon awakens!")
    
    boss_health = 80
    while boss_health > 0 and player_health > 0:
        print(f"\n[{name}: {player_health} HP] vs [Dragon: {boss_health} HP]")
        action = input("Choose action: (1) Attack (2) Dodge: ").strip()
        
        if action == "1":
            damage = random.randint(15, player_attack)
            boss_health -= damage
            print(f"💥 You strike the Dragon for {damage} damage!")
        elif action == "2":
            print("🛡️ You prepare to dodge the next attack.")
            # 70% chance to dodge successfully
            if random.random() < 0.7:
                print_slow("💨 Perfect dodge! The Dragon missed completely.")
                continue
        
        # Boss Attacks
        if boss_health > 0:
            boss_damage = random.randint(12, 25)
            player_health -= boss_damage
            print(f"🔥 The Dragon breathes fire for {boss_damage} damage!")

    if player_health > 0:
        print_slow("\n🏆 VICTORY! You killed the Shadow Dragon and saved the realm!")
    else:
        print_slow("\n💀 The Dragon turned you to ash. GAME OVER.")

# Start the game loop
if __name__ == "__main__":
    play_game()
