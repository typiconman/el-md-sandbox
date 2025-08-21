import os
import unicodedata

def normalize_text(text):
    """Normalize the text to Unicode Normal Form C (NFC)."""
    return unicodedata.normalize('NFC', text)

def normalize_markdown_file(file_path):
    """Normalize a Markdown file to Unicode Normal Form C and override its contents."""
    with open(file_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    # Normalize the content
    normalized_content = normalize_text(content)
    
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(normalized_content)

def crawl_and_normalize(directory):
    """Crawl through the directory and normalize all Markdown files."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Normalizing: {file_path}")
                normalize_markdown_file(file_path)

if __name__ == "__main__":
    current_directory = os.getcwd()
    crawl_and_normalize(current_directory)
    print("Normalization of all Markdown files in the directory and subdirectories is complete.")
