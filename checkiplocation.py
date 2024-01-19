import requests

def get_location(ip_address, api_key=None):
    url = f"https://ipinfo.io/{ip_address}/json"

    if api_key:
        url += f"?token={api_key}"

    response = requests.get(url)
    data = response.json()

    return data

def process_ip_addresses(file_path, api_key=None):
    with open(file_path, "r") as file:
        ip_addresses = [line.strip() for line in file.readlines()]

    for ip_address in ip_addresses:
        location_data = get_location(ip_address, api_key)

        print("IP-адрес:", location_data.get("ip"))
        print("Город:", location_data.get("city"))
        print("Регион:", location_data.get("region"))
        print("Страна:", location_data.get("country"))
        print("Координаты:", location_data.get("loc"))
        print("\n")

file_path = "list-of-ip.txt" 
api_key = "Your-api-key" 

process_ip_addresses(file_path, api_key)
