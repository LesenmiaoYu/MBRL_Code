import pyautogui
import time
import csv
import pyperclip  # Import pyperclip for clipboard management

# Initialize an empty dictionary for the value map
value_map = {}

# Read the operatorListTest.csv file
with open("operatorVersion2.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    # Enumerate through the rows and populate the dictionary
    for index, row in enumerate(csvreader, start=1):
        # Assuming each row has one operator name
        operator_name = row[0].strip()  # Strip whitespace
        value_map[index] = operator_name

# Coordinates for UI elements
coords = {
    "query_field_start": (1938, 531),  # Starting point for query field selection
    "search_button": (2490, 599),
    "result_field_start": (1539, 642),  # Starting point for results field selection
    "result_field_end": (1572, 642),    # Ending point for results field selection
    "randomSpot": (2373, 656),
}

# Clear clipboard before each iteration
def clear_clipboard():
    pyperclip.copy("")  # Clear clipboard to avoid residual data

def find_download_button():
    button_location = pyautogui.locateOnScreen('downloadButton.png')
    if button_location:
        print(f"Download button found at {button_location}")
        return pyautogui.center(button_location)  # Get the center coordinates
    else:
        print("Download button not found.")
        return None

# Ensure time.sleep() for smoothness between operations
def main():
    
    find_download_button()


    '''
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        # Print the coordinates
        print(f"Mouse position: x={x}, y={y}")
        # Sleep for a short period to avoid flooding the console
        time.sleep(0.1)
    '''

'''
    try:
        with open("output.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Name", "Result"])  # Header row

            eventsGoneThrough = 0

            for id, name in value_map.items():
                time.sleep(0.5)  # Allow the UI to stabilize

                # Step 1: Clear clipboard
                clear_clipboard()
                print("Clipboard cleared.")

                # Step 2: Click and clear the query value field
                pyautogui.click(coords["query_field_start"])  # Focus the field
                time.sleep(0.2)

                # Try clearing with drag-and-drop
                pyautogui.mouseDown(coords["query_field_start"])
                pyautogui.moveTo(coords["randomSpot"], duration=0.2)  # Drag to clear
                pyautogui.mouseUp()
                time.sleep(0.2)

                # Step 3: Type the operator name into the query field
                pyautogui.typewrite(name, interval=0.1)  # Simulate slower typing for stability
                time.sleep(0.5)  # Allow time for input to process

                # Step 4: Click the search button
                pyautogui.click(coords["search_button"])
                time.sleep(3)  # Wait for the search results to load

                # Step 5: Copy the result
                pyautogui.click(coords["result_field_start"])
                time.sleep(0.1)
                pyautogui.mouseDown()
                pyautogui.moveTo(coords["result_field_end"], duration=0.2)  # Drag to select the result field
                pyautogui.mouseUp()
                pyautogui.hotkey("ctrl", "c")  # Copy the selected text
                time.sleep(0.5)

                # Debugging: Print clipboard content
                result_value = pyperclip.paste().strip()  # Remove leading/trailing whitespace

                # Validate the result
                if result_value:
                    writer.writerow([id, name, result_value])  # Write to CSV immediately
                    eventsGoneThrough += 1
                    print(f"{eventsGoneThrough}/{len(value_map)}; Retrieved value for '{name}': {result_value}")
                else:
                    print(f"Warning: No value copied for '{name}'. Skipping.")

        print("Data saved to outputPart1.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
        '''

if __name__ == "__main__":
    print("Starting in 5 seconds. Please ensure the UI is ready.")
    time.sleep(5)  # Allow time to position your mouse or adjust UI
    main()