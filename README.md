

# Python IMDb Top 250 Scrapper
## Contents
 - Data
 - Output Formats
 - Settings
## Data
This script provides following data from the [IMDb Top 250](http://www.imdb.com/chart/top) list:

 - Title (location based)
 - Rank
 - Link
 - Rating
 - Users Ratings
 - Original Title
 - FSK (Germany)
 - Duration
 - Cast
 - Roles
 - Genres
 - Director
 - Writers
 - Budget
 - Opening Weekend Gross
 - Gross USA
 - Gross Worldwide

## Output Formats
Currently, there is only the option to output the data as a JSON file.

A sample JSON file is in the JSON folder.

I'm planning to implement an SQL Script Output and direct Access to a Database.

## Settings
In the main.py file you can modify the settings. Currently available settings are:
|Setting | What it does |
|--|--|
| removeCurrencySymbol | Removes Currency Symbol of Box Office Values  |
| detailedOutput| Only shows Title, Rank, Link and Rating in the console |
| outputJSON |Output a JSON file of the data |
| JSONPath |Path of the JSON file|


> Written with [StackEdit](https://stackedit.io/).
