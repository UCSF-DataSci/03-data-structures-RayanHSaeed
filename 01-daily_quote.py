#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
        'One day at a time.',
        'Keep moving forward.',
        'Small steps lead to big changes.',
        'Progress, not perfection.',
        'You’ve got this.',
        'Every day is a fresh start.',
        'Do what you can, with what you have.',
        'Be kind to yourself.',
        'Focus on the good.',
        'Stay patient and trust your journey.',
        'Choose joy.',
        'One step closer every day.',
        'Believe in your potential.',
        'You are stronger than you think.',
        'Embrace the process.'
]

def get_quote_of_the_day(quotes):
    todays_quote = random.choice(quotes)
    return todays_quote


if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))


# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt