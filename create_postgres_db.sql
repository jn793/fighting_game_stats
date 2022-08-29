CREATE TABLE dim_player(
    player_id int PRIMARY KEY,
    username varchar(12) UNIQUE NOT NULL,
    region varchar(16) NOT NULL,
    rank varchar(16) NOT NULL,
    rank_progress int NOT NULL
);

CREATE TABLE dim_match()
    match_id int PRIMARY KEY,
    match_start_epoch int NOT NULL,
    match_end_epoch int,
    match_status varchar(4),
    match_winner_id(int),
    match_loser_id(int)
;

CREATE TABLE dim_character(
    character_id int PRIMARY KEY,
    character_name varchar(16) UNIQUE NOT NULL,
    character_type varchar(32)
);

CREATE TABLE dim_datetime(
    epoch_timestamp int PRIMARY KEY,
    dt_day int NOT NULL,
    dt_month varchar(16) NOT NULL,
    dt_year int NOT NULL,
    competitive_season varchar(32) NOT NULL
);

CREATE TABLE fact_player_match (
    match_id int NOT NULL,
    player_id int NOT NULL,
    character_id int NOT NULL,
    timestamp_key int NOT NULL,
    FOREIGN KEY (match_id) REFERENCES dim_match (match_id),
    FOREIGN KEY (player_id) REFERENCES dim_player (player_id),
    FOREIGN KEY (character_id) REFERENCES dim_character (character_id),
    FOREIGN KEY (timestamp_key) REFERENCES dim_datetime (epoch_timestamp),
    PRIMARY KEY(match_id,player_id,character_id,timestamp_key)
);

