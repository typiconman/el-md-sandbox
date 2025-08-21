import sys
import os
import shutil
import xml.etree.ElementTree as ET
import tempfile
import subprocess

latin = 'dummy'

def process_markdown_file(source, destination):
    print(f'Sending {source} to {destination}')
    command = ['python3', '/home/sasha/Documents/cumd/cumd/cumd.py', '--html', source, destination]
    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def convert_manifest_to_html(manifest_file, output_dir):
    """Convert the XML manifest to an HTML file with links to Markdown files."""
    global latin

    # Parse the XML file
    tree = ET.parse(manifest_file)
    root = tree.getroot()
    manifest = root.find('manifest')
    head = root.find('head')
    for meta in head.findall('meta'):
        if meta.get('name') == 'latin':
            latin = meta.get('content')
        elif meta.get('name') == 'title':
            title = meta.get('content')
        elif meta.get('name') == 'publisher':
            publisher = meta.get('content')
        elif meta.get('name') == 'year':
            year = meta.get('content')
        elif meta.get('name') == 'note':
            note = meta.get('content')

    # Start building the HTML content
    html_content = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>{title}</title>\n</head>\n<body>\n'
    html_content += f'<h1>{title}</h1>\n'
    html_content += f'<h2>{publisher}: {year}</h2>\n<ul>\n'

    # Iterate through each chapter in the manifest
    # create a chapters directory first.
    os.makedirs(os.path.join(temp_dir, 'chapters'), exist_ok=True)

    for chapter in manifest.findall('chapter'):
        file_name = chapter.get('file')
        process_markdown_file(os.path.join(os.path.dirname(os.path.abspath(manifest_file)), 'chapters', file_name + '.md'), os.path.join(temp_dir, 'chapters', file_name + '.html'))
        description = chapter.get('name')
        if file_name and description:
            html_content += f'  <li><a href="chapters/{file_name}.html">{description}</a></li>\n'

    html_content += '</ul>\n'
    html_content += f'<p>Note: {note}</p></body>\n</html>'

    latin += year # this will be our output directory name

    output_file = os.path.join(output_dir, 'index.html')  # Set the output file path

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bookbuilder.py <markdown_file>")
    else:
        manifest_file = sys.argv[1]  # Input XML file

        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            convert_manifest_to_html(manifest_file, temp_dir)
            print(f"Converted '{manifest_file}' to '{temp_dir}'.")
            # Check if the output file exists
            if os.path.exists(os.path.join(temp_dir, 'index.html')):
                permanent = '/home/sasha/Documents/design/ponomar/maktabah/' + latin
                os.makedirs(permanent, exist_ok=True)  # Create the output directory if it doesn't exist
                shutil.copytree(temp_dir, permanent, dirs_exist_ok=True)  # Copy everything

                print(f"Output successfully written to: {permanent}")
            else:
                print("Output could not be created.")
