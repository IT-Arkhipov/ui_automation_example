import random
from datetime import datetime, timedelta


def random_date(start_year=1900, end_year=2021, date_format: str = "%d %B %Y"):
    # Generate a random date between the start and end years
    start_date = datetime(year=start_year, month=1, day=1)
    end_date = datetime(year=end_year, month=12, day=31)

    # Calculate the difference in days
    delta_days = (end_date - start_date).days

    # Generate a random number of days to add to the start date
    random_days = random.randint(0, delta_days)

    # Create the random date
    _random_date = start_date + timedelta(days=random_days)

    formatted_date = _random_date.strftime(date_format)

    return formatted_date
