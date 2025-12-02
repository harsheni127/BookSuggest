# load_books_big.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsuggest.settings")
django.setup()

from catalog.models import Book, Genre

books_data = [
       {
        "title": "It Ends With Us",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Fiction"],
        "rating": 5,
        "description": "A powerful story about love, trauma, strength, and difficult choices."
    },
    {
        "title": "It Starts With Us",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Fiction"],
        "rating": 4,
        "description": "A heartfelt sequel that explores healing, second chances, and choosing happiness."
    },
    {
        "title": "November 9",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama", "Fiction"],
        "rating": 5,
        "description": "A unique love story where two people meet on the same date each year."
    },
    {
        "title": "Ugly Love",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 4,
        "description": "An emotional love story about boundaries, pain, and healing."
    },
    {
        "title": "Verity",
        "author": "Colleen Hoover",
        "genres": ["Thriller", "Romance", "Mystery"],
        "rating": 5,
        "description": "A chilling psychological thriller about lies, manuscripts, and obsession."
    },
    {
        "title": "Reminders of Him",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A mother fights to rebuild her life and reconnect with her daughter."
    },
    {
        "title": "All Your Perfects",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A heartbreaking yet hopeful story about marriage, infertility, and love."
    },
    {
        "title": "Confess",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 4,
        "description": "A powerful love story built around secrets, art, and truth."
    },
    {
        "title": "Maybe Someday",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Young Adult"],
        "rating": 4,
        "description": "A musical romance filled with emotions, betrayal, and tough decisions."
    },
    {
        "title": "Maybe Not",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Comedy"],
        "rating": 4,
        "description": "A funny and cute novella set in the Maybe series universe."
    },
    {
        "title": "Maybe Now",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Young Adult"],
        "rating": 4,
        "description": "A satisfying continuation of the Maybe series, full of love and choices."
    },
    {
        "title": "Heart Bones",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A summer romance that explores class differences, secrets, and family wounds."
    },

 
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genres": ["Fiction", "Philosophy"],
        "rating": 5,
        "description": "A philosophical story about following your dreams."
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genres": ["Self-help", "Productivity"],
        "rating": 5,
        "description": "A guide on building better habits with small, consistent changes."
    },

    {
        "title": "It Ends With Us",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Fiction"],
        "rating": 5,
        "description": "A powerful story about love, trauma, strength, and difficult choices."
    },
    {
        "title": "It Starts With Us",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Fiction"],
        "rating": 4,
        "description": "A heartfelt sequel exploring healing and second chances."
    },
    {
        "title": "November 9",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A unique love story where two people meet on the same date each year."
    },
    {
        "title": "Ugly Love",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 4,
        "description": "An emotional story about boundaries, pain, and healing."
    },
    {
        "title": "Verity",
        "author": "Colleen Hoover",
        "genres": ["Thriller", "Romance", "Mystery"],
        "rating": 5,
        "description": "A chilling psychological thriller about lies and obsession."
    },
    {
        "title": "Reminders of Him",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A mother fights to rebuild her life and reconnect with her daughter."
    },
    {
        "title": "All Your Perfects",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A heartbreaking story about marriage, infertility, and love."
    },
    {
        "title": "Confess",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 4,
        "description": "A powerful love story built around secrets and truth."
    },
    {
        "title": "Maybe Someday",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Young Adult"],
        "rating": 4,
        "description": "A musical romance filled with emotions and tough decisions."
    },
    {
        "title": "Maybe Not",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Comedy"],
        "rating": 4,
        "description": "A cute novella set in the Maybe series universe."
    },
    {
        "title": "Maybe Now",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Young Adult"],
        "rating": 4,
        "description": "A satisfying continuation of the Maybe series."
    },
    {
        "title": "Heart Bones",
        "author": "Colleen Hoover",
        "genres": ["Romance", "Drama"],
        "rating": 5,
        "description": "A summer romance exploring class differences and family wounds."
    },

  
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genres": ["Fiction", "Philosophy"],
        "rating": 5,
        "description": "A philosophical tale about destiny and following your dreams."
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genres": ["Self-help", "Non-fiction"],
        "rating": 5,
        "description": "Small habits that create big improvements over time."
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "genres": ["Finance", "Self-help"],
        "rating": 4,
        "description": "The mindset difference between the rich and middle class."
    },
    {
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "genres": ["Finance", "Self-help"],
        "rating": 5,
        "description": "Timeless lessons on wealth, greed, and happiness."
    },
    {
        "title": "Ikigai",
        "author": "Héctor García",
        "genres": ["Self-help", "Lifestyle"],
        "rating": 5,
        "description": "The Japanese secret to living a long, meaningful life."
    },
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "genres": ["Thriller", "Mystery"],
        "rating": 5,
        "description": "A shocking psychological thriller about a woman's silence."
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genres": ["Fantasy", "Adventure"],
        "rating": 5,
        "description": "The magical beginning of Harry Potter’s journey."
    },
    {
        "title": "The Power of Your Subconscious Mind",
        "author": "Joseph Murphy",
        "genres": ["Self-help", "Spirituality"],
        "rating": 4,
        "description": "How the subconscious mind shapes your reality."
    },
   
    {"title":"It Ends With Us","author":"Colleen Hoover","genres":["Romance","Fiction"],"rating":5,"description":"A powerful story about love, trauma, strength, and difficult choices."},
    {"title":"It Starts With Us","author":"Colleen Hoover","genres":["Romance","Fiction"],"rating":4,"description":"A heartfelt sequel exploring healing and second chances."},
    {"title":"November 9","author":"Colleen Hoover","genres":["Romance","Drama"],"rating":5,"description":"A unique love story where two people meet on the same date each year."},
    {"title":"Ugly Love","author":"Colleen Hoover","genres":["Romance","Drama"],"rating":4,"description":"An emotional story about boundaries, pain, and healing."},
    {"title":"Verity","author":"Colleen Hoover","genres":["Thriller","Romance","Mystery"],"rating":5,"description":"A chilling psychological thriller about lies and obsession."},
    {"title":"Reminders of Him","author":"Colleen Hoover","genres":["Romance","Drama"],"rating":5,"description":"A mother fights to rebuild her life and reconnect with her daughter."},
    {"title":"All Your Perfects","author":"Colleen Hoover","genres":["Romance","Drama"],"rating":5,"description":"A heartbreaking story about marriage, infertility, and love."},
    {"title":"Confess","author":"Colleen Hoover","genres":["Romance","Drama"],"rating":4,"description":"A powerful love story built around secrets and truth."},
    {"title":"Maybe Someday","author":"Colleen Hoover","genres":["Romance","Young Adult"],"rating":4,"description":"A musical romance filled with emotions and tough decisions."},
    {"title":"Maybe Not","author":"Colleen Hoover","genres":["Romance","Comedy"],"rating":4,"description":"A cute novella set in the Maybe series universe."},
    {"title":"Maybe Now","author":"Colleen Hoover","genres":["Romance","Young Adult"],"rating":4,"description":"A satisfying continuation of the Maybe series."},
    {"title":"Heart Bones","author":"Colleen Hoover","genres":["Romance","Drama"],"rating":5,"description":"A summer romance exploring class differences and family wounds."},
    {"title":"The Alchemist","author":"Paulo Coelho","genres":["Fiction","Philosophy"],"rating":5,"description":"A philosophical tale about destiny and following your dreams."},
    {"title":"Atomic Habits","author":"James Clear","genres":["Self-help","Non-fiction"],"rating":5,"description":"Small habits that create big improvements over time."},
    {"title":"Rich Dad Poor Dad","author":"Robert Kiyosaki","genres":["Finance","Self-help"],"rating":4,"description":"The mindset difference between the rich and middle class."},
    {"title":"The Psychology of Money","author":"Morgan Housel","genres":["Finance","Self-help"],"rating":5,"description":"Timeless lessons on wealth, greed, and happiness."},
    {"title":"Ikigai","author":"Héctor García","genres":["Self-help","Lifestyle"],"rating":5,"description":"The Japanese secret to living a long, meaningful life."},
    {"title":"The Silent Patient","author":"Alex Michaelides","genres":["Thriller","Mystery"],"rating":5,"description":"A shocking psychological thriller about a woman's silence."},
    {"title":"Harry Potter and the Sorcerer's Stone","author":"J.K. Rowling","genres":["Fantasy","Adventure"],"rating":5,"description":"The magical beginning of Harry Potter’s journey."},
    {"title":"The Power of Your Subconscious Mind","author":"Joseph Murphy","genres":["Self-help","Spirituality"],"rating":4,"description":"How the subconscious mind shapes your reality."},

    {"title":"One Piece","author":"Eiichiro Oda","genres":["Manga","Adventure","Fantasy"],"rating":5,"description":"Pirate adventure searching for the One Piece."},
    {"title":"Naruto","author":"Masashi Kishimoto","genres":["Manga","Action"],"rating":5,"description":"A young ninja with dreams to become Hokage."},
    {"title":"Bleach","author":"Tite Kubo","genres":["Manga","Action"],"rating":4,"description":"Soul Reapers fighting Hollows."},
    {"title":"My Hero Academia","author":"Kohei Horikoshi","genres":["Manga","Superhero"],"rating":5,"description":"A world of heroes and quirks."},
    {"title":"Attack on Titan","author":"Hajime Isayama","genres":["Manga","Dark Fantasy"],"rating":5,"description":"Humanity vs titans behind massive walls."},
    {"title":"Demon Slayer","author":"Koyoharu Gotouge","genres":["Manga","Action"],"rating":5,"description":"A demon-hunting swordsman's journey."},
    {"title":"Fullmetal Alchemist","author":"Hiromu Arakawa","genres":["Manga","Fantasy"],"rating":5,"description":"Two brothers and alchemy's cost."},
    {"title":"Death Note","author":"Tsugumi Ohba","genres":["Manga","Psychological"],"rating":5,"description":"A notebook that kills; moral cat-and-mouse."},
    {"title":"Dragon Ball","author":"Akira Toriyama","genres":["Manga","Action"],"rating":5,"description":"Epic battles and the search for Dragon Balls."},
    {"title":"Hunter x Hunter","author":"Yoshihiro Togashi","genres":["Manga","Adventure"],"rating":5,"description":"A young boy seeking his father, training as a hunter."},
    {"title":"JoJo's Bizarre Adventure","author":"Hirohiko Araki","genres":["Manga","Adventure"],"rating":5,"description":"Generational saga with supernatural stands."},
    {"title":"Fairy Tail","author":"Hiro Mashima","genres":["Manga","Fantasy"],"rating":4,"description":"Guild adventures and powerful magic."},
    {"title":"Tokyo Ghoul","author":"Sui Ishida","genres":["Manga","Horror"],"rating":5,"description":"A half-ghoul struggling with identity."},
    {"title":"Sailor Moon","author":"Naoko Takeuchi","genres":["Manga","Magical Girl"],"rating":4,"description":"Girls transforming to protect the world."},
    {"title":"Cowboy Bebop (manga)","author":"Hajime Yatate / Cain Kuga","genres":["Manga","Sci-Fi"],"rating":4,"description":"Bounty hunters in space."},
    {"title":"Steins;Gate (novel)","author":"Chiyomaru Shikura","genres":["Light Novel","Sci-Fi"],"rating":5,"description":"Time-travel thriller with emotional stakes."},
    {"title":"Code Geass (novel)","author":"Ichirō Ōkouchi","genres":["Light Novel","Mecha"],"rating":4,"description":"A rebel with a supernatural power."},
    {"title":"Neon Genesis Evangelion","author":"Yoshiyuki Sadamoto","genres":["Manga","Mecha"],"rating":5,"description":"Pilots and psychological mecha conflicts."},
    {"title":"Akira","author":"Katsuhiro Otomo","genres":["Manga","Sci-Fi"],"rating":5,"description":"Dystopian cyberpunk classic."},
    {"title":"Berserk","author":"Kentaro Miura","genres":["Manga","Dark Fantasy"],"rating":5,"description":"A dark epic of revenge and fate."},
    {"title":"Vagabond","author":"Takehiko Inoue","genres":["Manga","Historical"],"rating":5,"description":"Musashi's journey in a masterful art style."},
    {"title":"Gintama","author":"Hideaki Sorachi","genres":["Manga","Comedy"],"rating":5,"description":"Samurai-era comedy with wild parody."},
    {"title":"Yu Yu Hakusho","author":"Yoshihiro Togashi","genres":["Manga","Action"],"rating":5,"description":"Spirit detective battles."},
    {"title":"Rurouni Kenshin","author":"Nobuhiro Watsuki","genres":["Manga","Historical"],"rating":5,"description":"A wandering swordsman with a past."},
    {"title":"Hellsing","author":"Kouta Hirano","genres":["Manga","Horror"],"rating":4,"description":"Vampire hunters vs supernatural threats."},
    {"title":"Black Clover","author":"Yūki Tabata","genres":["Manga","Fantasy"],"rating":4,"description":"Two boys chasing the dream to be wizard king."},
    {"title":"Chainsaw Man","author":"Tatsuki Fujimoto","genres":["Manga","Dark Fantasy"],"rating":5,"description":"A devil-hunting chaotic action series."},
    {"title":"Jujutsu Kaisen","author":"Gege Akutami","genres":["Manga","Supernatural"],"rating":5,"description":"Curses, sorcery and fierce battles."},
    {"title":"Mob Psycho 100","author":"ONE","genres":["Manga","Comedy"],"rating":5,"description":"Powerful psychic boy and slice-of-life humor."},
    {"title":"Vinland Saga","author":"Makoto Yukimura","genres":["Manga","Historical"],"rating":5,"description":"Vikings, revenge, and growth."},
    {"title":"Dr. Stone","author":"Riichiro Inagaki","genres":["Manga","Sci-Fi"],"rating":4,"description":"Science vs stone-age reboot."},
    {"title":"The Promised Neverland","author":"Kaiu Shirai","genres":["Manga","Thriller"],"rating":5,"description":"Children plotting escape from a terrible fate."},
    {"title":"Blue Period","author":"Tsubasa Yamaguchi","genres":["Manga","Slice of Life"],"rating":4,"description":"Art, passion, and the struggle to create."},
    {"title":"Kimi ni Todoke","author":"Karuho Shiina","genres":["Manga","Romance"],"rating":4,"description":"Shy girl and slow-blooming romance."},
    {"title":"Fruits Basket","author":"Natsuki Takaya","genres":["Manga","Fantasy"],"rating":5,"description":"A family cursed to transform into animals."},
    {"title":"Natsume's Book of Friends","author":"Yuki Midorikawa","genres":["Manga","Supernatural"],"rating":5,"description":"A gentle tale of yokai and human bonds."},
    {"title":"Kaguya-sama: Love is War","author":"Aka Akasaka","genres":["Manga","Romantic Comedy"],"rating":5,"description":"Mind games between two proud students."},
    {"title":"Horimiya","author":"HERO & Daisuke Hagiwara","genres":["Manga","Romance"],"rating":5,"description":"Hidden sides of highschool sweethearts."},
    {"title":"Love Hina","author":"Ken Akamatsu","genres":["Manga","Romcom"],"rating":4,"description":"Hilarious harem romcom."},
    {"title":"The Quintessential Quintuplets","author":"Negi Haruba","genres":["Manga","Romance"],"rating":4,"description":"Tutor and five very different sisters."},
    {"title":"Spice and Wolf","author":"Isuna Hasekura","genres":["Light Novel","Fantasy"],"rating":5,"description":"Merchant travels with a harvest goddess."},
    {"title":"Toradora!","author":"Yuyuko Takemiya","genres":["Light Novel","Romance"],"rating":5,"description":"A sweet tsundere romantic comedy."},
    {"title":"Clannad (novel)","author":"Key / Jun Maeda","genres":["Visual Novel Novelization","Drama"],"rating":5,"description":"Emotional stories about family and growth."},
    {"title":"Your Lie in April","author":"Naoshi Arakawa","genres":["Manga","Drama"],"rating":5,"description":"Music and healing after grief."},
    {"title":"Barakamon","author":"Satsuki Yoshino","genres":["Manga","Slice of Life"],"rating":5,"description":"Calligrapher's rural life and growth."},
    {"title":"Silver Spoon","author":"Hiromu Arakawa","genres":["Manga","Slice of Life"],"rating":4,"description":"Agriculture school comedy and learning."},
    {"title":"Assassination Classroom","author":"Yūsei Matsui","genres":["Manga","Action"],"rating":5,"description":"A class training to kill their teacher."},
    {"title":"Bunny Drop","author":"Yumi Unita","genres":["Manga","Slice of Life"],"rating":5,"description":"A heartfelt story of unexpected parenthood."},
    {"title":"March Comes in Like a Lion","author":"Chica Umino","genres":["Manga","Drama"],"rating":5,"description":"Shogi, trauma, and slow healing."},
    {"title":"Monster","author":"Naoki Urasawa","genres":["Manga","Thriller"],"rating":5,"description":"A surgeon hunts a monster he saved."},
    {"title":"Pluto","author":"Naoki Urasawa","genres":["Manga","Sci-Fi"],"rating":5,"description":"Reimagining of Astro Boy's arc, dark and thoughtful."},
    {"title":"20th Century Boys","author":"Naoki Urasawa","genres":["Manga","Mystery"],"rating":5,"description":"Childhood friends vs a cult and apocalyptic plot."},
    {"title":"Parasyte","author":"Hitoshi Iwaaki","genres":["Manga","Horror"],"rating":5,"description":"Alien parasites and a boy fighting for coexistence."},
    {"title":"Ajin","author":"Gamon Sakurai","genres":["Manga","Sci-Fi"],"rating":4,"description":"Immortal beings and government hunting."},
    {"title":"Oyasumi Punpun","author":"Inio Asano","genres":["Manga","Drama"],"rating":5,"description":"A dark, surreal coming-of-age tale."},
    {"title":"Golden Kamuy","author":"Satoru Noda","genres":["Manga","Historical"],"rating":5,"description":"Treasure hunt in Hokkaido with Ainu culture."},
    {"title":"Dorohedoro","author":"Q Hayashida","genres":["Manga","Dark Fantasy"],"rating":5,"description":"Weird, violent, and wildly imaginative."},
    {"title":"Land of the Lustrous","author":"Haruko Ichikawa","genres":["Manga","Fantasy"],"rating":5,"description":"Gem-like beings and existential themes."},
    {"title":"Cells at Work!","author":"Akane Shimizu","genres":["Manga","Educational"],"rating":4,"description":"Anthropomorphic cells keeping the body alive."},
    {"title":"Made in Abyss","author":"Akihito Tsukushi","genres":["Manga","Fantasy"],"rating":5,"description":"A wondrous but brutal descent into the Abyss."},
    {"title":"Kakegurui","author":"Homuromi Yamamoto","genres":["Manga","Psychological"],"rating":4,"description":"High-stakes gambling at an elite academy."},
    {"title":"K-On!","author":"Kakifly","genres":["Manga","Slice of Life"],"rating":4,"description":"Light music club and cute band antics."},
    {"title":"Azumanga Daioh","author":"Kiyohiko Azuma","genres":["Manga","Comedy"],"rating":5,"description":"Slice-of-life school comedy."},
    {"title":"Nichijou","author":"Keiichi Arawi","genres":["Manga","Comedy"],"rating":5,"description":"Absurdist school-day sketches."},
    {"title":"Sayonara, Zetsubou-Sensei","author":"Kozueko Morimoto","genres":["Manga","Dark Comedy"],"rating":4,"description":"A pessimistic teacher and satire."},
    {"title":"Blood Blockade Battlefront","author":"Yasuhiro Nightow","genres":["Manga","Action"],"rating":4,"description":"Supernatural city of chaos."},
    {"title":"Great Teacher Onizuka","author":"Toru Fujisawa","genres":["Manga","Comedy"],"rating":5,"description":"A former biker becomes an unconventional teacher."},
    {"title":"Saint Seiya","author":"Masami Kurumada","genres":["Manga","Mythology"],"rating":4,"description":"Knights with star-based armor."},
    {"title":"Detective Conan","author":"Gosho Aoyama","genres":["Manga","Mystery"],"rating":5,"description":"A child detective solves mysteries."},
    {"title":"The Girl From the Other Side","author":"Nagabe","genres":["Manga","Fantasy"],"rating":5,"description":"A haunting fairytale comic."},
    {"title":"Children of the Sea","author":"Daisuke Igarashi","genres":["Manga","Magical Realism"],"rating":4,"description":"Oceanic mystery and beautiful art."},
    {"title":"A Silent Voice","author":"Yoshitoki Oima","genres":["Manga","Drama"],"rating":5,"description":"Bullying, redemption, and voice."},
    {"title":"The Breaker","author":"Jeon Geuk-jin","genres":["Manhwa","Martial Arts"],"rating":5,"description":"Manhwa martial-arts power fantasy."},
    {"title":"Solo Leveling","author":"Chugong","genres":["Manhwa","Action"],"rating":5,"description":"A weak hunter grows to be the strongest."},
    {"title":"Tower of God","author":"S.I.U.","genres":["Manhwa","Fantasy"],"rating":5,"description":"Mysterious tower full of trials."},
    {"title":"Noblesse","author":"Son Jeho","genres":["Manhwa","Supernatural"],"rating":4,"description":"Vampire nobles in modern world."},
    {"title":"The God of High School","author":"Yongje Park","genres":["Manhwa","Action"],"rating":4,"description":"Martial arts tournament with cosmic stakes."},
    {"title":"Sweet Home","author":"Kim Carnby","genres":["Webtoon","Horror"],"rating":4,"description":"Apocalyptic monster horror webtoon."},
    {"title":"Lookism","author":"Park Tae-jun","genres":["Manhwa","Drama"],"rating":4,"description":"Body-switching and social commentary."},
    {"title":"Hardcore Leveling Warrior","author":"Sehoon Kim","genres":["Webtoon","GameFi"],"rating":4,"description":"Game-themed power fantasy webtoon."},
    {"title":"The Beginning After The End","author":"TurtleMe","genres":["Web Novel/Manhwa","Fantasy"],"rating":5,"description":"Reincarnation and high-fantasy kingdom building."},
    {"title":"Re:Zero − Starting Life in Another World","author":"Tappei Nagatsuki","genres":["Light Novel","Isekai"],"rating":5,"description":"A man looping death in a fantasy world."},
    {"title":"KonoSuba","author":"Natsume Akatsuki","genres":["Light Novel","Comedy"],"rating":4,"description":"Isekai satire with comedic party."},
    {"title":"Overlord","author":"Kugane Maruyama","genres":["Light Novel","Isekai"],"rating":4,"description":"An overlord trapped inside a game."},
    {"title":"That Time I Got Reincarnated as a Slime","author":"Fuse","genres":["Light Novel","Isekai"],"rating":4,"description":"A man reborn as a powerful slime."},
    {"title":"Sword Art Online","author":"Reki Kawahara","genres":["Light Novel","Isekai"],"rating":4,"description":"Trapped inside a VRMMO death game."},
    {"title":"No Game No Life","author":"Yuu Kamiya","genres":["Light Novel","Fantasy"],"rating":4,"description":"Gamer siblings challenge godlike rules."},
    {"title":"Log Horizon","author":"Mamare Touno","genres":["Light Novel","Isekai"],"rating":4,"description":"Strategy-driven trapped-in-game story."},
    {"title":"Bakuman","author":"Tsugumi Ohba & Takeshi Obata","genres":["Manga","Slice of Life"],"rating":5,"description":"Two teens chase the dream to make manga."},
    {"title":"Slam Dunk","author":"Takehiko Inoue","genres":["Manga","Sports"],"rating":5,"description":"Basketball, passion, and growth."},
    {"title":"Kuroko's Basketball","author":"Tadatoshi Fujimaki","genres":["Manga","Sports"],"rating":4,"description":"Tactical basketball with a phantom player."},
    {"title":"Haikyuu!!","author":"Haruichi Furudate","genres":["Manga","Sports"],"rating":5,"description":"Volleyball underdog story full of heart."},
    {"title":"Eyeshield 21","author":"Riichiro Inagaki","genres":["Manga","Sports"],"rating":4,"description":"American football shonen with speed."},
    {"title":"Hikaru no Go","author":"Yumi Hotta","genres":["Manga","Game"],"rating":5,"description":"A ghost and a boy revive the game of Go."},
    {"title":"Prince of Tennis","author":"Takeshi Konomi","genres":["Manga","Sports"],"rating":4,"description":"Tennis prodigy competition."},
    {"title":"Skip Beat!","author":"Yoshiki Nakamura","genres":["Manga","Romcom"],"rating":5,"description":"Revenge and showbiz transformation."},
    {"title":"Black Butler","author":"Yana Toboso","genres":["Manga","Dark"],"rating":5,"description":"A demon butler and Victorian mysteries."},
    {"title":"Pandora Hearts","author":"Jun Mochizuki","genres":["Manga","Fantasy"],"rating":5,"description":"Dark fairy-tale mystery."},
    {"title":"Nana","author":"Ai Yazawa","genres":["Manga","Drama"],"rating":5,"description":"Two women named Nana and their lives in Tokyo."},
    {"title":"Honey and Clover","author":"Chica Umino","genres":["Manga","Slice of Life"],"rating":5,"description":"Art school life and bittersweet growth."},
    {"title":"Beck","author":"Harold Sakuishi","genres":["Manga","Music"],"rating":4,"description":"Coming-of-age rock band manga."},
    {"title":"Eden: It's an Endless World!","author":"Hiroki Endo","genres":["Manga","Sci-Fi"],"rating":5,"description":"Philosophical post-apocalyptic epic."},
    {"title":"A Silent Voice (Koe no Katachi) - movie novelization","author":"Yoshitoki Oima","genres":["Manga/Novel","Drama"],"rating":5,"description":"Bullying, redemption, and empathy."},
    {"title":"Wolf Children (novel)","author":"Mamoru Hosoda","genres":["Novel","Fantasy"],"rating":4,"description":"Raising half-wolf children in humanity."},
    {"title":"Your Name (novel)","author":"Makoto Shinkai","genres":["Novel","Romance"],"rating":5,"description":"Body-switching romance across time."},
    {"title":"Spirited Away (novel)","author":"Hayao Miyazaki","genres":["Novel","Fantasy"],"rating":5,"description":"A girl's adventure in the spirit world."},
    {"title":"Monster (novelization)","author":"Naoki Urasawa","genres":["Novel","Thriller"],"rating":5,"description":"Intense psychological thriller tale."},
    {"title":"The Girl Who Leapt Through Time","author":"Yasutaka Tsutsui","genres":["Novel","Sci-Fi"],"rating":5,"description":"Classic time-leap story."},
    {"title":"Mushishi","author":"Yuki Urushibara","genres":["Manga","Supernatural"],"rating":5,"description":"Quiet supernatural folktales."},
    {"title":"Usagi Drop","author":"Yumi Unita","genres":["Manga","Slice of Life"],"rating":5,"description":"Parenting and gentle family drama."},
    {"title":"Yotsuba&!","author":"Kiyohiko Azuma","genres":["Manga","Comedy"],"rating":5,"description":"Childhood wonder in perfect slices of life."},
    {"title":"Monster Hunter Orage","author":"Hiro Mashima","genres":["Manga","Fantasy"],"rating":4,"description":"Game-inspired hunting adventures."},
    {"title":"Gleipnir","author":"Sun Takeda","genres":["Manga","Supernatural"],"rating":4,"description":"Shapeshifting and survival themes."},
    {"title":"D.Gray-man","author":"Katsura Hoshino","genres":["Manga","Dark Fantasy"],"rating":4,"description":"Exorcists vs akuma."},
    {"title":"Black Lagoon","author":"Rei Hiroe","genres":["Manga","Action"],"rating":4,"description":"Mercenary life and moral grey zones."},
    {"title":"Feng Shen Ji (manhua)","author":"Zheng Jian He","genres":["Manhua","Fantasy"],"rating":4,"description":"Epic mythological battles."},
    {"title":"Blade of the Immortal","author":"Hiroaki Samura","genres":["Manga","Samurai"],"rating":5,"description":"A cursed swordsman and redemption."},
    {"title":"Sanctuary","author":"Sho Fumimura","genres":["Manga","Crime"],"rating":4,"description":"Yakuza and political intrigue."},
    {"title":"Violet Evergarden (novel)","author":"Kana Akatsuki","genres":["Light Novel","Drama"],"rating":5,"description":"Letters, healing, and emotion."},
    {"title":"Planetes","author":"Makoto Yukimura","genres":["Manga","Sci-Fi"],"rating":5,"description":"Space garbage collectors and humanity."},
    {"title":"Arakawa Under the Bridge","author":"Nakashima Hikaru","genres":["Manga","Comedy"],"rating":4,"description":"Bizarre people and absurd humor."},
    {"title":"Psycho-Pass (novel)","author":"Gen Urobuchi","genres":["Novel","Sci-Fi"],"rating":4,"description":"Crime and a dystopian surveillance system."},
    {"title":"The Tatami Galaxy","author":"Tomihiko Morimi","genres":["Novel","Surreal"],"rating":5,"description":"A surreal college-life tale."},
    {"title":"Nicholas Nickleby (manga adaptation)","author":"Various","genres":["Manga","Classic"],"rating":3,"description":"Classic literature in manga form."},
    {"title":"Black Lagoon: Roberta's Blood Trail (OVA novel)","author":"Rei Hiroe","genres":["Novel","Action"],"rating":4,"description":"Extended violent tales of Lagoon Company."},
    {"title":"Oshi no Ko","author":"Aka Akasaka","genres":["Manga","Drama"],"rating":5,"description":"Idol industry with dark twists."},
    {"title":"Blue Exorcist","author":"Kazue Kato","genres":["Manga","Supernatural"],"rating":4,"description":"Brothers facing demon heritage."},
    {"title":"Welcome to the NHK","author":"Tatsuhiro Satou","genres":["Novel","Drama"],"rating":4,"description":"A dark comedy about hikikomori life."},
    {"title":"Kenshi Yonezu (biography)","author":"Various","genres":["Music","Biography"],"rating":3,"description":"Artist biography (placeholder)."},
    {"title":"Made in Abyss: Official Guidebook","author":"Akihito Tsukushi","genres":["Guide","Fantasy"],"rating":4,"description":"World details from the Abyss."},
    {"title":"The Way of the Househusband (manga)","author":"Kousuke Oono","genres":["Manga","Comedy"],"rating":4,"description":"An ex-yakuza becomes a devoted househusband."},
    {"title":"Kinnikuman (ultimate muscle)","author":"Yudetamago","genres":["Manga","Comedy"],"rating":3,"description":"Classic wrestling comedy shonen."},
    {"title":"Kimi no Iru Machi (A Town Where You Live)","author":"Kaito","genres":["Manga","Romance"],"rating":3,"description":"Long-distance romance and drama."},
    {"title":"Air Gear","author":"Oh! Great","genres":["Manga","Action"],"rating":4,"description":"Extreme inline skating gang battles."},
    {"title":"NANA to Kaoru","author":"Ryuta Amazume","genres":["Manga","Romance"],"rating":3,"description":"A quirky romantic BDSM-tinged comedy-drama."},
    {"title":"Real (Takehiko Inoue)","author":"Takehiko Inoue","genres":["Manga","Sports"],"rating":5,"description":"Wheelchair basketball and human resilience."},
    {"title":"Kokkoku","author":"Seita Horio","genres":["Manga","Supernatural"],"rating":4,"description":"Time-stopping mystery thriller."},
    {"title":"Shaman King","author":"Hiroyuki Takei","genres":["Manga","Adventure"],"rating":4,"description":"Shaman fights and spirit partners."},
    {"title":"Air (Visual Novel novelization)","author":"Key","genres":["Novel","Drama"],"rating":4,"description":"Deeply emotional visual-novel story."},
    {"title":"Slam Dunk: The Short Stories","author":"Takehiko Inoue","genres":["Manga","Sports"],"rating":4,"description":"Extra tales and slice-of-life sketches."},
    {"title":"Gunslinger Girl","author":"Yu Aida","genres":["Manga","Drama"],"rating":4,"description":"Young cyborg assassins and tragic stories."},
    {"title":"Katanagatari (novel)","author":"Nisio Isin","genres":["Light Novel","Action"],"rating":4,"description":"A stylistic sword quest."},
    {"title":"The Rising of the Shield Hero (novel)","author":"Aneko Yusagi","genres":["Light Novel","Isekai"],"rating":4,"description":"A falsely accused hero survives in another world."},
    {"title":"Btooom!","author":"Junya Inoue","genres":["Manga","Survival"],"rating":4,"description":"Survival game on an island with bombs."},
    {"title":"Terra Formars","author":"Yu Sasuga","genres":["Manga","Sci-Fi"],"rating":3,"description":"Genetically evolved cockroaches vs humanity."},
    {"title":"Kimi to 100 Kaime no koi (100th Love with You)","author":"Various","genres":["Manga","Romance"],"rating":3,"description":"Romantic time-loop themes."},
    {"title":"Mieruko-chan","author":"Tomoki Izumi","genres":["Manga","Horror"],"rating":4,"description":"A girl who sees monsters but pretends not to."},
    {"title":"Sakamoto Days","author":"Yuuto Suzuki","genres":["Manga","Action"],"rating":4,"description":"Retired hitman family-slice action."},
    {"title":"Frieren: Beyond Journey's End","author":"Kanehito Yamada","genres":["Manga","Fantasy"],"rating":5,"description":"An immortal mage reflecting on a hero's journey."},
    {"title":"SPY×FAMILY","author":"Tatsuya Endo","genres":["Manga","Comedy"],"rating":5,"description":"A spy family with secrets and heart."},
    {"title":"Blue Lock","author":"Muneyuki Kaneshiro","genres":["Manga","Sports"],"rating":5,"description":"Cutthroat soccer training for a superstar."},
    {"title":"Magi: The Labyrinth of Magic","author":"Shinobu Ohtaka","genres":["Manga","Adventure"],"rating":4,"description":"A fantasy epic inspired by Arabian Nights."},
    {"title":"Astra: Lost in Space","author":"Kenta Shinohara","genres":["Manga","Sci-Fi"],"rating":4,"description":"Kids thrown to space fight to survive."},
    {"title":"Sengoku Youko","author":"Satoshi Mizukami","genres":["Manga","Fantasy"],"rating":4,"description":"Immortal wanderer in fantastical Japan."},
    {"title":"Ajin: Demi-Human","author":"Gamon Sakurai","genres":["Manga","Supernatural"],"rating":4,"description":"Immortal beings hunted by governments."},
    {"title":"March Comes in Like a Lion: Short Stories","author":"Chica Umino","genres":["Manga","Slice of Life"],"rating":5,"description":"Extras from the main series."},
    {"title":"The Apothecary Diaries","author":"Natsu Hyuuga","genres":["Light Novel","Historical"],"rating":5,"description":"Court intrigue and medicine in a palace."},
    {"title":"The Twelve Kingdoms (novel)","author":"Fuyumi Ono","genres":["Light Novel","Fantasy"],"rating":5,"description":"Epic alternate-world fantasy."},
    {"title":"Magi: Sinbad no Bouken","author":"Shinobu Ohtaka","genres":["Manga","Adventure"],"rating":4,"description":"Spin-off focusing on Sinbad's adventures."},
    {"title":"Shouwa Genroku Rakugo Shinju","author":"Haruko Kumota","genres":["Manga","Drama"],"rating":5,"description":"The art and life of rakugo performers."},
    {"title":"Komi Can't Communicate","author":"Tomohito Oda","genres":["Manga","Comedy"],"rating":5,"description":"A girl with social anxiety and the kindness around her."},
    {"title":"Smile Down the Runway","author":"Kota Nozuki","genres":["Manga","Slice of Life"],"rating":4,"description":"Fashion dreams against social obstacles."},
    {"title":"Hikaru no Go: Extra Matches","author":"Yumi Hotta","genres":["Manga","Game"],"rating":4,"description":"More Go matches and character development."},
    {"title":"Otoyomegatari (A Bride's Story)","author":"Kaoru Mori","genres":["Manga","Historical"],"rating":5,"description":"Love stories set on the Silk Road."},
    {"title":"Heike Monogatari (manga)","author":"Hiroaki Samura","genres":["Manga","Historical"],"rating":4,"description":"A retelling of classic Heike tales."},
    {"title":"Shokugeki no Soma (Food Wars)","author":"Yuto Tsukuda","genres":["Manga","Food"],"rating":4,"description":"High-stakes cooking battles."},
    {"title":"Komi-san wa, Komyushou desu (Komi Can't Communicate) - extras","author":"Tomohito Oda","genres":["Manga","Comedy"],"rating":5,"description":"Side stories and character moments."},
    {"title":"Kaiju No. 8","author":"Naoya Matsumoto","genres":["Manga","Action"],"rating":5,"description":"Monster extermination with a twist."},
    {"title":"Frieren: Beyond Journey's End - extras","author":"Kanehito Yamada","genres":["Manga","Fantasy"],"rating":5,"description":"Short extras exploring characters."},
    {"title":"Blue Period: Extra Sketches","author":"Tsubasa Yamaguchi","genres":["Manga","Art"],"rating":4,"description":"Art student sketches and side pieces."},
    {"title":"The Legendary Hero Is Dead! (novel spin)","author":"Various","genres":["Light Novel","Comedy"],"rating":3,"description":"Parody of typical hero tales."},
    {"title":"Kumo desu ga, Nani ka? (So I'm a Spider, So What?)","author":"Okina Baba","genres":["Light Novel","Isekai"],"rating":4,"description":"A girl reborn as a spider monster in a dungeon."},
    {"title":"Shadow of the Moon (manga)","author":"Various","genres":["Manga","Fantasy"],"rating":3,"description":"Anthology and fantasy shorts."},
]

# Insert into DB, skip duplicates
added = 0
skipped = 0

for info in books_data:
    title = info.get("title").strip()
    author = info.get("author").strip()
    if Book.objects.filter(title=title, author=author).exists():
        skipped += 1
        print("SKIPPED:", title)
        continue

    b = Book.objects.create(
        title=title,
        author=author,
        description=info.get("description", "")[:2000],
        rating=info.get("rating", None)
    )

    for g in info.get("genres", []):
        g_obj, _ = Genre.objects.get_or_create(name=g)
        b.genres.add(g_obj)

    added += 1
    print("ADDED:", title)

print("\nFinished.")
print("Added:", added)
print("Skipped:", skipped)

# After running: confirm total books count
total = Book.objects.count()
print("Total books in DB now:", total)
