# AirBnB MongoDB Analysis 
### Written and Completed By Catherine Benge.

<br>
This is the report section of the mongodb assignment for database design. Thank you for reading!

<br>
<br>

# Part 1 | The Data

The data that I used was from Airbnb's listings data for the city of Madrid, Spain. [Here is the link](http://insideairbnb.com/get-the-data.html).

The original data file is in csv format. This dataset is very large, and includes many columns of fields. Some of them are later removed, as I will cover in the "munging" section. Here is a sample of the csv file:

<br>

| host_is_superhost | host_thumbnail_url                                                                                         | host_picture_url                                                                                              | host_neighbourhood  | host_listings_count | host_total_listings_count | host_verifications                                                                                                   | host_has_profile_pic | host_identity_verified | neighbourhood                      | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type               | room_type       | accommodates | bathrooms |
|-------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------|---------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|------------------------|------------------------------------|------------------------|------------------------------|----------|-----------|-----------------------------|-----------------|--------------|-----------|
| t                 | https://a0.muscache.com/im/pictures/user/1c7938e4-b6da-433a-a2ac-068d5447b31c.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/1c7938e4-b6da-433a-a2ac-068d5447b31c.jpg?aki_policy=profile_x_medium | Hispanoam√©rica     | 1                   | 1                         | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id',   'government_id']                                   | t                    | t                      |                                    | Hispanoam√©rica        | Chamart√≠n                   | 40.45724 | -3.67688  | Private room in apartment   | Private room    | 2            |           |
| f                 | https://a0.muscache.com/im/users/83531/profile_pic/1338760896/original.jpg?aki_policy=profile_small        | https://a0.muscache.com/im/users/83531/profile_pic/1338760896/original.jpg?aki_policy=profile_x_medium        | Aluche              | 2                   | 2                         | ['email', 'phone', 'reviews', 'manual_offline', 'jumio',   'offline_government_id', 'government_id']                 | t                    | t                      | Madrid, Spain                      | C√°rmenes              | Latina                       | 40.40341 | -3.74084  | Private room in apartment   | Private room    | 1            |           |
| f                 | https://a0.muscache.com/im/pictures/user/52bdf684-be3b-4cf8-aa76-7a3ef5262a2b.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/52bdf684-be3b-4cf8-aa76-7a3ef5262a2b.jpg?aki_policy=profile_x_medium | Legazpi             | 10                  | 10                        | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id', 'selfie',   'government_id', 'identity_manual']      | t                    | t                      | Madrid, Comunidad de Madrid, Spain | Legazpi                | Arganzuela                   | 40.38695 | -3.69304  | Entire apartment            | Entire home/apt | 6            |           |
| f                 | https://a0.muscache.com/im/pictures/user/233f48ef-47ac-463d-afdc-eede22cf636b.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/233f48ef-47ac-463d-afdc-eede22cf636b.jpg?aki_policy=profile_x_medium | Malasa√±a           | 1                   | 1                         | ['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id',   'work_email']                                  | t                    | t                      | Madrid, Spain                      | Universidad            | Centro                       | 40.42202 | -3.70395  | Entire apartment            | Entire home/apt | 3            |           |
| t                 | https://a0.muscache.com/im/users/101653/profile_pic/1314657116/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/101653/profile_pic/1314657116/original.jpg?aki_policy=profile_x_medium       | Justicia            | 1                   | 1                         | ['email', 'phone', 'facebook', 'reviews']                                                                            | t                    | f                      |                                    | Justicia               | Centro                       | 40.41995 | -3.69764  | Entire apartment            | Entire home/apt | 4            |           |
| f                 | https://a0.muscache.com/im/users/114340/profile_pic/1272373168/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/114340/profile_pic/1272373168/original.jpg?aki_policy=profile_x_medium       | Legazpi             | 1                   | 1                         | ['email', 'phone', 'reviews', 'jumio', 'government_id']                                                              | t                    | t                      | Madrid, Comunidad de Madrid, Spain | Legazpi                | Arganzuela                   | 40.38985 | -3.69011  | Private room in house       | Private room    | 1            |           |
| f                 | https://a0.muscache.com/im/pictures/user/52bdf684-be3b-4cf8-aa76-7a3ef5262a2b.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/52bdf684-be3b-4cf8-aa76-7a3ef5262a2b.jpg?aki_policy=profile_x_medium | Legazpi             | 10                  | 10                        | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id', 'selfie',   'government_id', 'identity_manual']      | t                    | t                      |                                    | Legazpi                | Arganzuela                   | 40.38841 | -3.69505  | Entire apartment            | Entire home/apt | 6            |           |
| f                 | https://a0.muscache.com/im/users/130907/profile_pic/1373028590/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/130907/profile_pic/1373028590/original.jpg?aki_policy=profile_x_medium       | Sol                 | 3                   | 3                         | ['email', 'phone', 'reviews']                                                                                        | t                    | f                      |                                    | Sol                    | Centro                       | 40.41552 | -3.70346  | Entire apartment            | Entire home/apt | 2            |           |
| f                 | https://a0.muscache.com/im/users/132883/profile_pic/1430685585/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/132883/profile_pic/1430685585/original.jpg?aki_policy=profile_x_medium       | Embajadores         | 1                   | 1                         | ['email', 'phone', 'facebook', 'reviews']                                                                            | t                    | f                      |                                    | Embajadores            | Centro                       | 40.41111 | -3.70269  | Entire loft                 | Entire home/apt | 2            |           |
| t                 | https://a0.muscache.com/im/users/162701/profile_pic/1326986599/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/162701/profile_pic/1326986599/original.jpg?aki_policy=profile_x_medium       | Palacio             | 1                   | 1                         | ['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id']                                                  | t                    | t                      |                                    | Palacio                | Centro                       | 40.4198  | -3.71078  | Entire apartment            | Entire home/apt | 5            |           |
| t                 | https://a0.muscache.com/im/pictures/user/c96f0fb5-0d2a-4563-8105-37a1ff5b5e60.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/c96f0fb5-0d2a-4563-8105-37a1ff5b5e60.jpg?aki_policy=profile_x_medium | Malasa√±a           | 17                  | 17                        | ['email', 'phone', 'reviews', 'jumio', 'government_id']                                                              | t                    | t                      |                                    | Justicia               | Centro                       | 40.41978 | -3.6973   | Entire apartment            | Entire home/apt | 4            |           |
| f                 | https://a0.muscache.com/im/users/130907/profile_pic/1373028590/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/130907/profile_pic/1373028590/original.jpg?aki_policy=profile_x_medium       | Sol                 | 3                   | 3                         | ['email', 'phone', 'reviews']                                                                                        | t                    | f                      |                                    | Universidad            | Centro                       | 40.42096 | -3.70428  | Entire apartment            | Entire home/apt | 3            |           |
| f                 | https://a0.muscache.com/im/users/218515/profile_pic/1332708533/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/218515/profile_pic/1332708533/original.jpg?aki_policy=profile_x_medium       | Goya                | 1                   | 1                         | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id',   'government_id']                                   | t                    | t                      |                                    | Goya                   | Salamanca                    | 40.42761 | -3.67604  | Entire condominium          | Entire home/apt | 3            |           |
| f                 | https://a0.muscache.com/im/pictures/user/58c5c44d-6c98-43d5-baec-980d08c1a1cd.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/58c5c44d-6c98-43d5-baec-980d08c1a1cd.jpg?aki_policy=profile_x_medium | Palacio             | 1                   | 1                         | ['email', 'phone', 'facebook', 'reviews', 'jumio',   'offline_government_id', 'government_id']                       | t                    | t                      | Madrid, Spain                      | Palacio                | Centro                       | 40.41971 | -3.71256  | Private room in guest suite | Private room    | 1            |           |
| f                 | https://a0.muscache.com/im/pictures/user/cd45cd23-7f8c-4439-ba2a-1b3c064825e5.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/cd45cd23-7f8c-4439-ba2a-1b3c064825e5.jpg?aki_policy=profile_x_medium | Justicia            | 2                   | 2                         | ['email', 'phone', 'facebook', 'reviews', 'manual_offline', 'jumio',   'selfie', 'government_id', 'identity_manual'] | t                    | t                      | Madrid, Spain                      | Justicia               | Centro                       | 40.4208  | -3.69878  | Private room in apartment   | Private room    | 3            |           |
| t                 | https://a0.muscache.com/im/users/313365/profile_pic/1440360603/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/313365/profile_pic/1440360603/original.jpg?aki_policy=profile_x_medium       | Fuencarral-El Pardo | 3                   | 3                         | ['email', 'phone', 'reviews', 'jumio', 'government_id']                                                              | t                    | t                      | Madrid, Spain                      | Pe√±agrande            | Fuencarral - El Pardo        | 40.48409 | -3.72257  | Private room in apartment   | Private room    | 2            |           |
| t                 | https://a0.muscache.com/im/users/353616/profile_pic/1295465186/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/353616/profile_pic/1295465186/original.jpg?aki_policy=profile_x_medium       | Malasa√±a           | 3                   | 3                         | ['email', 'phone', 'reviews', 'offline_government_id', 'selfie',   'government_id']                                  | t                    | t                      | Madrid, Community of Madrid, Spain | Universidad            | Centro                       | 40.42365 | -3.70889  | Entire apartment            | Entire home/apt | 2            |           |
| t                 | https://a0.muscache.com/im/pictures/user/09dc8a1d-f649-4a6c-a0dd-1bb89d880fd4.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/09dc8a1d-f649-4a6c-a0dd-1bb89d880fd4.jpg?aki_policy=profile_x_medium | Malasa√±a           | 6                   | 6                         | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id',   'government_id', 'work_email']                     | t                    | t                      | Madrid, Spain                      | Universidad            | Centro                       | 40.42252 | -3.7025   | Entire apartment            | Entire home/apt | 4            |           |
| t                 | https://a0.muscache.com/im/pictures/user/09dc8a1d-f649-4a6c-a0dd-1bb89d880fd4.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/09dc8a1d-f649-4a6c-a0dd-1bb89d880fd4.jpg?aki_policy=profile_x_medium | Malasa√±a           | 6                   | 6                         | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id',   'government_id', 'work_email']                     | t                    | t                      | Madrid, Community of Madrid, Spain | Palacio                | Centro                       | 40.42191 | -3.71038  | Entire apartment            | Entire home/apt | 3            |           |
| f                 | https://a0.muscache.com/im/pictures/user/2306276d-af01-452d-b8ad-a90496f8b6c8.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/2306276d-af01-452d-b8ad-a90496f8b6c8.jpg?aki_policy=profile_x_medium | Embajadores         | 4                   | 4                         | ['email', 'phone', 'reviews', 'jumio', 'offline_government_id', 'selfie',   'government_id', 'identity_manual']      | t                    | t                      |                                    | Embajadores            | Centro                       | 40.4115  | -3.70449  | Entire apartment            | Entire home/apt | 5            |           |



<br>
As you can see, this is only a snippet of larger data set with over 70 columns. Some fields with text descriptions were so large that they could not be formatted correctly into a table. For this reason, it was necessary to clean up this data with Python and remove unnecessary columns for ease of use.
<br>
<br>
<br>

# Part 2 | Munging

<br>
I munged the data in the program munge.py, completing the following tasks:

## 1. Removing all unecessary columns from the data

I defined all columns that I would need to form the queries in mongodb - 11 in total - for the `CSV DictWriter`:

```python
listing_fields = ['id', 'name','host_id', 'host_name', 'host_is_superhost', 'neighbourhood', 'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'beds', 'price', 'review_scores_rating',]
```

I kept the id values in case I would need to use them as unique identifiers for specific values.

Then, I wrote all the necessary columns in a `for` loop using `writerow({})`:

```python
for row in reader:
	 csv_writer.writerow({
		'id': row['id'],
	})
```

## 2. Standardizing all names with Title text: "MADRID HOUSE" -> "Madrid House"

I noticed that in the original dataset, there were some issues with some titles being capitalized, some being in title format, and some being all lowercase. I wanted to standardize these titles so that they would all share the same format using the `.title()` string method:

```python
for row in reader:
	word = row['name']
	word = word.title()
```

## 3. Replacing all empty data fields with "NULL" so that they are easier to see in the data.

I also noticed that there were many blank fields in the data that would easier to see if they were marked with a `"NULL"` value instead of being blank. I did this by isolating these values and replacing them with `"NULL"`:

```python
for row in reader:
    for i in row:
        if(row[i] == ""):
            row[i] = "NULL"
```

<br>
------

# Part 3 | Queries 

Below are the queries I was asked to complete for this assignment in Mongodb. For these queries, I provide the query itself with any relevant notes, the code used to execute the query, and a sample of the output I received. 

<br>

## 1. show exactly two documents from the listings collection in any order

Note:
1. I did not "pretty up" the query result because I wanted to show the distinction between a non-pretty and pretty query.

<br>

```js
db.listings.find().limit(2);
```

	{ "_id" : ObjectId("607503087c6a86bb05b1996f"), "id" : 6369, "name" : "Rooftop terrace room ,  ensuite bathroom", "host_id" : 13660, "host_name" : "Simon", "host_is_superhost" : "t", "neighbourhood" : "NULL", "neighbourhood_cleansed" : "Hispanoamérica", "neighbourhood_group_cleansed" : "Chamartín", "beds" : 1, "price" : "$50.00", "review_scores_rating" : 98 }

	{ "_id" : ObjectId("607503087c6a86bb05b19970"), "id" : 21853, "name" : "Bright and airy room", "host_id" : 83531, "host_name" : "Abdel", "host_is_superhost" : "f", "neighbourhood" : "Madrid, Spain", "neighbourhood_cleansed" : "Cármenes", "neighbourhood_group_cleansed" : "Latina", "beds" : 1, "price" : "$31.00", "review_scores_rating" : 92 }

<br>

## 2. show exactly 10 documents in any order, but print in easier to read format and noting the host names for further use, using the pretty() function.

Note:
1. I used the first two host ids with a "t" under superhost to form the answer for #3.

<br>

```js
db.listings.find().limit(10).pretty();
```

	{
		"_id" : ObjectId("607503087c6a86bb05b1996f"),
		"id" : 6369,
		"name" : "Rooftop terrace room ,  ensuite bathroom",
		"host_id" : 13660,
		"host_name" : "Simon",
		"host_is_superhost" : "t",
		"neighbourhood" : "NULL",
		"neighbourhood_cleansed" : "Hispanoamérica",
		"neighbourhood_group_cleansed" : "Chamartín",
		"beds" : 1,
		"price" : "$50.00",
		"review_scores_rating" : 98
	}
	{
		"_id" : ObjectId("607503087c6a86bb05b19970"),
		"id" : 21853,
		"name" : "Bright and airy room",
		"host_id" : 83531,
		"host_name" : "Abdel",
		"host_is_superhost" : "f",
		"neighbourhood" : "Madrid, Spain",
		"neighbourhood_cleansed" : "Cármenes",
		"neighbourhood_group_cleansed" : "Latina",
		"beds" : 1,
		"price" : "$31.00",
		"review_scores_rating" : 92
	}
	{
		"_id" : ObjectId("607503087c6a86bb05b19971"),
		"id" : 23001,
		"name" : "Apartmento Arganzuela- Madrid Rio",
		"host_id" : 82175,
		"host_name" : "Jesus",
		"host_is_superhost" : "f",
		"neighbourhood" : "Madrid, Comunidad de Madrid, Spain",
		"neighbourhood_cleansed" : "Legazpi",
		"neighbourhood_group_cleansed" : "Arganzuela",
		"beds" : 5,
		"price" : "$50.00",
		"review_scores_rating" : "NULL"
	}

<br>

## 3. Choose two host_names who are superhosts (available in the host_is_superhost field), and show all of the listings offered by either of the two hosts

<br>

Notes: 
1. Only show the name, price, neighbourhood, host_name, and host_is_superhost for each result
2. The two hosts selected from the last query only have one active listing each. 
<br>

Hosts who are superhosts:
1. Simon, id: 13660
2. Tenty, id: 101653
<br>

```js
let fields = { 
    _id: 0,
     "name": 1, 
     "price":1, 
     "neighourhood":1,
     "host_name": 1, 
     "host_is_superhost": 1,  
};
db.listings.find(
{
  host_id: 
  {
    $in: [13660, 101653],
  },
}, 
fields).pretty();
```
<br>

### Result:

<br>

	{
		"name" : "Rooftop terrace room ,  ensuite bathroom",
		"host_name" : "Simon",
		"host_is_superhost" : "t",
		"price" : "$50.00"
	}
	{
		"name" : "Select the Madrid more \"cool\".",
		"host_name" : "Tenty",
		"host_is_superhost" : "t",
		"price" : "$115.00"
	}

<br>

## 4. find all the unique host_name values (see the docs)

Note: I edited out in the input the beginning values, most of which were special characters or not true "names". 

<br>

```js
db.listings.distinct("host_name");
```
<br>

### Result:

<br>

	"Aaron",
	"Aarón",
	"Abaco",
	"Abbey",
	"Abdel",
	"Abdul-Ridha",
	"Abel",
	"Abel I.",
	"Abelardo",
	"Abigail",
	"Abilio",
	"Abla",
	"Abraham",
	"Acacia",

<br>

## 5. find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as neighbourhood_group_cleansed in the data file), ordered by review_scores_rating descending

<br>

More Information:
1. only show the name, beds, city, review_scores_rating, and price
2. if you run out of memory for this query, try filtering review_scores_rating that aren't empty; lastly, if there's still an issue, you can set the beds to match exactly 2

Notes:
1. I filtered empty review results out of the result so that I could see the valid data

<br>

```js
let fields = { 
    _id: 0,
     "name": 1, 
     "beds": 1, 
     "review_scores_rating":1, 
     "price":1, 
};
db.listings.find({
  beds: 
  {
    $gt: 2,
  },
  review_scores_rating: 
  {
      $nin: ["NULL"],
  },
  neighbourhood_group_cleansed: "Centro",
  }, fields).sort(
  	{
    "review_scores_rating": -1 
  }).pretty().limit(3);
```

<br>

### Result:

<br>


	{
		"name" : "Habitación céntrica a 1 min de Plza Santa Ana",
		"beds" : 3,
		"price" : "$59.00",
		"review_scores_rating" : 100
	}
	{
		"name" : "2 bedroom attic in Madrid center",
		"beds" : 3,
		"price" : "$510.00",
		"review_scores_rating" : 100
	}
	{
		"name" : "Increíble ático c/terraza privada en pleno Madrid!",
		"beds" : 3,
		"price" : "$90.00",
		"review_scores_rating" : 100
	}

<br>

## 6. show the number of listings per host

Note: I used the host_id field for identification, since it is a unique field.

<br>

```js
db.listings.aggregate(
	[
		{ 
			$group: 
				{_id: "$host_id", count: { $sum: 1 } 
			}
		},
	]
)
```
	{ "_id" : "Altagracia", "count" : 1 }
	{ "_id" : "Domi", "count" : 1 }
	{ "_id" : "Orange", "count" : 1 }

<br>

## 7. in a particular neighborhood_group_cleansed of your choosing again, find the average review_scores_rating per neighborhood, and only show the ones above a 95, sorted in descending order of rating (see the docs)

<br>

More Information (Based on Slack Edits)
1. average review_scores_rating for each neighbourhood_group_cleansed
2. only show the ones above 95
3. sort in desc order

Notes:
1. Only one neighborhood had an average rating higher than 95.

```js
db.listings.aggregate(
   [
     {
       $group:
         {
           _id: "$neighbourhood_group_cleansed",
           avgReviewScore: { $avg: "$review_scores_rating" }
         }
     },
     { $sort: {avgReviewScore: -1} }, 
     {$match: { avgReviewScore: {
                $gt: 95
            }
        }
    }
   ]
)
```

<br>

### Result:

<br>

	{ "_id" : "Fuencarral - El Pardo", "avgReviewScore" : 95.53092783505154 }

<br>
<br>

# Part 4 | Extra Credit


## Setup:

I uploaded per the instructions the virtual environment, installed the pymongo module, and the pretty print module so that everything would be formatting correctly. Then, I uploaded a .py file to i6 and ran the file in .venv to fetch the database results.

## 1. find all of the places that have more than 2 beds in a neighborhood of your choosing, ordered by review_scores_rating descending

For this query, I uploaded a [file](queries.py) to i6 with the query and pymongo connection information (provided in instructions.md) and ran this file through the `virtualenv` as follows: `python queries.py`

Here is the query below. 

```python
docs = collection.aggregate(
    [
        {
        "$project": {
            "_id":0,
            "neighbourhood_group_cleansed":1,
            "name":1,
            "beds":1,
            "review_scores_rating":1,
            "price":1
            }
        },
        {
        "$match": 
            {"$and": [
                {"beds":{"$gt":2}},
                {"neighbourhood_group_cleansed":"Centro"},
                {"review_scores_rating": {"$nin": ["NULL"]}}
                ]
        }
    },
        {
        "$sort":
            {"review_scores_rating":-1}}
    ])

for doc in docs:
    pprint.pprint(doc)
```

<br>

### Result:

<br>

	{'beds': 3,
	'name': 'Habitación céntrica a 1 min de Plza Santa Ana',
	'neighbourhood_group_cleansed': 'Centro',
	'price': '$59.00',
	'review_scores_rating': 100}
	{'beds': 3,
	'name': '2 bedroom attic in Madrid center',
	'neighbourhood_group_cleansed': 'Centro',
	'price': '$510.00',
	'review_scores_rating': 100}
	{'beds': 3,
	'name': 'Increíble ático c/terraza privada en pleno Madrid!',
	'neighbourhood_group_cleansed': 'Centro',
	'price': '$90.00',
	'review_scores_rating': 100}


