import random
import json

def main():
    generate_player(10000)

def generate_player(player_count):
    player_dict={}

    player_name_prefix=['Doc','Grumpy','Happy','Sleepy','Bashful','Sneezy','Dopey']
    prefix_len=len(player_name_prefix)
    player_name_bridge=['','-','_']
    bridge_len=len(player_name_bridge)
    player_name_suffix=['Runner','Glider','Flier','Biker','Jumper','Fighter']
    suffix_len=len(player_name_suffix)
    player_region=['usa','eur','jpn']
    region_len=len(player_region)
    player_rank=['bronze','silver','gold','platinum','diamond']
    rank_len=len(player_rank)

    for x in range(0,player_count):
        

        player_id=random.randrange(0,1000000)
        player_dict[player_id]={}

        player_name_num=random.randrange(1,1000)

        player_name=str(player_name_prefix[random.randrange(0,prefix_len)]+
            player_name_bridge[random.randrange(0,bridge_len)]+
            player_name_suffix[random.randrange(0,suffix_len)]+
            str(player_name_num))
        
        player_dict[player_id]['username']=player_name
        player_dict[player_id]['region']=player_region[random.randrange(0,region_len)]
        player_dict[player_id]['rank']=player_rank[random.randrange(0,rank_len)]
        player_dict[player_id]['rankprogress']=random.randrange(0,100)

    with open('./data/generated_player_data/player_data.json','w') as fp:
        json.dump(player_dict,fp,indent=4)


main()