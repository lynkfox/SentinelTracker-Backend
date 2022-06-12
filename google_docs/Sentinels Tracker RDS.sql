CREATE TABLE `boxSets` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255) UNIQUE,
  `dynamo_meta_query` varchar(255)
);

CREATE TABLE `villains` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255) UNIQUE,
  `box_set` varchar(255),
  `dynamo_meta_query` varchar(255),
  `total_wins` int DEFAULT 0,
  `total_games` int DEFAULT 0
);

CREATE TABLE `heroes` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255) UNIQUE,
  `box_set` varchar(255),
  `nemesis` varchar(255),
  `dynamo_meta_query` varchar(255),
  `total_wins` int DEFAULT 0,
  `total_games` int DEFAULT 0
);

CREATE TABLE `environments` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255) UNIQUE,
  `box_set` varchar(255),
  `dynamo_meta_query` varchar(255),
  `total_wins` int DEFAULT 0,
  `total_games` int DEFAULT 0
);

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255) UNIQUE,
  `dynamo_meta_query` varchar(255),
  `total_wins` int DEFAULT 0,
  `total_games` int DEFAULT 0
);

CREATE TABLE `heroTeams` (
  `id_hash` varchar(255) PRIMARY KEY,
  `hero_one` varchar(255),
  `hero_two` varchar(255),
  `hero_three` varchar(255),
  `hero_four` varchar(255),
  `hero_five` varchar(255)
);

CREATE TABLE `opponents` (
  `id_hash` varchar(255) PRIMARY KEY,
  `villain_one` varchar(255),
  `villain_two` varchar(255),
  `villain_three` varchar(255),
  `villain_four` varchar(255),
  `villain_five` varchar(255)
);

CREATE TABLE `oblivaeonSetups` (
  `id_hash` varchar(255) PRIMARY KEY,
  `scions` varchar(255),
  `shield` varchar(255),
  `rewards` varchar(255)
);

CREATE TABLE `gameDetails` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255),
  `entered_on` timestamp DEFAULT (now()),
  `game_mode` varchar(255),
  `selection_method` varchar(255),
  `platform` varchar(255),
  `end_result` varchar(255),
  `estimated_time` varchar(255),
  `house_rules` varchar(255),
  `number_of_players` int,
  `number_of_heroes` int,
  `perceived_difficulty` int,
  `rounds` int,
  `oblivaeon_details` varchar(255),
  `hero_team` varchar(255),
  `environment` varchar(255),
  `villain` varchar(255),
  `hero_one_incapped` bool,
  `hero_two_incapped` bool,
  `hero_three_incapped` bool,
  `hero_four_incapped` bool,
  `hero_five_incapped` bool,
  `villain_one_incapped` bool,
  `villain_two_incapped` bool,
  `villain_three_incapped` bool,
  `villain_four_incapped` bool,
  `villain_five_incapped` bool
);

ALTER TABLE `villains` ADD FOREIGN KEY (`box_set`) REFERENCES `boxSets` (`full_name`);

ALTER TABLE `heroes` ADD FOREIGN KEY (`box_set`) REFERENCES `boxSets` (`full_name`);

ALTER TABLE `heroes` ADD FOREIGN KEY (`nemesis`) REFERENCES `villains` (`full_name`);

ALTER TABLE `environments` ADD FOREIGN KEY (`box_set`) REFERENCES `boxSets` (`full_name`);

ALTER TABLE `heroTeams` ADD FOREIGN KEY (`hero_one`) REFERENCES `heroes` (`full_name`);

ALTER TABLE `heroTeams` ADD FOREIGN KEY (`hero_two`) REFERENCES `heroes` (`full_name`);

ALTER TABLE `heroTeams` ADD FOREIGN KEY (`hero_three`) REFERENCES `heroes` (`full_name`);

ALTER TABLE `heroTeams` ADD FOREIGN KEY (`hero_four`) REFERENCES `heroes` (`full_name`);

ALTER TABLE `heroTeams` ADD FOREIGN KEY (`hero_five`) REFERENCES `heroes` (`full_name`);

ALTER TABLE `opponents` ADD FOREIGN KEY (`villain_one`) REFERENCES `villains` (`full_name`);

ALTER TABLE `opponents` ADD FOREIGN KEY (`villain_two`) REFERENCES `villains` (`full_name`);

ALTER TABLE `opponents` ADD FOREIGN KEY (`villain_three`) REFERENCES `villains` (`full_name`);

ALTER TABLE `opponents` ADD FOREIGN KEY (`villain_four`) REFERENCES `villains` (`full_name`);

ALTER TABLE `opponents` ADD FOREIGN KEY (`villain_five`) REFERENCES `villains` (`full_name`);

ALTER TABLE `gameDetails` ADD FOREIGN KEY (`user`) REFERENCES `users` (`username`);

ALTER TABLE `gameDetails` ADD FOREIGN KEY (`oblivaeon_details`) REFERENCES `oblivaeonSetups` (`id_hash`);

ALTER TABLE `gameDetails` ADD FOREIGN KEY (`hero_team`) REFERENCES `heroTeams` (`id_hash`);

ALTER TABLE `gameDetails` ADD FOREIGN KEY (`environment`) REFERENCES `environments` (`full_name`);

ALTER TABLE `gameDetails` ADD FOREIGN KEY (`villain`) REFERENCES `opponents` (`id_hash`);
