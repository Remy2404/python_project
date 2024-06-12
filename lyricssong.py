import time

def print_lyrics():
    # Define the sections of the song with delays for the animation
    sections = [
        ("\n\nCause you're the one that I like, I can't deny\nEvery night you're on my mind\nSo, if I call you tonight\nWill you pick up and give me your time?\nMiss you every night, miss you all the time\nNo, I don't even know where to start\n\nCause you're the one that I like, I can't deny\nEverything I feel inside\nWill you tell me I'm the one\nThe one that inside of your heart\nUsed to brush aside, now I can't deny\nThat, baby, you're my special one\nCause you're the one that I like", 4),
        ("\n\nYou mean a lot to me\nCause you have made me believe\nHow love makes anything\nBetter than they used to be\nI'm not like this before\nYou make me wish for more\nOh, when you pass me by\nGirl, you give me butterflies", 3),
        ("\n\nCause you're the one that I like, I can't deny\nEvery night you're on my mind\nSo, if I call you tonight\nWill you pick up and give me your time?\nMiss you every night, miss you all the time\nNo, I don't even know where to start\n\nCause you're the one that I like, I can't deny\nEverything I feel inside\nWill you tell me I'm the one\nThe one that inside of your heart\nUsed to brush aside, now I can't deny\nThat, baby, you're my special one\nCause you're the one that I like", 4),
        ("\n\nCause everything slows down in time\n(Oh) I don't know what to say\nCause, girl, when you smile I'd fall for it again and again", 3)
    ]

    # Print each section with animation
    for section, delay in sections:
        for char in section:
            print(char, end='', flush=True)
            time.sleep(0.08)  # Adjust the delay to control the speed of the animation
        print()
        time.sleep(delay)  # Pause before printing the next section

# Call the function to print the lyrics
print_lyrics()
