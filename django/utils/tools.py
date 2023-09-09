import unicodedata
import re

def sanitize_to_slug(string):
    # Convert string to lowercase
    string = string.lower()

    # Remove leading and trailing whitespaces
    string = string.strip()

    # Replace spaces and hyphens with underscores
    string = re.sub(r'[\s-]+', '_', string)

    # Remove diacritics (e.g., convert "é" to "e")
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')

    # Remove non-alphanumeric characters except underscores
    string = re.sub(r'[^a-z0-9_]', '', string)

    # Remove consecutive underscores
    string = re.sub(r'_{2,}', '_', string)

    # Remove leading and trailing underscores
    string = string.strip('_')

    return string
