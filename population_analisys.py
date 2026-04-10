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

def calculate_population_change(data):
    changes = {}
    sorted_data = sorted(data, key=lambda x: (x['country'], x['year']))
    
    for i in range(1, len(sorted_data)):
        curr = sorted_data[i]
        prev = sorted_data[i-1]
        
        if curr['country'] == prev['country']:
            country = curr['country']
            year_range = f"{prev['year']}-{curr['year']}"
            change = curr['population'] - prev['population']
            
            if country not in changes:
                changes[country] = []
            changes[country].append({year_range: change})
            
    return changes