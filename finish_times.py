# stored data
finish_times = []
#finish_times = {}
male_record_times = {
    9.58 : "World Record Time",
    9.86 : "European Record Time",
    9.87 : "British Record Time"
}
female_record_times = {
    10.49 : "World Record Time",
    10.73 : "European Record Time",
    10.99 : "British Record Time"
}
male_time = [9.87]
female_time = [10.99]
## nested
times_nested = {
    "male" : male_time,
    "female" : female_time
}
genders_nested = {
    "male" : male_record_times,
    "female" : female_record_times
}
record_achieved = {}
finish_times = {}
printed_key = []
gender = "none"
counter = 0
gender_input = str(input("what is the gender of the athletes in the race?: "))
if gender_input == "female" or gender_input == "male":
    gender = gender_input
    player_input = int(input("how many lanes? 4 or 8: "))
    if player_input == 4 or player_input == 8: 
        for i in range(0, player_input):
            i += 1
            finish = float(input(f"input a finish time for lane {i} (in seconds and miliseconds XX.XX or X.XX): "))
            finish_times[i] = finish 
        for key, value in finish_times.items():
            #if value in times_nested[gender]: 
                #print("----------------------------------------")
                #print("lane: ", key, ",",  "record time: ", f"{value:.2f}", ",",  "record achieved: ", #genders_nested[gender].get(value))
            #else:
                if not value in record_achieved:
                    for k in sorted(genders_nested[gender], key=lambda sort: genders_nested[gender][sort], reverse=True):
                        if value < k and value > 0 and value > 0.00:
                            if not key in printed_key:
                                print("----------------------------------------")
                                print("lane: ", key, ",", "new time: ", f"{value:.2f}", ",",  "record time: ", k, ",",  "record: ", genders_nested[gender].get(k))
                                printed_key.append(key)
                        elif value <= 0.00 and not key in printed_key:
                                print("----------------------------------------")
                                print("lane: ", key,  ",", "new time: ", f"{value:.2f}",  ",",)
                                print("record: No records broken!")
                                printed_key.append(key)
                        elif value >= times_nested[gender][-1] and not key in printed_key:
                                print("----------------------------------------")
                                print("lane: ", key,  ",", "new time: ", f"{value:.2f}",  ",", "record: No records broken!")
                                printed_key.append(key)
    else:
        print("Invalid input: can only be 4 or 8 lanes!")
else:
    print("Invalid Gender: female or male has to be input!")