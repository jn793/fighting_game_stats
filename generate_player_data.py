import random
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def main():
    generate_player(10000)

def generate_player(player_count):
    players=[]

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
        player_row=[]
        player_id=random.randrange(0,1000000)

        player_name_num=random.randrange(1,1000)

        player_name=str(player_name_prefix[random.randrange(0,prefix_len)]+
            player_name_bridge[random.randrange(0,bridge_len)]+
            player_name_suffix[random.randrange(0,suffix_len)]+
            str(player_name_num))
        
        player_row=[player_id,player_name,player_region[random.randrange(0,region_len)],
            player_rank[random.randrange(0,rank_len)],random.randrange(0,100)]
        players.append(player_row)
    
    df=pd.DataFrame(players,columns=['id','username','region','rank','rank_progress'])
    df=df.drop_duplicates(subset=['id'])
    
    table=pa.Table.from_pandas(df)
    pq.write_table(table,'./data/generated_players.parquet')

main()