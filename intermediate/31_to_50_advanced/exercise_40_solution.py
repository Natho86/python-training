# Exercise 40: Working with datetime Module - SOLUTION
# Difficulty: Intermediate-
# Concepts: datetime module, Date manipulation, Time calculations

from datetime import datetime, timedelta

# SOLUTION
def calculate_age(birth_date):
    """
    Calculate age from birth date.

    Args:
        birth_date: datetime object representing birth date

    Returns:
        int: Age in years
    """
    today = datetime.now()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred this year yet
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def days_until_birthday(birth_date):
    """
    Calculate days until next birthday.

    Args:
        birth_date: datetime object representing birth date

    Returns:
        int: Days until next birthday
    """
    today = datetime.now()
    # Get birthday for current year
    next_birthday = datetime(today.year, birth_date.month, birth_date.day)

    # If birthday already passed this year, use next year
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)

    days = (next_birthday - today).days
    return days, next_birthday

# Main program
print("=== DateTime Example ===")

# Current date and time
now = datetime.now()
print(f"Current date and time: {now}")
print(f"Formatted: {now.strftime('%B %d, %Y at %I:%M %p')}")

# Calculate age
birth_date = datetime(1990, 5, 15)
age = calculate_age(birth_date)
print(f"\nBirth date: {birth_date.strftime('%Y-%m-%d')}")
print(f"Age: {age} years old")

# Days until birthday
days, next_bday = days_until_birthday(birth_date)
print(f"Next birthday: {next_bday.strftime('%Y-%m-%d')}")
print(f"Days until birthday: {days} days")

# Different date formats
print("\n=== Date Formatting ===")
print(f"ISO format: {now.isoformat()}")
print(f"US format: {now.strftime('%m/%d/%Y')}")
print(f"European format: {now.strftime('%d/%m/%Y')}")
print(f"Full text: {now.strftime('%A, %B %d, %Y')}")
print(f"Time only: {now.strftime('%H:%M:%S')}")

"""
EXPLANATION:
1. datetime.now() gets the current date and time
2. datetime(year, month, day) creates a specific date
3. Subtracting dates gives a timedelta object with .days attribute
4. strftime() formats dates using format codes:
   - %Y: 4-digit year
   - %m: 2-digit month
   - %d: 2-digit day
   - %B: Full month name
   - %A: Full day name
   - %H: Hour (24-hour)
   - %I: Hour (12-hour)
   - %M: Minute
   - %S: Second
   - %p: AM/PM

Key Concepts:
- datetime module provides date and time functionality
- datetime objects can be compared and subtracted
- strftime() converts datetime to formatted string
- strptime() parses string to datetime
- timedelta represents a duration
"""

# More datetime examples
print("\n--- MORE DATETIME EXAMPLES ---")

# Parse string to datetime
date_string = "2024-12-25"
christmas = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {christmas}")

# Calculate date arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
last_month = now - timedelta(days=30)

print(f"\nTomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"Next week: {next_week.strftime('%Y-%m-%d')}")
print(f"30 days ago: {last_month.strftime('%Y-%m-%d')}")

# Working hours calculation
work_start = datetime(2024, 11, 27, 9, 0)  # 9:00 AM
work_end = datetime(2024, 11, 27, 17, 30)  # 5:30 PM
work_duration = work_end - work_start
print(f"\nWork duration: {work_duration}")
print(f"Work hours: {work_duration.total_seconds() / 3600:.1f} hours")

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

def date_difference_detailed(date1, date2):
    """
    Calculate detailed difference between two dates.

    Args:
        date1: First datetime object
        date2: Second datetime object

    Returns:
        str: Human-readable difference
    """
    # Ensure date1 is earlier
    if date1 > date2:
        date1, date2 = date2, date1

    years = date2.year - date1.year
    months = date2.month - date1.month
    days = date2.day - date1.day

    # Adjust for negative days
    if days < 0:
        months -= 1
        # Days in previous month
        if date2.month == 1:
            prev_month_days = 31
        else:
            prev_month = datetime(date2.year, date2.month - 1, 1)
            next_month = datetime(date2.year, date2.month, 1)
            prev_month_days = (next_month - prev_month).days
        days += prev_month_days

    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12

    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months != 1 else ''}")
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")

    return ", ".join(parts) if parts else "0 days"

def is_leap_year(year):
    """
    Check if a year is a leap year.

    Args:
        year: Year to check

    Returns:
        bool: True if leap year
    """
    # Divisible by 4 but not by 100, unless also divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test detailed date difference
start_date = datetime(2020, 3, 15)
end_date = datetime(2024, 11, 27)
difference = date_difference_detailed(start_date, end_date)
print(f"From {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}:")
print(f"Difference: {difference}")

# Test leap year function
print("\nLeap years:")
years_to_check = [2020, 2021, 2024, 2100, 2000]
for year in years_to_check:
    leap_status = "is" if is_leap_year(year) else "is not"
    print(f"{year} {leap_status} a leap year")

# Practical example: Project deadline tracker
print("\n--- PROJECT DEADLINE TRACKER ---")

def deadline_status(deadline_date, project_name):
    """Check status of project deadline."""
    now = datetime.now()
    time_left = deadline_date - now

    if time_left.days < 0:
        return f"⚠️ {project_name}: OVERDUE by {abs(time_left.days)} days!"
    elif time_left.days == 0:
        return f"🔥 {project_name}: DUE TODAY!"
    elif time_left.days <= 3:
        return f"⚡ {project_name}: Due in {time_left.days} days (URGENT)"
    else:
        return f"✓ {project_name}: Due in {time_left.days} days"

projects = [
    ("Website Redesign", datetime(2024, 12, 1)),
    ("Report Submission", datetime(2024, 11, 28)),
    ("Client Presentation", datetime(2025, 1, 15)),
]

print("\nProject Deadlines:")
for name, deadline in projects:
    print(deadline_status(deadline, name))

# Timezone-aware datetime (bonus)
print("\n--- BONUS: TIMEZONE AWARENESS ---")
try:
    from datetime import timezone
    # UTC time
    utc_now = datetime.now(timezone.utc)
    print(f"UTC time: {utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
except ImportError:
    print("Timezone features require additional setup")
