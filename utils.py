import datetime as dt
import random
import time
import logging
import requests


def get_request(url):
    headers = requests.utils.default_headers()
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    headers.update({"User-Agent": ua})

    response = requests.get(url, headers=headers, timeout=100)
    # log(response.status_code, url)
    return response


def get_date(datetime=False):

    if datetime:
        template = "{:%Y-%m-%d %H:%M:%S}"
    else:
        template = "{:%Y%m%d}"

    return template.format(dt.datetime.now())


# def log(*args):
#     logging.basicConfig(filename = "scraper.log",
#                     format="%(asctime)s %(message)s",
#                     filemode = "w",
#                     level = logging.INFO)
#     logger = logging.getLogger()    
#     logger.info(*args)
#     print(get_date(datetime=True), *args)
