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


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        city_name = input("input a city name: ").lower()
        if city_name == "chicago" or city_name =='new york city' or city_name =='washington':
            city = city_name
            break
        else:
            print("wrong input choose one city from chicago, new york city, washington") 
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Input a month name: ").lower()
        if month == 'january' or month =='feburary' or month =='march' or month =='april' or month =='may' or month == 'june':
            month = month
            break
        elif month == 'all':
            break
       
        else:
           print(" Wrong input, Input month must be before june or 'all' in lower case")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
  
    while True:
        day = input("Input a weekday name: ").title()
        if day == "All":
            break
        elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            day = day
            break
        else:
            print("Wrong input, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ") 
          
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
    #load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the start time colum to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from strat time to create new colums
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
        # filter by month to create the new dataframe
    
    if month == 'all':
        # use all months by list 1:7 
        
        # creare new dataframe using all months
        df = df[df['month'] > 0] 
    elif month != 'all':
        #use index of months list to get corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # create the new dataframe using filter by month
        df = df[df['month'] == month]
    
    # filter by day of week 
    if day != 'All':
        # create new dataframe by using filter by days
        df = df[df['day_of_week'] == day]
    elif day == 'All':
       
        df= df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month    
    most_common_month = pd.to_datetime(df['Start Time']).dt.month.mode()[0]
    print('The most common month is {}.'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day_of_week = pd.to_datetime(df['Start Time']).dt.weekday_name.mode()[0]
    print('The most common day of week is {}.'.format(most_common_day_of_week))
    # TO DO: display the most common start hour
    most_common_hour = pd.to_datetime(df['Start Time']).dt.hour.mode()[0]
    print('The most common start hour is{}.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].value_counts()[0]
    print('Most common start station is {}'.format(most_common_start))

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].value_counts()[0]
    print('Most common end station is {}'.format(most_common_end))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most common combination of start station and end station trip is {}'.format(most_common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_duration = sum(df['Trip Duration'])
    print('Total travel time is {}'.format(sum_duration))

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Mean travel time is {}'.format(mean_duration))
    print("\nThis computation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types count: {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('Gender count: {}'.format(gender_counts))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = min(df['Birth Year'])
        most_recent_birth = max(df['Birth Year'])
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth year is {} \n Most recent birth year and most common birth yearis {} and {}'.format(earliest_birth, most_recent_birth, most_common_birth))
    else:
        print(' Birth year stats cannot be calculated because Gender does not appear in the dataframe')
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input("Would you like to view 5 rows of the data? Enter yes or no?")
        start_loc = 0
        while (view_data == 'yes'):
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display != 'yes':
                break
        if view_data != 'yes':
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

      
if __name__ == "__main__":
	main()

