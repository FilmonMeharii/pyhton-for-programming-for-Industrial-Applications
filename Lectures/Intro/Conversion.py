

price_usd = float(input('Price in USD: '))
rate = float(input('Exchange rate (SEK per USD): '))

price_sek = rate * price_usd
print(f'Price in SEK: {price_sek}')


