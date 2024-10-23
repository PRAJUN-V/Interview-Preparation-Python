from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Add one day to get tomorrow's date
tomorrow = today + timedelta(days=10)

# Print in 'YYYY-MM-DD' format
print(tomorrow.strftime('%Y-%m-%d'))
