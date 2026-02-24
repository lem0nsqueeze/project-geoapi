import requests

def get_ip_info(ip):
	url = f"http://ip-api.com/json/{ip}"

	try:
		response = requests.get(url, timeout=5)
		data = response.json()

		if data["status"] != "success":
			print("Kunde inte hämta data.")
			return

		print(f"\n IP Information för: {ip}")
		print(f"Land: {data.get('country')}")
		print(f"Region: {data.get('regionName')}")
		print(f"Stad: {data.get('city')}")

	except Exception as e:
		print("Fel uppstod:", e)

if __name__ == "__main__":
	ip = input("Ange en IP-adress (eller lämna tom för din egen): ").strip()

	if not ip:
		ip = ""

	get_ip_info(ip)
