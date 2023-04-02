import requests
import datetime

def main():
    start = datetime.datetime.now()
    print(f"=== Start Scraping {start} ===")
    for i in range(9999):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
        try:
            r = requests.get(url, timeout=5)
            r = r.json()
            id    = r['id']
            name  = r['name']
            image = r['sprites']['front_default']
            types = r['types'][0]['type']['name']
            print(id,name,image,types)
        except:
            i = 9999
    print(f"=== End   Scraping {datetime.datetime.now()} Eraps : {datetime.datetime.now() - start} ===")

if __name__ == '__main__':
    main()
