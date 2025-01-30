from bs4 import BeautifulSoup
import csv

def add_list_item(html_file):
    while True:
        new_item = input("Enter the new list item (or type 'stop' to end or 'print' turn into txt): ")
        new_item_nospace= new_item.replace(" ","")
        if new_item.lower() == 'stop':
            print("Stopping the function.")
            break
        #Text file
        elif new_item.lower() == 'print':
            # Read the HTML file
            with open('programs-to-make-work-easy\list for rob\list.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract text from the parsed HTML
            text_content = soup.get_text()

            save_location = r'D:\Users\Shaun.RBB\Documents\Aaron\visual studio\ebay listing\programs-to-make-work-easy\list for rob\output.txt'
            with open(save_location, 'w', encoding='utf-8') as file:
                file.write(text_content)

            print("HTML content has been converted to text and saved in output.txt")
        #CSV 
        elif new_item.lower() == 'print.csv':
            with open('programs-to-make-work-easy\list for rob\list.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            items = soup.find_all('li')
            csv_file = r'D:\Users\Shaun.RBB\Documents\Aaron\visual studio\ebay listing\programs-to-make-work-easy\list for rob\output.csv'

            # Write to CSV file
            with open(csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['SKU'])  # Write header
                    for item in items:
                        writer.writerow([item.text])

            print("HTML list has been converted to CSV and saved in output.csv")

        elif new_item.lower() == 'check':
            # Read the HTML file
            with open('programs-to-make-work-easy\list for rob\list.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            items = soup.find_all('li')

            # Clear spaces
            checked_items = set()
            for item in items:
                checked_text = item.get_text(strip=True).replace(" ", "")
                checked_items.add(checked_text)
            # Create a new list
            new_list = [soup.new_tag('li') for _ in checked_items]
            for tag, text in zip(new_list, checked_items):
                tag.string = text

            # Replace old ones
            ul_tag = soup.find('ul')
            ul_tag.clear()
            ul_tag.extend(new_list)

            # Makes the new html list
            with open('programs-to-make-work-easy/list for rob/list.html', 'w', encoding='utf-8') as file:
                file.write(str(soup))

            print("HTML list has been check for duplicates and all spaces deleted")

        else:
            print("Adding item to the list...")

            # Read the HTML file
            with open(html_file, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')

            # Find the first <ul> or <ol> element
            ul = soup.find(['ul', 'ol'])
            if not ul:
                print("No list found in the HTML file.")
                continue

            # Create a new <li> element
            new_li = soup.new_tag('li', attrs={'class': 'list-item'})
            new_li.string = new_item_nospace

            # Add the new <li> to the list
            ul.append(new_li)

            # Write the modified HTML back to the file
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(str(soup))

            print(f"Added '{new_item_nospace}' to the list.")

# Replace with your HTML file path
html_file = 'programs-to-make-work-easy\list for rob\list.html'

# Call the function to start the process
add_list_item(html_file)
