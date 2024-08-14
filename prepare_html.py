from bs4 import BeautifulSoup

def add_block_to_newletter(html_file_path, block_template, content):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Parse the div template and replace the placeholder with content
    div_soup = BeautifulSoup(block_template, 'html.parser')
    div_tag = div_soup.find('div')
    
    # Optionally, you can replace a placeholder in the block_template with content
    div_tag.string = content
    
    # Find the body tag and append the new div
    body_tag = soup.find('body')
    body_tag.append(div_tag)
    
    # Return the modified HTML as a string
    return str(soup)