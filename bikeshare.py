import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data from chicago, new york city or washington?\n').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print('Please key in a correct city name')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to see data from?\nPlease choose from january, february, march, april, may, june or all.\n').lower()
    while month not in('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print('Please key in a correct month name\n')
        month = input('Which month would you like to see data from?\nPlease choose from january, february, march, april, may, june or all.\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = input('\nSelect the day of the week you want to filter the bikeshare data by. \n Choose from the list: (sunday, monday, tuesday, wednesday, thursday, friday, saturday, all): ').lower()
    while True:
        if day in days:
            print('\nWe are working with {} data\n'.format(day.upper()))
            break
        else:
            print('\nPlease choose a valid day of the week from the list (sunday, monday, tuesday, wednesday, thursday, friday, saturday, all)\n').lower()
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    data_file = CITY_DATA[city]
    df = pd.read_csv(data_file)

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()[0]
    print('The most common day of the week is:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used end station is:', end_station)

    # display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'] + ' ' 'to' ' ' + df['End Station']
    frequent_combination = df['Start_End'].mode()[0]
    print('Most frequent start and end station is:', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration =df['Trip Duration'].sum()
    print('The total travel time is:', trip_duration)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean of the travel time is:', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # Display counts of user types
        count_usertypes = df['User Type'].value_counts()
        print('Count of user types is:\n', count_usertypes)

        # Display counts of gender
        count_gender= df['Gender'].value_counts()
        print('Count of gender is:\n', count_gender)

    # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent= df['Birth Year'].max()
        most_common= df['Birth Year'].mode()[0]

        print('The earliest birth day is:', earliest)
        print('The most recent birth day is:', most_recent)
        print('The most common birth year is:', most_common)

    except:
        print('the data for washington is not available.')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
    """Displays 5 lines of raw data"""

    i = 0
    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no:').lower()
        if answer =='yes':
            print(df.iloc[i:i+5])
            i += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
