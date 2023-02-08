﻿# WebScraping-LaLiga-Results
 
 This project is a web scraper that collects data on the La Liga league in Spain for the years 2022 to 2019. The data collected includes shooting statistics for each team in the league, as well as results from matches played. The data is obtained from the website fbref.com, which provides a wealth of information on football leagues, teams, and players.

The project uses the libraries pandas and requests to collect and process the data, while BeautifulSoup is used to parse the HTML content of the pages. A for loop is used to iterate through each year in the specified range and retrieve data for each team in the league. The data is stored in a list of dataframes and later combined into a single dataframe using the pd.concat() method. Finally, the data is exported to a CSV file using the to_csv() method.
