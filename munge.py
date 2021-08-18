import csv

raw_data = open('data/listings.csv', 'r')
clean_data = open('data/listings_clean.csv', 'w')

reader = csv.DictReader(raw_data)
reader = list(reader)

listing_fields = ['id', 'name','host_id', 'host_name', 'host_is_superhost', 'neighbourhood', 'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'beds', 'price', 'review_scores_rating',]
csv_writer = csv.DictWriter(clean_data, fieldnames=listing_fields)
csv_writer.writeheader()

for row in reader:
    for i in row:
        if(row[i] == ""):
            row[i] = "NULL"
    word = row['name']
    word = word.title()

    csv_writer.writerow({
        'id': row['id'],
        'name': word,
        'host_id': row['host_id'], 
        'host_name': row['host_name'],
        'host_is_superhost': row['host_is_superhost'], 
        'neighbourhood': row['neighbourhood'],
        'neighbourhood_cleansed': row['neighbourhood_cleansed'],
        'neighbourhood_group_cleansed': row['neighbourhood_group_cleansed'],
        'beds': row['beds'], 
        'price': row['price'], 
        'review_scores_rating': row['review_scores_rating']
    })
