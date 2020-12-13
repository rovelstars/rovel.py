import requests

API_URL = "https://api.npmjs.org"
REGISTRY_URL = "https://registry.npmjs.org"

def get_details(package_name):
	return requests.get(f"{REGISTRY_URL}/{package_name}").json()

def get_stat(package_name, start, end):
	return requests.get(f"{API_URL}/downloads/point/{start}:{end}/{package_name}").json()