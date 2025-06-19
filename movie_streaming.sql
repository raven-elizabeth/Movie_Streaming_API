-- MYSQL DB goes here

-- CREATE
CREATE DATABASE streaming_library;
USE streaming_library;

CREATE TABLE film (
film_ID INT AUTO_INCREMENT,
film_name VARCHAR(255),
synopsis VARCHAR(255),
film_link VARCHAR(255),
PRIMARY KEY (film_ID),
UNIQUE (film_name, synopsis, film_link)
);

CREATE TABLE production_company (
company_ID INT AUTO_INCREMENT,
company_name VARCHAR(255),
PRIMARY KEY (company_ID)
);

CREATE TABLE film_production_company (
film_ID INT,
company_ID INT,
PRIMARY KEY (film_ID, company_ID),
FOREIGN KEY (film_ID) REFERENCES film(film_ID),
FOREIGN KEY (company_ID) REFERENCES production_company(company_ID)
);

CREATE TABLE genre (
genre_ID INT AUTO_INCREMENT,
genre_name VARCHAR(255) UNIQUE,
PRIMARY KEY (genre_ID)
);

CREATE TABLE film_genre (
film_ID INT,
genre_ID INT,
PRIMARY KEY(film_ID, genre_ID),
FOREIGN KEY (film_ID) REFERENCES film(film_ID),
FOREIGN KEY (genre_ID) REFERENCES genre(genre_ID)
);

CREATE TABLE director (
director_ID INT AUTO_INCREMENT,
director_forename VARCHAR(255),
director_surname VARCHAR(255),
PRIMARY KEY (director_ID)
);

CREATE TABLE film_director (
film_ID INT,
director_ID INT,
PRIMARY KEY (film_ID, director_ID),
FOREIGN KEY (film_ID) REFERENCES film(film_ID),
FOREIGN KEY (director_ID) REFERENCES director(director_ID)
);

CREATE TABLE actor (
actor_ID INT AUTO_INCREMENT,
actor_forename VARCHAR(255),
actor_surname VARCHAR(255),
PRIMARY KEY (actor_ID)
);

CREATE TABLE film_actor (
film_ID INT,
actor_ID INT,
PRIMARY KEY (film_ID, actor_ID),
FOREIGN KEY (film_ID) REFERENCES film(film_ID),
FOREIGN KEY (actor_ID) REFERENCES actor(actor_ID)
);

CREATE TABLE region (
region_ID INT AUTO_INCREMENT,
region_name VARCHAR(255) UNIQUE,
PRIMARY KEY (region_ID)
);

CREATE TABLE film_region (
film_ID INT,
region_ID INT,
PRIMARY KEY (film_ID, region_ID),
FOREIGN KEY (film_ID) REFERENCES film(film_ID),
FOREIGN KEY (region_ID) REFERENCES region(region_ID)
);


-- INSERT INTO
INSERT INTO film (film_name, synopsis, film_link)
VALUES
("Robin Hood",
	"The clever outlaw Robin Hood and his loyal friend Little John outsmart the greedy Prince John while fighting for justice and the poor. But when Maid Marian is put in danger, Robin must risk everything in his most daring adventure yet!",
    "https://youtu.be/z4rLod7TBEY?si=wtKc6btFYXS3bLx_"),
("The Goonies",
	"A group of misfit kids find a pirate map and race to find hidden treasure before a family of criminals. Battling booby traps, secret tunnels, and unexpected allies, they must work together to save their homes and uncover the legend of One-Eyed Willy!",
    "https://youtu.be/hJ2j4oWdQtU?si=f2NV_rMTy4_xanCx"),
("Home Alone",
	"Clever eight-year-old Kevin McCallister is accidentally left behind for the holidays and must defend his home from two bumbling burglars. Using brilliant traps and quick thinking, he turns his house into a battleground in the ultimate Christmas showdown!",
    "https://youtu.be/jEDaVHmw7r4?si=8ZOGc9fwSz9ZcsSE"),
("Spider-Man: Homecoming",
	"Peter Parker struggles to balance high school life with his new role as a superhero under Tony Stark’s guidance. But when the deadly Vulture threatens his city, Peter must prove he’s more than just a friendly neighborhood Spider-Man!",
    "https://youtu.be/rk-dF1lIbIg?si=L1yDauXv_fB2rW1t"),
("X-Men",
	"Mutants with extraordinary powers fight for acceptance in a world that fears them. As Professor X’s team clashes with Magneto’s Brotherhood, Wolverine and the X-Men must stop a young mutant from triggering a war.",
    "https://youtu.be/VNxwlx6etXI?si=vwaE09cjNJkrYM7m"),
("Gremlins",
	"A small town descends into chaos when a boy accidentally breaks the rules for his mysterious new pet, unleashing mischievous, destructive creatures. As the gremlins wreak havoc, he must find a way to stop them before it’s too late!",
    "https://youtu.be/XBEVwaJEgaA?si=LetrLy5wMASuLELm"),
("Shrek",
	"A grumpy ogre’s swamp is upended when fairy tale creatures move in, forcing him to rescue Princess Fiona to reclaim his land. Along the way, Shrek discovers friendship, love, and that being different can make you truly special!",
    "https://youtu.be/CwXOrWvPBPk?si=vnh_lS6mG1qrWVKV"),
("The Breakfast Club",
	"Five high school students from different cliques are forced to spend a Saturday in detention together. As they open up, they realize they have more in common than they thought, forging unexpected friendships that change their lives forever.",
    "https://youtu.be/BSXBvor47Zs?si=o8jwQIx9qvG-wcgn"),
("Spider-Man: Into the Spider-Verse",
	"Teenager Miles Morales discovers he has spider-powers and meets other versions of Spider-Man from different dimensions. Together, they must stop a dangerous villain threatening the multiverse, while learning the true meaning of heroism!",
    "https://youtu.be/g4Hbz2jLxvQ?si=PpXK-FSBLEQYUujN"),
("Paddington",
	"A lovable Peruvian bear travels to London in search of a new home and lands in a series of hilarious misadventures. With help from his new family, Paddington shows that kindness and curiosity can bring even the most unlikely friends together!",
    "https://youtu.be/7bZFr2IA0Bo?si=VbiuQpQ6GFqsszxd"),
("Dumbo",
	"A young elephant with oversized ears is ridiculed by others but discovers that his unique gift allows him to soar to new heights. With the help of his loyal mouse friend, Dumbo learns that being different can be his greatest strength!",
    "https://youtu.be/OFNRmu2xRKU?si=BalE6Arweb8f23wm"),
("Harry Potter and the Philosopher's Stone",
	"A young boy named 'Harry' learns that he's a wizard and begins his magical education at Hogwarts, where he attends enchanting classes. As he uncovers a dark secret, Harry and his friends must face evil forces to protect a powerful, enchanted stone!",
    "https://youtu.be/l91Km49W9qI?si=g4-l8iXpK_qdD7WG"),
("The Karate Kid",
	"A bullied teenager moves to a new town and learns karate from an unlikely mentor, Mr. Miyagi. Through hard work and discipline, he discovers the true meaning of strength and finds the courage to face his toughest challenge yet!",
    "https://youtu.be/r_8Rw16uscg?si=IIOuwk7zb6YOOsyz"),
("How to Train Your Dragon",
	"A young Viking named Hiccup befriends an injured dragon, defying his tribe’s belief that dragons are enemies. Together, they embark on an incredible journey that challenges their world and changes everything they thought they knew about dragons!",
    "https://youtu.be/GfBHLVtbG6U?si=dKSze0k54M24caGp"),
("The Lord of the Rings: The Fellowship of the Ring",
	"A young hobbit is entrusted with destroying a powerful ring that could bring darkness to the world. Joined by unlikely heroes, he must face incredible challenges to prevent an evil force from conquering Middle-Earth!",
    "https://youtu.be/_nZdmwHrcnw?si=Ac9azsKKuYpiVH2H");

INSERT INTO production_company (company_name)
VALUES
("Walt Disney Productions"),
("Amblin Entertainment"),
("20th Century Fox"),
("Hughes Entertainment"),
("Marvel Studios"),
("Columbia Pictures"),
("Pascal Pictures"),
("Marvel Entertainment Group"),
("The Donners' Company"),
("Bad Hat Harry Productions"),
("Warner Bros."),
("Dreamworks Animation"),
("Channel Productions"),
("A&M Films"), -- 14
("Marvel Entertainment"),
("Sony Pictures Animation"),
("Arad Productions"),
("Lord Miller Productions"),
("Heyday Films"),
("StudioCanal"),
("TF1 Films Production"),
("Warner Bros. Pictures"),
("1492 Pictures"),
("Delphi II Productions"),
("Jerry Weintraub Productions"),
("WingNut Films"),
("New Line Cinema");

INSERT INTO film_production_company (film_ID, company_ID)
VALUES
(1, 1),
(2, 2),
(3, 3),
(3, 4),
(4, 5),
(4, 6),
(4, 7),
(5, 3),
(5, 8),
(5, 9),
(5, 10),
(6, 2),
(6, 11),
(7, 12),
(8, 13),
(8, 14),
(9, 6),
(9, 15),
(9, 16),
(9, 17),
(9, 18),
(9, 7),
(10, 19),
(10, 20),
(10, 21),
(11, 1),
(12, 22),
(12, 23),
(12, 19),
(13, 24),
(13, 25),
(14, 12),
(15, 26),
(15, 27);

INSERT INTO genre (genre_name)
VALUES
("Children's"),
("Animation"),
("90s"),
("Coming of age"),
("Superhero"),
("Christmas"),
("Comedy"),
("Fantasy"),
("Action"),
("70s"),
("Folklore"),
("80s"),
("Adventure"),
("Sci-Fi"),
("Horror");

INSERT INTO film_genre (film_ID, genre_ID)
VALUES
(1, 1),
(1, 2),
(1, 10),
(1, 7),
(1, 11),
(1, 13),
(2, 1),
(2, 4),
(2, 12),
(2, 7),
(2, 13),
(3, 1),
(3, 3),
(3, 7),
(3, 6),
(4, 5),
(4, 9),
(4, 14),
(5, 5),
(5, 9),
(5, 14),
(6, 3),
(6, 6),
(6, 7),
(6, 15),
(7, 1),
(7, 2),
(7, 7),
(7, 8),
(8, 3),
(8, 4),
(8, 7),
(9, 1),
(9, 2),
(9, 5),
(9, 9),
(10, 1),
(10, 7),
(10, 13),
(11, 1),
(11, 2),
(11, 7),
(12, 1),
(12, 8),
(13, 1),
(13, 4),
(13, 9),
(13, 12),
(14, 1),
(14, 2),
(14, 4),
(14, 8),
(14, 9),
(14, 13),
(15, 8),
(15, 13);

INSERT INTO director (director_forename, director_surname)
VALUES
("Wolfgang", "Reitherman"),
("Richard", "Donner"),
("Chris", "Columbus"),
("Jon", "Watts"),
("Bryan", "Singer"),
("Joe", "Dante"),
("Andrew", "Adamson"),
("Vicky", "Jenson"),
("John", "Hughes"),
("Bob", "Persichetti"),
("Peter", "Ramsey"),
("Rodney", "Rothman"),
("Paul", "King"),
("Ben", "Sharpsteen"),
("John G.", "Avildsen"),
("Chris", "Sanders"),
("Dean", "DeBlois"),
("Peter", "Jackson");

INSERT INTO film_director (film_ID, director_ID)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(7, 8),
(8, 9),
(9, 10),
(9, 11),
(9, 12),
(10, 13),
(11, 14),
(12, 3),
(13, 15),
(14, 16),
(14, 17),
(15, 18);

INSERT INTO actor (actor_forename, actor_surname)
VALUES
("Brian", "Bedford"),
("Phil", "Harris"),
("Monica", "Evans"),
("Pat", "Buttram"),
("Peter", "Ustinov"),
("Jeff", "Cohen"),
("Ke Huy", "Quan"),
("Corey", "Feldman"),
("Sean", "Astin"),
("John", "Matuszak"),
("Macaulay", "Culkin"),
("Catherine", "O'Hara"),
("Joe", "Pesci"),
("Daniel", "Stern"),
("Tom", "Holland"),
("Michael", "Keaton"),
("Zendaya", NULL),
("Marisa", "Tomei"),
("Laura", "Harrier"),
("Hugh", "Jackman"),
("Patrick", "Stewart"),
("Ian", "McKellen"),
("James", "Marsden"),
("Famke", "Janssen"),
("Halle", "Berry"),
("Zach", "Galligan"),
("Phoebe", "Cates"),
("Glynn", "Turman"),
("Howie", "Mandel"),
("Mike", "Myers"),
("Eddie", "Murphy"),
("Cameron", "Diaz"),
("Conrad", "Vernon"),
("Molly", "Ringwald"),
("Judd", "Nelson"),
("Anthony Michael", "Hall"),
("Ally", "Sheedy"),
("Emilio", "Estevez"),
("Shameik", "Moore"),
("Jake", "Johnson"),
("Hailee", "Steinfeld"),
("Mahershala", "Ali"),
("Nicolas", "Cage"),
("John", "Mulaney"),
("Liev", "Schreiber"),
("Ben", "Whishaw"),
("Hugh", "Bonneville"),
("Hall", "Johnson"),
("Billy", "Bletcher"),
("Daniel", "Radcliffe"),
("Rupert", "Grint"),
("Emma", "Watson"),
("Ralph", "Macchio"),
("William", "Zabka"),
("Pat", "Morita"),
("Jay", "Baruchel"),
("America", "Ferrera"),
("Gerard", "Butler"),
("Elijah", "Wood"),
("Viggo", "Mortensen"),
("Orlando", "Bloom"),
("John", "Rhys-Davies"),
("Liv", "Tyler"),
("Cate", "Blanchett"),
("Andy", "Serkis"),
("Dominic", "Monaghan"),
("Billy", "Boyd");

INSERT INTO film_actor (film_ID, actor_ID)
VALUES
(1, 1), -- Robin Hood
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 6), -- The Goonies
(2, 7),
(2, 8),
(2, 9),
(2, 10),
(3, 11), -- Home Alone
(3, 12),
(3, 13),
(3, 14),
(4, 15), -- Spider-Man: Homecoming
(4, 16),
(4, 17),
(4, 18),
(4, 19),
(5, 20), -- X-Men
(5, 21),
(5, 22),
(5, 23),
(5, 24),
(5, 25),
(6, 26), -- Gremlins
(6, 27),
(6, 28),
(6, 29),
(6, 8),
(7, 30), -- Shrek
(7, 31),
(7, 32),
(7, 33),
(8, 34), -- The Breakfast Club
(8, 35),
(8, 36),
(8, 37),
(8, 38),
(9, 39), -- Spider-Man: Into the Spider-Verse
(9, 40),
(9, 41),
(9, 42),
(9, 43),
(9, 44),
(9, 45),
(10, 46), -- Paddington
(10, 47),
(11, 48), -- Dumbo
(11, 49),
(12, 50), -- Harry Potter
(12, 51),
(12, 52),
(13, 53), -- The Karate Kid
(13, 54),
(13, 55),
(14, 56), -- How to Train Your Dragon
(14, 57),
(14, 58),
(15, 59), -- TLOR: The Fellowship of the Ring
(15, 60),
(15, 61),
(15, 62),
(15, 63),
(15, 64),
(15, 65),
(15, 66),
(15, 67),
(15, 9),
(15, 22);

INSERT INTO region (region_name)
VALUES
("Europe"),
("Africa"),
("North America"),
("South America"),
("Oceania"),
("Asia");

INSERT INTO film_region (film_ID, region_ID)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(2, 3),
(2, 4),
(2, 6),
(3, 5),
(3, 1),
(4, 1),
(5, 1),
(5, 2),
(5, 3),
(5, 4),
(5, 5),
(5, 6),
(6, 6),
(6, 5),
(7, 1),
(7, 3),
(7, 4),
(7, 5),
(7, 6),
(8, 3),
(8, 4),
(9, 1),
(10, 2),
(11, 5),
(12, 6),
(13, 2),
(13, 4),
(13, 5),
(13, 6),
(14, 1),
(14, 2),
(14, 3),
(14, 4),
(14, 5),
(14, 6),
(15, 5),
(15, 1);


-- Stored Procedure
DELIMITER //
CREATE PROCEDURE add_new_film (
IN title VARCHAR(255),
IN summary VARCHAR(255),
IN youtube_link VARCHAR(255)
)
BEGIN
	INSERT IGNORE INTO film (film_name, synopsis, film_link)
    VALUES (title, summary, youtube_link);
END //
DELIMITER ;