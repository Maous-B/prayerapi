
import requests

def main():
    link = "https://api.aladhan.com/v1/calendarByCity?city=Paris&country=France"
    responsezer = requests.get(link)
    result = responsezer.json()
    fajr = result['data'][1]['timings']['Fajr']
    dhuhr = result['data'][1]['timings']["Dhuhr"]
    asr = result["data"][1]["timings"]["Asr"]
    maghrib = result["data"][1]["timings"]["Maghrib"]
    isha = result["data"][1]["timings"]["Isha"]
    print(f"Fajr : {fajr}\nDhuhr : {dhuhr}\nAsr : {asr}\nMaghrib : {maghrib}\nIsha : {isha}")

if __name__ == "__main__":
    main()