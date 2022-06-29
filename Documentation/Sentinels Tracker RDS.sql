CREATE TABLE [villains] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [full_name] nvarchar(255) UNIQUE,
  [base] nvarchar(255),
  [query_name_value] nvarchar(255),
  [query_alt_value] nvarchar(255)
)
GO

CREATE TABLE [heroes] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [full_name] nvarchar(255) UNIQUE,
  [base] nvarchar(255),
  [query_name_value] nvarchar(255),
  [query_alt_value] nvarchar(255)
)
GO

CREATE TABLE [environments] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [full_name] nvarchar(255) UNIQUE,
  [base] nvarchar(255),
  [query_name_value] nvarchar(255),
  [query_alt_value] nvarchar(255)
)
GO

CREATE TABLE [users] (
  [id] int UNIQUE PRIMARY KEY IDENTITY(1, 1),
  [username] nvarchar(255) UNIQUE
)
GO

CREATE TABLE [heroTeams] (
  [id_hash] nvarchar(255) UNIQUE PRIMARY KEY,
  [hero_one] nvarchar(255),
  [hero_two] nvarchar(255),
  [hero_three] nvarchar(255),
  [hero_four] nvarchar(255),
  [hero_five] nvarchar(255),
  [valid_team] bool
)
GO

CREATE TABLE [opponents] (
  [id_hash] nvarchar(255) UNIQUE PRIMARY KEY,
  [villain_one] nvarchar(255),
  [villain_two] nvarchar(255),
  [villain_three] nvarchar(255),
  [villain_four] nvarchar(255),
  [villain_five] nvarchar(255),
  [valid_team] bool
)
GO

CREATE TABLE [oblivaeonSetups] (
  [id_hash] nvarchar(255) UNIQUE PRIMARY KEY,
  [shield] nvarchar(255),
  [scions] nvarchar(255),
  [rewards] nvarchar(255),
  [environments] nvarchar(255),
  [player_one_heroes] nvarchar(255),
  [player_two_heroes] nvarchar(255),
  [player_three_heroes] nvarchar(255),
  [player_four_heroes] nvarchar(255),
  [player_five_heroes] nvarchar(255)
)
GO

CREATE TABLE [gameDetails] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [username] nvarchar(255),
  [entered_on] timestamp DEFAULT (now()),
  [game_mode] nvarchar(255),
  [selection_method] nvarchar(255),
  [platform] nvarchar(255),
  [end_result] nvarchar(255),
  [win] bool DEFAULT (0),
  [estimated_time] nvarchar(255),
  [house_rules] nvarchar(255),
  [number_of_players] int,
  [number_of_heroes] int,
  [perceived_difficulty] int,
  [rounds] int,
  [oblivaeon_details] nvarchar(255),
  [hero_team] nvarchar(255),
  [environment] nvarchar(255),
  [villain] nvarchar(255),
  [hero_one] nvarchar(255),
  [hero_one_incapped] bool,
  [hero_two] nvarchar(255),
  [hero_two_incapped] bool,
  [hero_three] nvarchar(255),
  [hero_three_incapped] bool,
  [hero_four] nvarchar(255),
  [hero_four_incapped] bool,
  [hero_five] nvarchar(255),
  [hero_five_incapped] bool,
  [villain_one] nvarchar(255),
  [villain_one_incapped] bool,
  [villain_two] nvarchar(255),
  [villain_two_incapped] bool,
  [villain_three] nvarchar(255),
  [villain_three_incapped] bool,
  [villain_four] nvarchar(255),
  [villain_four_incapped] bool,
  [villain_five] nvarchar(255),
  [villain_five_incapped] bool,
  [advanced] bool DEFAULT (0),
  [challenge] bool DEFAULT (0),
  [comments] nvarchar(255),
  [entry_is_valid] bool DEFAULT (false)
)
GO

ALTER TABLE [heroTeams] ADD FOREIGN KEY ([hero_one]) REFERENCES [heroes] ([full_name])
GO

ALTER TABLE [heroTeams] ADD FOREIGN KEY ([hero_two]) REFERENCES [heroes] ([full_name])
GO

ALTER TABLE [heroTeams] ADD FOREIGN KEY ([hero_three]) REFERENCES [heroes] ([full_name])
GO

ALTER TABLE [heroTeams] ADD FOREIGN KEY ([hero_four]) REFERENCES [heroes] ([full_name])
GO

ALTER TABLE [heroTeams] ADD FOREIGN KEY ([hero_five]) REFERENCES [heroes] ([full_name])
GO

ALTER TABLE [opponents] ADD FOREIGN KEY ([villain_one]) REFERENCES [villains] ([full_name])
GO

ALTER TABLE [opponents] ADD FOREIGN KEY ([villain_two]) REFERENCES [villains] ([full_name])
GO

ALTER TABLE [opponents] ADD FOREIGN KEY ([villain_three]) REFERENCES [villains] ([full_name])
GO

ALTER TABLE [opponents] ADD FOREIGN KEY ([villain_four]) REFERENCES [villains] ([full_name])
GO

ALTER TABLE [opponents] ADD FOREIGN KEY ([villain_five]) REFERENCES [villains] ([full_name])
GO

ALTER TABLE [gameDetails] ADD FOREIGN KEY ([username]) REFERENCES [users] ([username])
GO

ALTER TABLE [gameDetails] ADD FOREIGN KEY ([oblivaeon_details]) REFERENCES [oblivaeonSetups] ([id_hash])
GO

ALTER TABLE [gameDetails] ADD FOREIGN KEY ([hero_team]) REFERENCES [heroTeams] ([id_hash])
GO

ALTER TABLE [gameDetails] ADD FOREIGN KEY ([environment]) REFERENCES [environments] ([full_name])
GO

ALTER TABLE [gameDetails] ADD FOREIGN KEY ([villain]) REFERENCES [opponents] ([id_hash])
GO
