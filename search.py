import os
import re
import sys
import unicodedata

def normalize_text(text):
    """Normalize the text by removing diacritical marks."""
    # Normalize to NFD (Normalization Form Decomposed)
    normalized = unicodedata.normalize('NFD', text)
    # Remove diacritical marks
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')

def highlight_text(line, search_string):
    """Highlight the search string in the line."""
    # Create a regex pattern for the search string
    pattern = re.compile(re.escape(normalize_text(search_string)), re.IGNORECASE)
    # Highlight the found string in the line
    return pattern.sub(f'\033[1;31m{search_string}\033[0m', normalize_text(line))

def search_markdown_files(directory, search_string):
    """Search for a given string in all Markdown files in the specified directory and its subdirectories."""
    normalized_search_string = normalize_text(search_string)
    # Compile a regex pattern for the search string
    pattern = re.compile(re.escape(normalized_search_string), re.IGNORECASE)

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, start=1):
                        normalized_line = normalize_text(line)
                        if pattern.search(normalized_line):
                            # Highlight the found string in the line
                            highlighted_line = highlight_text(line.strip(), search_string)
                            print(f"{file_path}:{line_number}: {highlighted_line}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py <search_string>")
    else:
        search_directory = os.path.dirname(os.path.abspath(__file__))
        search_term = sys.argv[1]
        search_markdown_files(search_directory, search_term)
