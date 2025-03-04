import requests
import json

# search categories procedure function
def search_category(search_data):
	# loop through category and display results
	index = 0
	for item in search_data["items"]:
		title = item.get("title", "N/A")
		address = item.get("address", {}).get("label", "N/A")
		latitude = item.get("position", {}).get("lat", "N/A")
		longitude = item.get("position", {}).get("lng", "N/A")
		distance = item.get("distance", "N/A")
		categories = []
		categories_data = item.get("categories", [])

		for i in categories_data:
			category_name = i.get("name", "N/A")
			categories.append(category_name)

		print(f"Result #{index + 1}:- \n Title: {title} \n Address: {address} \n Cordinates: {latitude},{longitude} \n Distance: {distance} \n Categories: {categories}")
		index+=1

# request ip address, longitude and latitude of user
response = requests.get("https://ipinfo.io/json")

ip_json = response.json()
ip_address = ip_json["ip"]
location = ip_json["loc"].split(",")
latitude = location[0]
longitude = location[1]

# request user to select category and then search for places near user that fit inputed category
category = input("Enter a category (restaurant, shop, library): ").lower()
print("")

params = {
    "at": f"{latitude},{longitude}",
    "limit": 5,
    "lang": "en",
    "q": category,
    "apiKey": "cv6QrasgL-m0qIgvvQHcrhbler0t_jKgIdx43Ng9y48"
}

# call category search function
search_category(requests.get("https://discover.search.hereapi.com/v1/discover", params=params).json())

