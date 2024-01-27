import bs4
import requests 

# "Country" : (URL,HTML_TAG)
country_newspapers = {"Germany":("https://www.deutschland.de/de",'.teaser-small__headline'),
                      "Iran":("https://www.hamshahrionline.ir/",'.title'),
                      "France":("https://www.lemonde.fr/",'.article__title-label')
                      }

def create_prompt():
    # Get Country
    country = input("What country would you like a news summary for? ")
    # Get country's URL newspaper and the HTML Tag for titles
    capitalized_country = country.capitalize()
    try:
        url,tag = country_newspapers[capitalized_country]
    except:
        print("Sorry that country is not supported!")
        return
    
    # Scrape the Website
    results = requests.get(url)
    soup = bs4.BeautifulSoup(results.text,"lxml")
    
    # Grab all the text
    country_headlines = ''
    for item in soup.select(tag)[:3]:
        country_headlines += item.getText()+'\n'
        
    prompt = "Detect the language of the news headlines below, then translate a summary of the headlines to English in a conversational tone:\n"
    return prompt + country_headlines
