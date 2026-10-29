
import pyttsx3


START_NUMBER = 50
VOICE_RATE = 150

engine = pyttsx3.init()
voices = engine.getProperty("voices")

if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)

engine.setProperty("rate", VOICE_RATE)

next_number = START_NUMBER
waiting_numbers = []



def print_header():
    print("\n" + "=" * 40)
    print("           SMART QUEUE")
    print("=" * 40)


def speak(message):
    print(f"\n  🔊 {message}\n")
    engine.say(message)
    engine.runAndWait()


def call_next():
    global next_number

    waiting_numbers.append(next_number)

    print("\n" + "-" * 40)
    print(f"  Ticket #{next_number} issued successfully!")
    print(f"  People waiting: {len(waiting_numbers)}")
    print("-" * 40)

    next_number += 1


def show_waiting_numbers():
    print("\n" + "-" * 40)
    print("           WAITING LIST")
    print("-" * 40)

    if not waiting_numbers:
        print("  No one is waiting right now.")
    else:
        for position, number in enumerate(waiting_numbers, start=1):
            print(f"  {position:>2}. Ticket #{number}")

        print("-" * 40)
        print(f"  Total waiting: {len(waiting_numbers)}")

    print("-" * 40)


def read_number():
    if not waiting_numbers:
        speak("There are no numbers waiting.")
        return

    current_number = waiting_numbers.pop(0)

    print("\n" + "-" * 40)
    print(f"  NOW SERVING: Ticket #{current_number}")
    print(f"  Remaining: {len(waiting_numbers)}")
    print("-" * 40)

    speak(f"Number {current_number}, please go to the room.")


def main():
    while True:
        print_header()

        print("  1. Get a new ticket")
        print("  2. Show waiting list")
        print("  3. Call next number")
        print("  4. Exit")

        print("-" * 40)

        choice = input("  Select an option (1-4): ").strip()

        if choice == "1":
            call_next()

        elif choice == "2":
            show_waiting_numbers()

        elif choice == "3":
            read_number()

        elif choice == "4":
            print("\n" + "=" * 40)
            print("  Smart Queue closed successfully.")
            print("  Thank you for using our system!")
            print("=" * 40 + "\n")
            break

        else:
            print("\n  [!] Invalid input. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  Smart Queue stopped.")
    finally:
        engine.stop()
