import datetime
import time
import sys

def display_clock():
    """
    Displays a digital clock in the console that updates every second.
    Press Ctrl+C to stop the clock.
    """
    try:
        print("Starting clock... Press Ctrl+C to stop.")
        while True:
            # Get the current time
            now = datetime.datetime.now()

            # Format the time as HH:MM:SS
            current_time = now.strftime("%H:%M:%S")

            # Print the time, using '\r' to return to the beginning of the line
            # This overwrites the previous time, creating an updating effect.
            # 'end=""' prevents adding a newline character after printing.
            # 'flush=True' ensures the output is displayed immediately.
            print(f"\rCurrent Time: {current_time}", end="", flush=True)

            # Wait for 1 second before updating
            time.sleep(1)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nClock stopped.")
        sys.exit(0) # Exit the script cleanly
    except Exception as e:
        # Handle any other unexpected errors
        print(f"\nAn error occurred: {e}")
        sys.exit(1) # Exit with an error code

if __name__ == "__main__":
    # Run the clock function if the script is executed directly
    display_clock()
