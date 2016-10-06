__author__ = 'roshun/sonia'
from random import randint

profile = raw_input("bae, family, budget, hipster, squad, yolo: ")

#defines user class with an empty dictionary
class user:
    def _init_(self):
        prefDict = dict()

user = user()

#maps YelpAPI categories to our parent categories
categories = {"nightlife": ['bars', 'nightlife'],
              "restaurants": ['turkish','spanish','restaurants','portuguese','polish','mideastern','mexican','mediterranean','malaysian', 'african', 'arabian', 'belgian', 'brazilian', 'caribbean', 'chinese', 'donburi', 'food', 'german', 'french', 'gourmet', 'italian', 'japanese', 'latin', 'localflavor'],
              "kidfriendly": ['pets','artsandcrafts', 'education'],
              "outdoor": ['sportgoods','parks','active', 'bicycles', 'diving', 'fitness'],
              "tourist": ['transport','tours','religiousorgs','hotels', 'hotelstravel'],
              "budget": ['homeandgarden'],
              "entertainment": ['tanning','shopping','massmedia', 'beautysvc', 'festivals', 'musicinstrumentservices'],
              "art": ['photographers','arts', 'fashion'],
              "ignore": ['specialtyschools','realestate','publicservicesgovt','professional','physicians','petservices','nonprofit','localservices', 'auto', 'c_and_mh', 'dentalhygienests', 'dentists', 'diagnosticservices', 'eventservices', 'financialservices', 'flowers', 'hair', 'hairremoval', 'health', 'homeservices', 'itservices', 'lawyers']}

#initilaize preference dict based on the user's profile choice
if profile == "bae":
        user.prefDict = {'nightlife': 2, 'restaurants': 2, 'kidfriendly': 0, 'outdoor': 1, 'tourist': 2, 'budget': 0, 'entertainment': 1, 'art': 1}

if profile == "family":
        user.prefDict = {'nightlife': 0, 'restaurants': 2, 'kidfriendly': 3, 'outdoor': 1, 'tourist': 2, 'budget': 0, 'entertainment': 1, 'art': 1}

if profile == "budget":
        user.prefDict = {'nightlife': 1, 'restaurants': 1, 'kidfriendly': 1, 'outdoor': 4, 'tourist': 1, 'budget': 0, 'entertainment': 1, 'art': 1}

if profile == "hipster":
        user.prefDict = {'nightlife': 2, 'restaurants': 2, 'kidfriendly': 0, 'outdoor': 1, 'tourist': .5, 'budget': 0, 'entertainment': 2, 'art': 2.5}

if profile == "squad":
        user.prefDict = {'nightlife': 3, 'restaurants': 2, 'kidfriendly': 0, 'outdoor': 2, 'tourist': 1, 'budget': 0, 'entertainment': 1, 'art': 1}
        
if profile == "yolo":
        user.prefDict = {'nightlife': 3, 'restaurants': 1, 'kidfriendly': 0, 'outdoor': 3, 'tourist': 1, 'budget': 0, 'entertainment': 1, 'art': 1}

print(user.prefDict)


#randomized third category: first two are hardcoded, in app will be top places in city, and prev pick category
cat_array = ["nightlife", "restaurants", "kidfriendly", "outdoor", "tourist", "budget", "entertainment", "art", "ignore"]
category_index = randint(0, 7)
cat_in_array = cat_array[category_index]
random_cat_index = randint(0, (len(categories[cat_in_array]) -1))
random_category = categories[cat_in_array][random_cat_index]

picked_category = raw_input("bars, parks, " + str(random_category) + ": " )
random_options = ["bars", "parks", random_category]
random_options.remove(picked_category)

print("the two non chosen categories are " + str(random_options[0]) + " and " + str(random_options[1]))


#output the next category that should be fed to the yelpAPI based on user preferences
def choose_one(key_user):
	max_category = ""
	chosen_category = ""
	max_rank = 0
    
	for cat in categories:
		if picked_category in categories[cat]:
			chosen_category = cat
			print("the parent category is of the chosen is: " + chosen_category)

	for cat in categories:
		if random_options[0] in categories[cat]:
			nonselect1 = cat
			print("the parent category of the first nonchosen is: " + nonselect1)
        
	for cat in categories:
		if random_options[1] in categories[cat]:
			nonselect2 = cat
			print("the parent category of the second nonchosen is: " + nonselect2)

	if user.prefDict[nonselect1] > 0:
		user.prefDict[nonselect1] -= 1
        
	if user.prefDict[nonselect2] > 0:
		user.prefDict[nonselect2] -= 1

	print(user.prefDict)


	if chosen_category == "nightlife":
		user.prefDict['restaurants'] += 1
		user.prefDict['nightlife'] += 2
		if user.prefDict['kidfriendly'] > 0:
			user.prefDict['kidfriendly'] -= 1
                
	if chosen_category == "restaurants":
		user.prefDict['restaurants'] += 1
    
	if chosen_category == "kidfriendly":
		user.prefDict['kidfriendly'] += 1
		user.prefDict['tourist'] += 1
        
        if user.prefDict['nightlife'] > 0:
            user.prefDict['nightlife'] -= 1

	if chosen_category == "outdoor":
		user.prefDict['outdoor'] += 1

	if chosen_category == "tourist":
		user.prefDict['tourist'] += 1
		user.prefDict['art'] += 1

	if chosen_category == "entertainment":
		user.prefDict['entertainment'] += 1
		user.prefDict['nightlife'] += 2

	if chosen_category == "art":
		user.prefDict['art'] += 1
		user.prefDict['tourist'] += 1
            
	print(user.prefDict)


	for category in key_user.prefDict:
		if key_user.prefDict.get(category) > max_rank:
			max_rank = key_user.prefDict.get(category)
			max_category = category
        print("the user's max category is " + max_category + " with the rank of " + str(max_rank))

	index = randint(0, (len(categories[max_category]) -1))
	next_category = categories[max_category][index]
	print("the random number is: " + str(index))
	print("the next category will be: " + next_category)


choose_one(user)
	
		

