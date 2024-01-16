#Converts time to Frecnch revolutionary dates

# Part 1: Converting to decimal time
def get_decimal_time(conventional_hour, conventional_minute, conventional_second):
    total_seconds = conventional_hour * 3600 + conventional_minute * 60 + conventional_second
    decimal_hour = total_seconds // 10000
    total_seconds %= 10000
    decimal_minute = total_seconds // 100
    decimal_second = total_seconds % 100
    return f"{decimal_hour}:{decimal_minute}:{decimal_second}"

# Part 2: Converting to revolutionary dates
def get_french_month(gregorian_month):
    if gregorian_month == 1:
        return "Nivôse"
    elif gregorian_month == 2:
        return "Pluviôse"
    elif gregorian_month == 3:
        return "Ventôse"
    elif gregorian_month == 4:
        return "Germinal"
    elif gregorian_month == 5:
        return "Floréal"
    elif gregorian_month == 6:
        return "Prairial"
    elif gregorian_month == 7:
        return "Messidor"
    elif gregorian_month == 8:
        return "Thermidor"
    elif gregorian_month == 9:
        return "Fructidor"
    elif gregorian_month == 10:
        return "Vendémiaire"
    elif gregorian_month == 11:
        return "Brumaire"
    else:
        return "Frimaire"

def get_decimal_date(gregorian_month, gregorian_day, gregorian_year):
    revolutionary_month = get_french_month(gregorian_month)
    revolutionary_day = gregorian_day
    revolutionary_year = gregorian_year - 1792
    decade = (revolutionary_day - 1) // 10
    return f"{revolutionary_day} {revolutionary_month} Year {revolutionary_year}, Décade {decade + 1}"

# Part 3: Putting it all together
def get_french_datetime(gregorian_datetime_str):
    gregorian_datetime_parts = gregorian_datetime_str.split()
    time_parts = gregorian_datetime_parts[0].split(":")
    date_parts = gregorian_datetime_parts[1].split("/")

    conventional_hour = int(time_parts[0])
    conventional_minute = int(time_parts[1])
    conventional_second = int(time_parts[2])
    gregorian_month = int(date_parts[0])
    gregorian_day = int(date_parts[1])
    gregorian_year = int(date_parts[2])

    decimal_time = get_decimal_time(conventional_hour, conventional_minute, conventional_second)
    decimal_date = get_decimal_date(gregorian_month, gregorian_day, gregorian_year)

    return f"{decimal_time}\n{decimal_date}"


def main():
    gregorian_datetime = "16:07:46 03/22/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)

