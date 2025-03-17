import pywhatkit as kit
import pandas as pd
import time
import random

# Load Excel file
df = pd.read_excel("try.xlsx")  # Update file path as needed

message = "your message here"  # Change this message to your actual message

# Country code (change as needed)
country_code = "+977"  # Nepal

# Loop through numbers and send messages
for number in df['Contact']:  # Replace 'Contact' with your actual column name
    try:
        full_number = f"{country_code}{int(number)}"  # Ensure correct format
        
        # Send message instantly with minimum delay
        kit.sendwhatmsg_instantly(full_number, message, wait_time=3)  
        
        print(f"Message sent to: {full_number}")
        
        # Reduce delay (minimum 5-10 seconds to avoid spam detection)
        time.sleep(random.randint(5, 10))  
        
    except Exception as e:
        print(f"Failed to send message to {number}: {e}")

print("All messages sent successfully!")
