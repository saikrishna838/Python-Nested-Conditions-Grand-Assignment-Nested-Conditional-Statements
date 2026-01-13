n = int(input())
years = n // 365
weeks = (n - (365 * years))
weeks = weeks // 7
days = (n - (365 * years) - (7 * weeks))
days = days // 1
print(str(years) + " years " + str(weeks) + " weeks " + str(days) + " days ")
