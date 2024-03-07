import csv

MIN_REVIEWS = 100000
newfilename = 'amazon_products_over_'+str(MIN_REVIEWS)+'_reviews.csv'

with open('raw/amazon_products.csv', newline='') as csvreadfile:
    reader = csv.DictReader(csvreadfile)
    with open(newfilename, 'w+', newline='') as csvwritefile:
        writer = csv.DictWriter(csvwritefile, reader.fieldnames)
        writer.writeheader()
        i = 0
        for row in reader:
            n_reviews = int(row['reviews'])
            if n_reviews > MIN_REVIEWS:
                writer.writerow(row)
                i += 1

print(i, " rows found for MIN_REVIEWS =",MIN_REVIEWS)
print('see ', newfilename)
