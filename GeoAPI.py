import requests

def show_help():
    print("\nHJÄLP – IP Geolocation Program")
    print("--------------------------------")
    print("Skriv in en IP-adress eller DNS för att få geografisk information.")
    print("Tryck bara Enter för att använda din egen IP-adress.")
    print("Skriv 'help' eller '--help' för att visa denna hjälptext.")
    print("Skriv 'quit' eller 'exit' för att avsluta.\n")

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] != "success":
            print("Kunde inte hämta data.")
            return

        lat = data.get("lat")
        lon = data.get("lon")
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"

        print(f"\nIP Information för: {ip if ip else 'Din egen IP'}")
        print(f"Land:   {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"Stad:   {data.get('city')}")
        print(f"Kords:  {lat}, {lon}")
        print(f"Karta:  {maps_link}\n")

    except Exception as e:
        print("Fel uppstod:", e)

if __name__ == "__main__":
    print("IP Geolocation Program – skriv 'help' för hjälp, 'quit' för att avsluta.\n")
    while True:
        ip = input("Ange DNS eller IP-adress: ").strip()

        if ip.lower() in ["quit", "exit"]:
            print("Avslutar programmet.")
            break
        elif ip.lower() in ["help", "--help"]:
            show_help()
        else:
            get_ip_info(ip)
