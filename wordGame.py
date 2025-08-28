#Imported Modules
import pygame, random
pygame.init() #Initialising Pygame

#Screen Size
WIDTH, HEIGHT = 500,500

#List of random words genereated with Copilot
WORDS = ["horizon", "adventure", "zephyr", "mindfulness", "twilight", "optimistic", "cloud", "journey", "dazzling", "glacier", "whisper", "brilliant", "ocean", "flame", "miracle", "radiant", "victory", "compassion", "forest", "flourish", "exuberant", "paradise", "love", "sunrise", "courage", "delight", "xylophone", "serene", "notebook", "ambition", "wisdom", "whimsical", "penguin", "kindness", "gratitude", "triumph", "unique", "youthful", "justice", "yearning", "inspire", "ladder", "yellow", "freedom", "jewel", "resilience", "glorious", "wisdom", "luminous", "hopeful", "river", "balance", "nurture", "honesty", "ocean", "harmony", "resplendent", "quiver", "generosity", "xenophobia", "radiance", "serene", "uplifting", "star", "horizon", "understanding", "destiny", "ambitious", "reflective", "joyful", "laughter", "quality", "thoughtfulness", "tenacious", "gracious", "wondrous", "zeal", "patience", "exhilarating", "yearning", "vibrancy", "determined", "inquisitive", "kindhearted", "courageous", "wonder", "fortitude", "majestic", "phenomenal", "loyal", "charismatic", "mindful", "embracing", "hospitable", "noble", "peaceful", "innovative", "reliable", "adventurous", "tenacity", "fearless", "trustworthy", "generous", "optimism", "extraordinary", "ambitious", "noble-hearted", "tranquil", "inspired", "benevolence", "lively", "thoughtful", "reliable", "resilient", "humble", "enthusiastic", "kindness", "exemplary", "genuine", "knowledgeable", "diligence", "compassionate", "meticulous", "mindfulness", "radiance", "steadfast", "inspiring", "uplifted", "unwavering", "transformative", "bountiful", "imaginative", "fearless", "lightning", "radiant", "nurturing", "appreciative", "enlightened", "overjoyed", "zealous", "liberated", "uplifting", "sympathetic", "luminous", "selfless", "spirited", "adventurous", "harmonious", "exhilarating", "sublime", "integrity", "motivated", "brilliant", "dynamic", "jubilant", "successful", "benevolent", "accomplish", "uplifting", "glorious", "empathetic", "trailblazing", "compassionate", "majestic", "purposeful", "phenomenal", "meaningful", "cheerful", "bold", "prudent", "steadfast", "versatile", "uplifting", "joyous", "sincere", "graceful", "diligence", "accomplished", "radiant", "unbiased", "knowledge-seeking", "brave", "warmhearted", "extraordinary", "liberated", "inquisitive", "collaborative", "intuitive", "visionary", "trustworthy", "trailblazing", "integrity", "limitless", "zenith", "creative", "perseverance", "flawless", "zen-like", "wholehearted", "charismatic", "benevolent", "vigilant", "thoughtful", "proactive", "exemplary", "fearless", "remarkable", "principled", "resilient", "dedicated", "logical", "faithful", "motivated", "compassionate", "selfless", "insightful", "genuine", "dedicated", "enchanting", "enthusiastic", "successful", "fearless", "luminous", "trustworthy", "meticulous", "honest", "keen-eyed", "steadfast", "extraordinary", "prudent", "trailblazing", "vivacious", "intuitive", "loyal", "exhilarating", "quality-driven", "exuberant", "uplifted", "unwavering", "serene", "reflective", "inspiring", "radiance", "passionate", "perseverance", "accomplish", "devoted", "sympathetic", "expressive", "benevolence", "adventurous", "courageous", "innovative", "knowledgeable", "judicious", "resplendent", "justice", "determined", "meaningful", "cheerful", "extraordinary", "brilliant", "trailblazing", "purposeful", "faithful", "radiant", "passionate", "mindful", "uplifting", "fascinating", "empowered", "limitless", "zeal", "diligence", "insightful", "ambitious", "remarkable", "perceptive", "hopeful", "harmonious", "expressive", "delight", "luminary", "breathtaking", "wondrous", "luminous", "compassionate", "sublime", "inquisitive", "joyful", "enthusiastic", "lighthearted", "exuberant", "mindful", "extraordinary", "successful", "empathetic", "ambitious", "visionary", "dedicated", "curious", "proactive", "bold", "determined", "transformative", "creative", "brave", "cheerful", "compassionate", "glorious", "wholehearted", "uplifting", "honest", "insightful", "loyal", "brilliant", "sympathetic", "innovative", "radiant", "exemplary", "flourishing", "tenacious", "charismatic", "dedicated", "remarkable", "limitless", "adventurous", "passionate", "principled", "trailblazing", "perseverance", "energetic", "jubilant", "meaningful", "dynamic", "tranquil", "zealous", "harmonious", "selfless", "wondrous", "radiance", "reflective", "compassionate", "resilient", "uplifted", "intuitive", "proactive", "glorious", "exhilarating", "extraordinary", "diligence", "serene", "brilliant", "joyful", "knowledgeable", "perseverance", "cheerful", "expressive", "fearless", "limitless", "remarkable", "honest", "dedicated", "compassionate", "hopeful", "limitless", "trailblazing"]

#inputs all selected words into the array
selected_words = []

#used for the timer, score and lives
current_time, scoreCount, lives_number = 0, 0, 3
FPS = 60 #Frame Rate

#Creating the window page with text and fonts wherever necessary
window = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Word Game")
clock = pygame.time.Clock()
text = pygame.font.SysFont("Comic Sans MS", 20, "Bold")
heading = pygame.font.SysFont("Comic Sans MS", 40, "Bold")

#Need to create new button designs and then blit them into the system
newButton = pygame.image.load("New Button.jpg").convert_alpha()
seenButton = pygame.image.load("Seen.png").convert_alpha()
image_size = (150, 150) #Size of images

word = random.choice(WORDS) #A word is randomised initally

#Transformed the images
newButton = pygame.transform.scale(newButton, image_size)
seenButton = pygame.transform.scale(seenButton, image_size)

def draw():
    #Globalised variables to randomsie a new word and to top the timer
    global wordFont, word, gameOver
    scoreText, endingText = "", ""
    
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (0, 50, WIDTH, 10))
    livesCounter = text.render(("Lives: " + str(lives_number)), 1, (255, 255, 255))
    scoreCounter = text.render(("Score: " + str(scoreCount)), 1, (255, 255, 255))
    formattedTime = "{:02}:{:02}".format(current_time // 60000 % 60, current_time // 1000 % 60) #Needed help with formatting times in pygame
    timerText = text.render(("Time: " + formattedTime), 1, (255, 255, 255))
    
    scoreText = ("Score: " + str(scoreCount))
    timeText = ("Time: " + str(current_time // 1000))
    
    wordFont = text.render((word), 1, (255, 255, 255)) #Writing the text with the specified font
    
    #Used to stop the front-end of the game whilst the window runs normally
    if lives_number == 0:
        endingText = ("GAME OVER!!!")
        over = heading.render(endingText, 1, (255, 255, 255))
        window.blit(over, (150 - len(endingText), 250 - len(endingText)))
        wordFont.set_alpha(0) #Used to hide the text
        newButton.set_alpha(0) #Used to hide button
        seenButton.set_alpha(0) #Used to hide button
        gameOver = True
    
    #Displays all information with the use of blit and updating each time (the values for placing the items are hardcoded)
    window.blit(wordFont, (200 + len(word), 200))
    window.blit(livesCounter, (10, 0))
    window.blit(scoreCounter, ((WIDTH - (len(scoreText)) - 100, 0)))
    window.blit(timerText, (WIDTH - len(timeText) - 300, 0))
    window.blit(newButton, (100, 250))
    window.blit(seenButton, (300, 250))
    
    pygame.display.update()

run, gameOver = True, False

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and lives_number != 0:
            new_rect = pygame.Rect(100, 300, 150, 150)
            seen_rect = pygame.Rect(300, 300, 150, 150)
            backGround_rect = pygame.Rect(0, 50, WIDTH, HEIGHT-50)
            
            if new_rect.collidepoint(event.pos) and word not in selected_words:
                scoreCount += 1
            
            elif seen_rect.collidepoint(event.pos) and word in selected_words:
                scoreCount += 1
            
            else:
                lives_number -= 1
            
            selected_words.append(word)
            word = random.choice(WORDS)

    #Needed help with running the timer
    if not gameOver:
        current_time = pygame.time.get_ticks()

        draw()
