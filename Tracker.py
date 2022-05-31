import json
import utils
from bs4 import BeautifulSoup
from pathlib import Path
script_path = Path(__file__, '..').resolve()
with open(script_path.joinpath("config.json")) as f:
    config = json.load(f)
url_index_bases = config["url_index_bases"]


def selectCarrier(trackingNumber):
    if (trackingNumber[0:1] == "1Z"):
        track_url = url_index_bases.format(trackingNumber,"UPS")
        StartTrack(track_url)
    else: 
        track_url = url_index_bases.format(trackingNumber,"Fedex")
        StartTrack(track_url)

def GetDeliveryDateTime(soup):
    dateResult = soup.select("div > div > div:nth-child(3) > table > tr:nth-child(2) > td:nth-child(1)")
    dateSoup = BeautifulSoup(str(dateResult[0]), features="html.parser")
    date = dateSoup.contents[0].contents[0]
    TimeResult = soup.select("div > div > div:nth-child(3) > table > tr:nth-child(2) > td:nth-child(2)")
    timeSoup = BeautifulSoup(str(TimeResult[0]), features="html.parser")
    time = timeSoup.contents[0].contents[0]
    return date+time

def GetPickupDateTime(soup):
    date = soup.contents[1].contents[0].contents[0]
    time = soup.contents[1].contents[1].contents[0]
    return date+time

def StartTrack(track_url):
    response = utils.get_request(track_url)
    html = response.text
    soup = BeautifulSoup(html, features="html.parser")
    result = soup.select("div > div > div:nth-child(3) > table > tr:nth-child(2) > td:nth-child(4)")
    newSoup = BeautifulSoup(str(result[0]), features="html.parser")
    status = newSoup.contents[0].contents[0]
    if (status == "Delivered"):
        DeliverTime = GetDeliveryDateTime(soup)
    else: DeliverTime = ""
    table=soup.find_all("tr", class_="toggledItem")
    pickUpsoup = BeautifulSoup(str(table[-1:]), features="html.parser")
    PickUpTime = GetPickupDateTime(pickUpsoup)
    print(DeliverTime, PickUpTime)
    return (DeliverTime, PickUpTime)


selectCarrier("283375959163")