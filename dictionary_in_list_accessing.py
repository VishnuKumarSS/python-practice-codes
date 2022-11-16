# TIP:  get() function is used to get the value by entering key in dictionary



data_values = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },]

for i in data_values:
    print(i)
    if i["name"] == "Cristiano Ronaldo": # here we are finding the Cristiano Ronaldo
        print(i['follower_count']) # after that we are printing the follower_count of Cristiano Ronaldo

# for i in data_values:
#     print(i)