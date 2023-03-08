import requests

if __name__ == '__main__':
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.38&longitude=4.64&hourly=temperature_2m"
    r = requests.get(url).json()

    hourly_temp = zip(r['hourly']['time'], r['hourly']['temperature_2m'])

    for i in hourly_temp:
        print(i)