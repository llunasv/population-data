import csv

def read_population_data(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                country, year, population = row
                data.append({
                    "country": country.strip(),
                    "year": int(year.strip()),
                    "population": int(population.strip())
                })
    return data