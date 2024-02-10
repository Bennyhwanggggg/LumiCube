"""
Visualise live Bitcoin price swings.
"""

import requests


def get_price(from_currency, to_currency):
    r = requests.get("https://api.gemini.com/v1/pricefeed/"
        + from_currency + to_currency)
    price = float(r.json()[0]['price'])
    return price

initial = get_price('btc', 'usd')
prices = [initial for i in range(16)]
display.set_all(black)
while True:
    # Add the new price and remove the oldest one
    prices.append(get_price('btc', 'usd'))
    prices = prices[1:]
    step = 3.0
    led_colours = {}
    for x in range(0, len(prices)):
        y_value = int((prices[x] - min(prices))/step)
        for y in range(8):
            colour = white if y == y_value else black
            led_colours[x, y] = colour
    display.set_leds(led_colours)
    time.sleep(2)
