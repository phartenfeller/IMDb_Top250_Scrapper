from bs4 import BeautifulSoup
import requests
import os

from scraper_functions import getTitle, getLink, getRank, getAmountUsersRated, getRating, getDuration, getOriginalTitle,\
    getFSK, getRoles, getCast, getGenres, getDirectors, getWriters, getGrossWorldwide, getGrossUSA, getOpneningWeekend,\
    getBudget, CurrencySetting, detailedOutputSetting, getTS, getTSFilepath

from json_writer import appendJSON, generateJSON, writeJSON

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# Settings
## Removes Currency Symbol of Output Values
removeCurrencySymbol = True
## Only shows Title, Rank, Link and Rating in the Console
detailedOutput = True

## Output a JSON File of the Data
outputJSON = True
## Path of the JSON File
#ä IF you keep this setting the files get created in the subfolder "JSON" (which has to exist)
JSONPath = dir_path + '\\JSON\\'

def main():
    url = 'http://www.imdb.com/chart/top'

    # Open Top250 page
    page = requests.get(url)
    content = page.content

    # Setting Regions
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find("tbody", {"class": "lister-list"})
    rows = table.findChildren(['th', 'tr'])

    for row in rows:
        # Setting Regions
        titleColumn = row.find("td", {"class": "titleColumn"})
        linkText = titleColumn.find("a")['href']

        # Scrape Data
        title = getTitle(titleColumn)
        rank = getRank(linkText)
        link = getLink(linkText)
        rating = getRating(row)
        amountUsersRated = getAmountUsersRated(row)

        dateScraped = getTS()

        # Open Moviepage
        moviePage = requests.get(link)
        movieSoup = BeautifulSoup(moviePage.content, 'html.parser')

        # Setting Regions
        main = movieSoup.find("div", {"id" : "title-overview-widget"})
        titleDetails = movieSoup.find(id="titleDetails")

        # Scrape Data
        ## Details
        originalTitle = getOriginalTitle(main, title)
        fsk = getFSK(main)
        duration = getDuration(main)
        castArray = getCast(movieSoup)
        rolesArray = getRoles(movieSoup)
        genresArray = getGenres(movieSoup)
        directorArray = getDirectors(main)
        writersArray = getWriters(main)

        ## Box Office
        budget = getBudget(movieSoup)
        openingWeekend = getOpneningWeekend(titleDetails)
        grossUSA = getGrossUSA(titleDetails)
        grossWorldwide = getGrossWorldwide(titleDetails)

        if outputJSON:
            appendJSON(title, rank, link, rating, amountUsersRated, dateScraped, originalTitle, fsk, duration, castArray,
               rolesArray, genresArray, directorArray, writersArray, budget, openingWeekend, grossUSA, grossWorldwide)

def setSettings(removeCurrencySymbol, detailedOutput):
    CurrencySetting(removeCurrencySymbol)
    detailedOutputSetting(detailedOutput)

def createJSON():
    generateJSON()
    writeJSON(JSONPath, getTSFilepath())


setSettings(removeCurrencySymbol, detailedOutput)
main()
if outputJSON:
    createJSON()

