import json

titles = []
ranks = []
links = []
ratings = []
usersRated = []
datesScraped = []
originalTitles = []
fsks = []
durations = []
castArrays = []
rolesArrays = []
genresArrays = []
directorArrays = []
writerArrays = []
budgets = []
openingWeekends = []
grossesUSA = []
grossesWorldwide = []

data = {}
data_json = ''

def writeJSON(path, filename):
    filepath = path + filename + ".json"
    with open(filepath, "w+") as fp:
        fp.write(data_json)

def appendJSON(title, rank, link, rating, amountUsersRated, dateScraped, originalTitle, fsk, duration, castArray,
               rolesArray, genresArray, directorArray, writersArray, budget, openingWeekend, grossUSA, grossWorldwide):
    titles.append(title)
    ranks.append(rank)
    links.append(link)
    ratings.append(rating)
    usersRated.append(amountUsersRated)
    datesScraped.append(dateScraped)
    originalTitles.append(originalTitle)
    fsks.append(fsk)
    durations.append(duration)
    castArrays.append(castArray)
    rolesArrays.append(rolesArray)
    genresArrays.append(genresArray)
    directorArrays.append(directorArray)
    writerArrays.append(writersArray)
    budgets.append(budget)
    openingWeekends.append(openingWeekend)
    grossesUSA.append(grossUSA)
    grossesWorldwide.append(grossWorldwide)

def generateJSON():
    global data
    global data_json
    data = [{"Title": t, "Rank": r, "Link": l, "Rating": ra, "Users Rated:": ur, "Date Scraped": ds,
             "Original Title": o, "FSK": f, "Duration": d, "Cast": c, "Roles": ro, "Genres": g,
             "Directors": di, "Writers": w, "Budget": b, "Opening Weekend": o, "Gross USA": gu, "Gross Worldwide": gw}
            for t, r, l, ra, ur, ds, o, f, d, c, ro, g, di, w, b, o, gu, gw in zip(titles, ranks, links, ratings,
                                                                                  usersRated, datesScraped,
                                                                                  originalTitles,fsks, durations,
                                                                                  castArrays, rolesArrays, genresArrays,
                                                                                  directorArrays, writerArrays, budgets,
                                                                                  openingWeekends, grossesUSA,
                                                                                  grossesWorldwide)]

    data_json = json.dumps(data)
    print(data_json)


