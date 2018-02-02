import datetime
import time

removeCurrencySymbol = True
detailedOutput = True

# Settings functions
def CurrencySetting(boolean):
    global removeCurrencySymbol
    removeCurrencySymbol = boolean

def detailedOutputSetting(boolean):
    global detailedOutput
    detailedOutput = boolean

# Date functions
def getTS():
    ts = time.time()
    now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    return now

def getTSFilepath():
    ts = time.time()
    now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    return now

# String manipulation
def removeBreaks(string):
    return string.replace('\n', '')

def removeCurrency(string):
    string = removeBreaks(string)
    string = string.replace(' ', '')
    string = string.replace(',', '')

    if removeCurrencySymbol:
        string = string.replace('$', '')
        string = string.replace('£', '')
        string = string.replace('€', '')
        string = string.replace('RUR ', '')
        string = string.replace('KRW ', '')
        string = string.replace('FRF ', '')

    return string

def calcMinutens(duration):
    try:
        hours = int(duration.split('h')[0])
    except:
        hours = 0

    try:
        minutes = int(duration.split('h')[1].replace('min', ''))
    except:
        minutes = 0

    duration = hours * 60 + minutes
    return duration

# Movie Information
def getTitle(titleColumn):
    title = titleColumn.find("a").contents[0]

    print("\n \n")
    print("===", title, "===")

    return title


def getLink(linkText):
    linkSuffix = 'http://www.imdb.com'
    link = linkSuffix + linkText.split('?')[0]

    print(" Link:", link)

    return link

def getRank(linkText):
    rank = linkText.split('_')[15]

    print(" Rank:", rank)

    return rank


def getRating(row):
    ratingColumn = row.find("td", {"class": "ratingColumn imdbRating"}).find("strong")
    rating = ratingColumn.contents[0]

    print(" Rating:", rating)

    return rating

def getAmountUsersRated(row):
    ratingColumn = row.find("td", {"class": "ratingColumn imdbRating"}).find("strong")
    amountUsersRated =  removeCurrency(str(ratingColumn).split(' ')[4])

    if detailedOutput:
        print(" Amount users rated:", amountUsersRated)

    return amountUsersRated

# Movie Subinformation
def getOriginalTitle(main, title):
    try:
        original_title = main.find("div", {"class" : "originalTitle"}).text.split(' (original')[0]
    except:
        original_title = title

    if detailedOutput:
        print(" Original Title:", original_title)

    return original_title

def getFSK(main):
    try:
        fsk = removeBreaks(main.find("meta", {"itemprop" : "contentRating"})['content'])
    except:
        fsk = ''

    if detailedOutput:
        print(" FSK:", fsk)

    return fsk

def getDuration(main):
    duration = removeBreaks(main.find("time", {"itemprop" : "duration"}).text.replace(' ', ''))
    duration = calcMinutens(duration)

    if detailedOutput:
        print(" Duration:", duration)

    return duration


def getCast(movieSoup):
    castArray = []
    castTable = movieSoup.find("table", {"class": "cast_list"})
    cast = castTable.findAll("span", {"itemprop": "name"})

    for span in cast:
        castArray.append(span.text)

    if detailedOutput:
        print(" Cast:", castArray)

    return castArray

def getRoles(movieSoup):
    rolesArray = []
    castTable = movieSoup.find("table", {"class": "cast_list"})
    roles = castTable.findAll("td", {"class" : "character"})

    for a in roles:
        rolesArray.append(removeBreaks(a.text).strip())

    if detailedOutput:
        print(" Roles:", rolesArray)

    return rolesArray

def getGenres(movieSoup):
    genresArray = []
    genres_list = movieSoup.find("div", {"itemprop": "genre"})

    for a in genres_list.findAll("a"):
        genresArray.append(a.text)

    if detailedOutput:
        print(" Genres:", genresArray)

    return genresArray

def getWriters(main):
    writersArray = []
    writer_area = main.find("span", {"itemprop" : "creator"})

    for span in writer_area.findAll("span", {"itemprop" : "name"}):
        writersArray.append(span.text)

    if detailedOutput:
        print(" Writers:", writersArray)

    return writersArray

def getDirectors(main):
    directorArray = []
    director_area = main.find("span", {"itemprop" : "director"})

    for span in director_area.findAll("span", {"itemprop" : "name"}):
        directorArray.append(span.text)

    if detailedOutput:
        print(" Directors:", directorArray)

    return directorArray

#Box Office
def getBudget(titleDetails):
    try:
        budget = removeCurrency(titleDetails.find(text="Budget:").parent.nextSibling)
    except:
        budget = ''

    if detailedOutput:
        print(" Budget:", budget)

    return budget

def getOpneningWeekend(titleDetails):
    try:
        openingWeekend = removeCurrency(titleDetails.find(text="Opening Weekend USA:").parent.nextSibling)
    except:
        openingWeekend = ''

    if detailedOutput:
        print(" Opening Weekend:", openingWeekend)

    return  openingWeekend

def getGrossUSA(titleDetails):
    try:
        grossUSA = removeCurrency(titleDetails.find(text="Gross USA:").parent.nextSibling)
    except:
        grossUSA = ''

    if detailedOutput:
        print(" Gross USA:", grossUSA)

    return grossUSA

def getGrossWorldwide(titleDetails):
    try:
        grossWorldwide = removeCurrency(titleDetails.find(text="Cumulative Worldwide Gross:").parent.nextSibling)
    except:
        grossWorldwide = ''

    if detailedOutput:
        print(" Gross Worldwide:", grossWorldwide)

    return grossWorldwide
