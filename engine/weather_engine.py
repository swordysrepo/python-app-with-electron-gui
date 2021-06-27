import requests
from bs4 import BeautifulSoup as bs
import sys
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# print("file is called.")
# sys.stdout.write("file is called.")
logging.info("file is called.")

# sys.stdout.write("Hello")
city = sys.argv[1]


def get_weather(place):
    try:
        logging.info("get weather function is called.")

        # sys.stdout.write("get weather function is called.")
        place = place.replace(" ", "-")
        url = "https://www.weather-forecast.com/locations/" + place + "/forecasts/latest"
        r = requests.get(url)
        logging.info(f"reply is {r}")
        #parse the message piece by piece
        x = str(r)
        x = x.replace("<","")
        x = x.replace(">","")
        x = x.replace("[","")
        x = x.replace("]","")
        x = x.lower()
        x = x.replace("response","")
        x = x.replace(" ","")
        if x == "404":
            #log message so we can read this
            logging.info(f"passed is 404 error")
        else:
            #log the message, with whitespace covered on either side.
            logging.info(f"x is : asdadadsasdasddasdas{x}asdadsadsdasdas")

        logging.info(f"content is {r.content}")
        soup = bs(r.content, "lxml")
        try: # try to split the weather variable 
            weather = soup.findAll("span", {"class": "phrase"})[0].text
        except:
            #catch the "exception" in this case . 
            weather  = f"Location {place} is invalid"
        return weather
    except Exception as e:
        logging.info("exception thrown.")
        logging.error(e)
        logging.error("error happened when getting the weather")

# city = "adsasd"
print(get_weather(city))
sys.stdout.flush()
