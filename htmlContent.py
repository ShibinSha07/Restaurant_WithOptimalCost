from bs4 import BeautifulSoup
import requests
import json

# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry


URL = "https://www.yelp.com/biz/village-the-soul-of-india-hicksville"
headers = {
    "User-Agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract Restaurant Name
    name = soup.find('h1', class_='y-css-olzveb').get_text(strip=True)
    print("Restaurant Name:", name)

    
    # Extract Address
    address = soup.find('address')
    if address:
        # Extract all text within the <address> tag
        address_text = address.get_text(separator=", ", strip=True)
        print("Address:", address_text)
    else:
        print("Address not found.")

    
    # Extract Open/Close Times
    # hours_section = soup.find('span', class_='y-css-1jz061g')
    # open_close_times = [hour.get_text(strip=True) for hour in hours_section]
    hours_section = soup.find('span', class_='y-css-qavbuq')
    open_close_times = [hour.get_text(strip=True) for hour in hours_section]
    print("Open/Close Times:", open_close_times)

# Replace 'html_content' with your actual HTML content

    menu_items = []
    # Find all dish containers
    dish_containers = soup.find_all('div', class_='dishWrapper__09f24__Bj2sT y-css-mhg9c5')

    for dish in dish_containers:
        # Find the name of the dish
        name_tag = dish.find('p', class_='y-css-3s36gp')
        # Find the price of the dish
        price_tag = dish.find('span', class_='price__09f24__F1T0p y-css-10rylqc')

        # Ensure both name and price exist
        if name_tag and price_tag:
            item_name = name_tag.get_text(strip=True)
            item_price = price_tag.get_text(strip=True)
            menu_items.append({"name": item_name, "price": item_price})

    print("Menu:", menu_items)


    # Store Data in Dictionary
    restaurant_data = {
        "name": name,
        "address": address,
        # "open_close_times": open_close_times,
        # "menu": menu_items
    }

    # # Save Data to JSON File
#     with open("restaurant_data.json", "w") as json_file:
#         json.dump(restaurant_data, json_file, indent=2)
    
#     print("Data saved to restaurant_data.json")
# else:
#     print(f"Failed to fetch page. Status code: {response.status_code}")


