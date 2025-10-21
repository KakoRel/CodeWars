def life_predictor(birth_date):
    year, month, day = map(int, birth_date.split('-'))
    
    days_to_subtract = 280
    
    while days_to_subtract > 0:
        day -= 1
        
        if day == 0:
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            
            day = days_in_month(year, month)
        
        days_to_subtract -= 1
    
    return f"{year:04d}-{month:02d}-{day:02d}"

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

# Test with the given example
print(life_predictor("2000-09-18"))  # "1999-12-13"