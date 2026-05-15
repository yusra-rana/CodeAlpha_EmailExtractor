
# Email Extractor Automation Script

import re

# Open the text file
file = open("sample.txt", "r")

# Read file content
text = file.read()

# Find all email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Create output file
output = open("emails.txt", "w")

# Write emails into file
for email in emails:
    output.write(email + "\n")

# Close files
file.close()
output.close()

# Print result
print("Email addresses extracted successfully!")
print("Saved in emails.txt")

