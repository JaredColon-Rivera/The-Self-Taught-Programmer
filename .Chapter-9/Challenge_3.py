
import csv

movies_list = [
				["Top Gun", "Risky Business", "Minority Report"], 
				["Titanic", "The Revanent", "Inception"], 
				["Training Day", "Man on Fire", "Flight"]
			]


with open("movies.cvs", "w", newline='') as f:
	w = csv.writer(f, delimiter=",")
	for x in movies_list:
		w.writerow(x)