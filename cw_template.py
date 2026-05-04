"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID:  
 4. Date: 
****************************************************************************

"""

from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)


#**********************************************************************************************************************************************************************

"""
# Task A : Input validation for airport code and year.

This task A allows the user to:
    -Enter a three-letter departure airport code(validated)
    -Enter a four-digit year (validated)
    -Automatically build the correct CSV file name
    -Display the selected airports's full name and the chosen year
    
    All inputs are case-insensitive and include proper error messages.
"""

#Valid airport codes and their full names
valid_airports = {
    "LHR" : "London Heathrow",
    "MAD" : "Madrid Adolfo Suárez-Barajas",
    "CDG" : "Charles De Gaulle International",
    "IST" : "Istanbul Airport International",
    "AMS" : "Amsterdam Schiphol",
    "LIS" : "Lisbon Portela",
    "FRA" : "Frankfurt Main",
    "FCO" : "Rome Fiumicino",
    "MUC" : "Munich International",
    "BCN" : "Barcelona International",
}


#Valid aipline codes and their full names
valid_airlines = {
    "BA" : "British Airways",
    "AF" : "Air France",
    "AY" : "Finnair",
    "KL" : "KLM",
    "SK" : "Scandinavian Airlines",
    "TP" : "TAP Air Portugal",
    "TK" : "Turkish Airlines",
    "W6" : "Wizz Air",
    "U2" : "easyJet",
    "FR" : "Ryanair",
    "A3" : "Aegean Airlines",
    "SN" : "Brussels Airlines",
    "EK" : "Emirates",
    "QR" : "Qatar Airways",
    "IB" : "Iberia",
    "LH" : "Lufthansa",
}


def get_valid_airport_code():
    """
    This function asks the user to enter a three-letter airport code.
    It keeps reapiting the question until the user inputs a valid code.
    
    Returns:
    A valid airport code in upperscase (str)
    
"""
    
    #Use a variable to hold the prompt message,which changes on errors
    code_prompt1 = "Please enter a three-letter city code: "
    
    while True:
        #Get input,convert it to uppercase,and strip any accidental spaces
        code = input(code_prompt1).strip().upper()
        
        if len(code) != 3:
            #If length is wrong, display the prompt for the next attempt
            code_prompt1 = "Wrong code length - please enter a three-letter city code: "
            continue
        
        #Check if the code is in the list of valid airports
        elif code not in valid_airports:
            #If the code isn't recognised, display the prompt
            code_prompt1 = "Unavailable city code - please enter a valid city code: "
            continue
        else:
            return code      #If both checks pass,return the valid airport code
        
        
def get_valid_year():
    """
    This function asks the user to enter a year in YYYY format.
    It keeps repeating the question until the user inputs a valid year.
    
    Returns:
        A valid year as an integer (int)
    
"""
    
    #Use a variable to hold the prompt message, which changes on errors
    year_prompt1 = "Please enter the year required in the format YYYY: "
    
    while True:
        year_input = input(year_prompt1)     #Get the input as a string first
        
        try:
            year = int(year_input)          #Convert the string input to an integer (where errore happen)
            
        except ValueError:
            #If the input contained non-numeric characters,display the prompt
            year_prompt1 = "Wrong data type - please enetr a four-digit year value: "
            continue
        
        #Check if the year falls within the required range
        if 2000 <= year <= 2025:
            return year
        
        else:
            #If the year is out of bounds, display the prompt
            year_prompt1 = "Out of range - please enter a value from 2000 to 2025: "
            continue
        
        
def task_a_main():
    """
    This function gets the valid airport code and year from the user,then shows the matching CSV file.
    It validates both inputs,builds the CSV filename, and prints the details.
    
    Returns:
    tuple:(CSV filename, full airport name,year)
"""
    
    airport_code = get_valid_airport_code()
    print()
    year = get_valid_year()
    
    #Combine airport code and year to make the CSV file name
    selected_data_file = airport_code + str(year) + ".csv"
    
    #Display the output
    print("\n" + "*" * 85)
    print(f"File {selected_data_file} selected - Planes departing {valid_airports[airport_code]}{year}")
    print("*" * 85 + "\n")
    
    try:
        load_csv(selected_data_file)   #Calls the function "load_csv" sending the variable "selected_data_file" as a parameter
    except FileNotFoundError:
        print(f"File {selected_data_file} not found. check the file name and location.")

    return selected_data_file,valid_airports[airport_code],year
    
    
#**********************************************************************************************************************************************************************    

"""
#Task B: Flight data analysis

This function goes through all the flights in 'data_list' and counts different things about them.

  It calculates:
    -Total number of flights
    -Flights from terminal 2
    -Flights under 600 miles
    -Air france flights and average AF flights
    -British airway flights and average per hour
    -Flights below 15˚C
    -Hours when it rained
    -Least common destinations
    -Percentages for BA flights and delayed AF flights
    
"""

def task_b(data_list,airport_code,airport_full_name,year):
    
    #1. Total number of flights in the file
    total_flight_count = len(data_list)    #Count all rows in the CSV
    
    #2. Count how many flights left from terminal 2
    flights_terminal_2 = 0
    for flight in data_list:
        if flight[8] == "2":
            flights_terminal_2 += 1
            
            
    #3. Count flights that travelled less than 600 miles
    flights_under_600 = 0
    for flight in data_list:
        try:
            miles = int(flight[5])     #Convert the distance string into an integer for the comparison
            if miles < 600:
                flights_under_600 += 1
        except ValueError:
            #Skip this flight if the distance cannot be converted to a number
            continue
        
        
    #4. Count how many flights were operated by Air France (AF)
    af_flights_count = 0
    for flight in data_list:
        airline = flight[1]
        if airline.startswith("AF"):
             af_flights_count += 1


    #5. Count flights departing in temperatures below 15˚C
    flights_below_15 = 0
    for flight in data_list:
        temp_text = flight[10]

        try:
            temp = int(temp_text.split("˚")[0])
            if temp < 15:
                flights_below_15  += 1
        except (ValueError,IndexError):
            #If the temperature looks strange, skip this row
            continue


    #6. Count British Airways flights and work out their average per hour
    ba_total = 0
    for flight in data_list:
        flight_num = flight[1]
        if flight_num.startswith("BA"):
            ba_total += 1

    #Calculate the average over the 12- hour observation period and round to 2 decimal places
    ba_avg_hour = round(ba_total/12,2)

    #7. Count BA flights as a percentage of the total flights
    ba_pct = round((ba_total/total_flight_count) *100,2)

    #8. Count the percentage of delayed Air France flights
    af_flights_delayed = 0
    for flight in data_list:
        airline = flight[1]
        scheduled = flight[2]   #scheduled departure time
        actual = flight[3]      #actual departure time

        #If the times do not match, the flight was delayed
        if airline.startswith("AF") and scheduled != actual:
            af_flights_delayed += 1

        #Calculate the percentage, and check if af_flights_count is zero to prevent DivisionByZeroError
        if af_flights_count > 0:
            pct_af_flights_delayed = round((af_flights_delayed/af_flights_count)* 100,2)
        else:
            pct_af_flights_delayed = 0


    #9. Count how many different hours had rain
    #Using a set so the same hour is only counted once 
    rain_hours = set()
    for flight in data_list:
        weather = flight[10].lower() 

        if "rain" in weather:
            #Extract the hour number from the scheduled departure time (e.g "10:30" -> 10)
            hour_only = int(flight[2].split(":")[0]) #Convert the hour string to integer 
            rain_hours.add(hour_only)   #Add the hour to the set of rainy hours (no duplicates allowed)

        total_rain_hours = len(rain_hours)


    #10. Find the least common destinations 
    dest_counts = {}       #Initialize an empty dictionary to store{'Dest_Code': Count}

    #Go through each flight and count destinations
    for flight in data_list:
        dest = flight[4]
        if dest in dest_counts:
            #Already saw this destination? just add 1 to the count 
            dest_counts[dest] += 1
        else:
            #First time seeing this destination? start count at 1
            dest_counts[dest] = 1

    #find the lowest number of flights to any destination
    min_count = min(dest_counts.values())
    least_common_full = []

    #Collect all destinations that have this lowest count
    for code,count in dest_counts.items():
        if count == min_count:
            #Get full airport name if know it, otherwise just use the code
            if code in valid_airports:
                least_common_full.append(valid_airports[code])
            else:
                least_common_full.append(code)


    #Print results(Task B output)

    print(f"\nThe total number of flights from this airport was {total_flight_count}")
    print(f"The total number of flights departing Terminal Two was {flights_terminal_2}")
    print(F"The total number of departures on flights under 600 miles was {flights_under_600} ")
    print(F"There were {af_flights_count} Air France flights from this airport")
    print(F"There were {flights_below_15} flights departing in temperatures below 15 degrees")
    print(F"There was an average of {ba_avg_hour} British Airways flights per hour from this airport")
    print(F"British Airways planes made up {ba_pct}% of all departures")
    print(F"{pct_af_flights_delayed}% of Air France departures were delayed")
    print(F"There were {total_rain_hours} hours in which rain fell")
    print(F"The least common destinations is {least_common_full} \n")

    #Return everything to task C can save it to the text file
    return(
        total_flight_count,flights_terminal_2,flights_under_600,af_flights_count,
        flights_below_15,ba_avg_hour,ba_pct,pct_af_flights_delayed,total_rain_hours,least_common_full
    )


#**********************************************************************************************************************************************************************

"""
#Task C : Save task B results to a text file.

This function takes all the calculated results from task B
and writes them into a file called 'results.txt'. It includes 
the selected file name, aiport,year,and every statistic calculated in task B

"""

def task_c_save(filename,airport_full_name,year,results):
    (total_flight_count,flights_terminal_2,flights_under_600,af_flights_count,
        flights_below_15,ba_avg_hour,ba_pct,pct_af_flights_delayed,total_rain_hours,least_common_full) = results
    

    try:
        with open("results.txt", "a") as f:
            f.write("*"* 90 +"\n")
            f.write(F"File {filename} selected - Planes departing {airport_full_name}{year}\n")
            f.write("*"* 90 +"\n")
            f.write(f"The total number of flights from this airport was {total_flight_count}\n")
            f.write(f"The total number of flights departing Terminal Two was {flights_terminal_2}\n")
            f.write(F"The total number of departures on flights under 600 miles was {flights_under_600}\n ")
            f.write(F"There were {af_flights_count} Air France flights from this airport\n")
            f.write(F"There were {flights_below_15} flights departing in temperatures below 15 degrees\n")
            f.write(F"There was an average of {ba_avg_hour} British Airways flights per hour from this airport\n")
            f.write(F"British Airways planes made up {ba_pct}% of all departures\n")
            f.write(F"{pct_af_flights_delayed}% of Air France departures were delayed\n")
            f.write(F"There were {total_rain_hours} hours in which rain fell\n")
            f.write(F"The least common destinations is {least_common_full} \n\n\n")
    except Exception as e:
        print("Could not write to results.txt", e)  



#**********************************************************************************************************************************************************************          

"""
#Task D: Draw a histogram for a selected airline

This function:
    -asks the user for a valid two-letter airline code (accept lower/upper case)
    -count how many flights that airline had in each hour(00 -11)
    -draws a horizontal histogram  using graphics.py
    -shows a clear title, hour labels,numeric counts , and simple sytle
"""

def task_d_histogram(data_list,airport_name,valid_airlines,year):
    #Ask the user for an airline code and keep asking until it is valid
    code_prompt2 = "Enter a two-character Airline code to plot a histogram: "
    code = input(code_prompt2).strip().upper()

    #keep asking if the code is not in the airline list
    while code not in valid_airlines:
        code = input("Unavailable Airline code please try again.").strip().upper()

    airline_full_name = valid_airlines[code]     #Get full airline name for the title

#Set up hours 00–11 with zero counts so the chart always shows all hours
    hourly_counts = {f"{i:02d}": 0 for i in range(12)} 
    
    FLIGHT_NUM_INDEX = 1
    ACTUAL_DEPARTURE_INDEX = 3

    for f in data_list:
        try:
            airline_field = f[FLIGHT_NUM_INDEX]
            # Extract the actual departure hour (e.g., "06" from "06:05")
            actual_hour = f[ACTUAL_DEPARTURE_INDEX][:2] 
            
            # Check 1: Does the flight number start with the selected airline code?
            if airline_field.startswith(code): 
                # Check 2: Is the hour within our 12-hour window?
                if actual_hour in hourly_counts:
                    hourly_counts[actual_hour] += 1
        except IndexError:
            # Skip rows with missing data fields
            continue
            
    # Convert dictionary to a sorted list of counts for easier plotting
    hours_to_plot = sorted(hourly_counts.keys())
    counts = [hourly_counts[h] for h in hours_to_plot]
    
    
    
    #Create the graphics window and set up the layout for the bars
    margin_left = 160
    margin_right = 80
    bar_height = 28
    gap = 10
    rows = len(hours_to_plot)
    win_width = 900
    # Set height dynamically based on the number of bars to ensure clear content
    win_height = max(300, 120 + rows * (bar_height + gap)) 

    # Creating the window using graphics.py
    win = GraphWin(f"Flight Histogram:{code} ", win_width, win_height)
    win.setBackground("lightgrey")

    # Draw Title 
    title_text = f"Departures by hour for {airline_full_name} from {airport_name} {year}"
    title = Text(Point(win_width//2, 25), title_text)
    title.setSize(14)
    title.setStyle("bold")
    title.draw(win)

    # Scaling Logic(Figure out how wide the bars should be so they fit nicely in the window)
    max_count = max(counts) if counts else 1
    if max_count == 0:
        max_count = 1  # Avoid division by zero
        
    max_bar_width = win_width - (margin_left + margin_right)
    # The scale factor ensures the longest bar will reach the maximum allowed width
    scale = max_bar_width / max_count 

    # Draw Y-axis Label
    y_label_text = "Hours\n\n00:00\nto\n12:00"
    y_label = Text(Point(40, win_height//2), y_label_text )
    y_label.setSize(12)
    y_label.draw(win)

    # Draw Horizontal Bars 
    top_y = 60
    # Iterate through the sorted hours (00 to 11) and their counts
    for i, h in enumerate(hours_to_plot):
        y0 = top_y + i * (bar_height + gap)
        y1 = y0 + bar_height
   
            # Draw hour label (left/Y-axis value)
        hour_label = Text(Point(margin_left - 70, (y0 + y1)//2), h)
        hour_label.setSize(10)
        hour_label.draw(win)

        # Draw the bar rectangle
        bar_len = counts[i] * scale
        rect = Rectangle(Point(margin_left, y0), Point(margin_left + bar_len, y1))
        rect.setFill("maroon")
        rect.setOutline("black")
        rect.draw(win)

        # Draw numerical count value
        count = counts[i]
        count_label_pos = Point(margin_left + bar_len + 20, (y0 + y1)//2)
        count_label = Text(count_label_pos, str(count))
        count_label.setSize(10)
        count_label.draw(win)

    # Wait for the user to click before closing the window
    help_text = Text(Point(win_width//2, win_height - 20), "Click anywhere to close the histogram window.")
    help_text.setSize(10)
    help_text.draw(win)
    
    # Wait for the user to click and handle potential errors during closing
    try:
        win.getMouse()
    except:
        pass
    finally:
        win.close()
    






#**********************************************************************************************************************************************************************

"""
Task E : Allow the user to run the program again.

This function:
    -asks the user if they want to select a new data file and repeat the whole process (Task A and D)
    -keeps asking until the user enetrs Y or N(accept lower/upper case)
    -returns True if the user wants to pick a new  CSV file
    -returns False if the user wants to stop the program 

It basically lets the user run everything again without restarting the program manually.  
"""

def ask_run_again():
    while True:
        choice = input("Do you want to select a new data file? Y/N: ")
        if choice == "Y":
            return True
        if choice == "N":
            return False
        print("Please enter Y or N ")


#Main program loop(Task A - E)
if __name__ == "__main__":
    while True:
        #Clear the old data list so every run starts fresh
        data_list = []

        #Task A (select & load)
        selected_file,airport_name,year = task_a_main()

        #Task B (analysis)
        results = task_b(data_list,airport_name,valid_airlines,year)

        #Task C (save)
        task_c_save(selected_file,airport_name,year,results)

        #Task D (histogram)
        task_d_histogram(data_list,airport_name,valid_airlines,year)

        #Task E (ask whether to run again)
        if ask_run_again():
            #loop again:clears data_list at top of loop
            continue
        else:
            print("\nThank you.End of run.")
            break



            
            
            
            
        

