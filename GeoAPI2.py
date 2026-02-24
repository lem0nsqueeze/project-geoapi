import requests

def show_help():
    print("\nHJÄLP – IP Geolocation Program")
    print("--------------------------------")
    print("Skriv in en IP-adress för att få geografisk information.")
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

        print(f"\nIP Information för: {ip if ip else 'Din egen IP'}")
        print(f"Land:   {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"Stad:   {data.get('city')}\n")

    except Exception as e:
        print("Fel uppstod:", e)

if __name__ == "__main__":
    while True:
        ip = input("Ange en IP-adress (eller skriv 'help'): ").strip()

        if ip.lower() in ["quit", "exit"]:
            print("Avslutar programmet.")
            break
        elif ip.lower() in ["help", "--help"]:
            show_help()
            # Loop continues — returns to the prompt automatically
        else:
            get_ip_info(ip)
