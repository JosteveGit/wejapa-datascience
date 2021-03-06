import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city: ").lower()
    # get user input for month (all, january, february, ... , june)
    month = input("Enter the month: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day: ").capitalize()
    if day == "All":
        day = day.lower()

    print('-' * 40)
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
    df = pd.read_csv(city + ".csv")

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #
    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is {}".format(most_common_month))

    # display the most common day of week
    most_common_day_of_the_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is {}".format(most_common_day_of_the_week))

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    # find the most common hour (from 0 to 23)
    popular_hour = pd.DatetimeIndex(df['Start Time']).hour.value_counts().idxmax()
    print("The most common hour is {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is {}".format(df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print("The most commonly used end station is {}".format(df['End Station'].value_counts().idxmax()))

    # display most frequent combination of start station and end station trip
    output = \
        df.groupby(['Start Station', 'End Station']).count().sort_values(by=['Start Station', 'End Station'],
                                                                         axis=0).iloc[
            0]
    print("The mmost frequent combination of start station and end station trip {}".format(
        output.value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print(df.columns)

    # display total travel time
    s = pd.to_datetime(df['Start Time']) - pd.to_datetime(df['End Time'])
    tt = s.dt.seconds / 60

    print("Total travel time is {}".format(tt.sum()))

    # display mean travel time
    print("Total mean time is {}".format(tt.mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of the user types: {}".format(user_types))

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print("The counts gender: {}".format(gender))

    # Display earliest, most recent, and most common year of birth
    by = pd.to_datetime(df['Birth Year'])
    earliest = by.min()
    most_recent = by.max()
    most_common = by.value_counts().idxmax()

    print("This earliest year of birth is {}".format(earliest))
    print("This most recent year of birth is {}".format(most_recent))
    print("This most common year of birth is {}".format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
