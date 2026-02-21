

while True:
    offer = int(input('What is your offer? '))
    if offer >= 150:
        print(f'offer accepted. Sold for {offer} SEK')
        break
    suggestion = 150 + (150 - offer)
    print(f'offer too low. How about {suggestion} ')
     