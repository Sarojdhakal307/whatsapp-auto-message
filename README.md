# WhatsApp Bulk Messaging Script

This script allows you to send bulk WhatsApp messages using Python and the `pywhatkit` library. It reads phone numbers from an Excel file and sends a predefined message to each contact.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `pywhatkit`
  - `pandas`
  - `openpyxl` (for reading Excel files)

You can install the required dependencies using:

```bash
pip install pywhatkit pandas openpyxl
```

## Usage

1. **Prepare the Excel file**:
   - Create an Excel file (`try.xlsx`) with a column containing phone numbers.
   - Ensure the column name matches the one used in the script (`Contact`).

2. **Modify the script**:
   - Update the `message` variable with your desired text.
   - Ensure the `country_code` is correct for your region.

3. **Run the script**:

   ```bash
   python script.py
   ```

4. **How it works**:
   - Reads the phone numbers from `try.xlsx`.
   - Uses `pywhatkit` to send WhatsApp messages.
   - Introduces a delay (5-10 seconds) between messages to prevent spam detection.

## Important Notes

- Ensure you are logged into WhatsApp Web on your default browser.
- WhatsApp Web must remain open during message transmission.
- Use responsibly to avoid account restrictions.

## Disclaimer

This script is intended for educational purposes only. 

