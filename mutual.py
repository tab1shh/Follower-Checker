import json

following_file_path = r'connections\followers_and_following\following.json'
followers_file_path = r'connections\followers_and_following\followers.json'

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)
    
following_data = read_json_file(following_file_path)
people_i_follow_split = [] 

for relationships_following in following_data['relationships_following']: 
    for following_string_data in relationships_following['string_list_data']: 
        people_i_follow = following_string_data['value']
        people_i_follow_split.extend(people_i_follow.split())

followers_data = read_json_file(followers_file_path)
people_who_follow_me_split = []  
        
for followers_entry in followers_data:
    string_data_list = followers_entry.get('string_list_data') 

    for string_data in string_data_list: 
        people_who_follow_me = string_data.get('value')
        people_who_follow_me_split.extend(people_who_follow_me.split())


people_i_follow_set = set(people_i_follow_split)
people_who_follow_me_set = set(people_who_follow_me_split)

mutuals = people_i_follow_set.intersection(people_who_follow_me_set) 
non_mutuals_i_follow = people_i_follow_set - people_who_follow_me_set 
non_mutuals_who_follow_me = people_who_follow_me_set - people_i_follow_set 

print("non mutuals that i follow:")
for follower in non_mutuals_i_follow:
    print(follower)

print("\nnon mutuals who follow me")
for follower in non_mutuals_who_follow_me:
    print(follower)