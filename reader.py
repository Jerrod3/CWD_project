import numpy as np
from statistics import mean

# for each rank file, 8 arrays
# for each array, there are 60 instances
# use an F-string and a loop to upload all files
# Average of values per day over each rep per param.
count = 0
repetitions = []
# Set count to 0, while loop to whatever amount of files to iterate through. Store all arrays from file in
# repetition list.
while count <= 10:
    rank = np.load(f"rank_{count}_T_total_deer.npy")
    count = count + 1
    repetitions.append(rank)
# the while loop uses an f string, which allows the user to replace whatever is in {} with a variable (count in
# this example)

# Create a list of averages per day across files. The while loop progresses each day using the count
# variable
count = 0
final_product = []
devs = []
while count <= 59:
    # create a list for each parameter per day
    param_1 = []
    param_2 = []
    param_3 = []
    param_4 = []
    param_5 = []
    param_6 = []
    param_7 = []
    param_8 = []
    for instance in repetitions:
        # loop through each file
        array = instance[0]
        # Grab the array part of the tupple
        ticks = 0
        # incorporate another count variable (ticks) to track which parameter is being looped through in the array
        for lst in array:
            param = lst[count]
            back = param.tolist()
            # convert numpy object to float, then append the parameter to the correct list
            if ticks == 0:
                param_1.append(back)
            elif ticks == 1:
                param_2.append(back)
            elif ticks == 2:
                param_3.append(back)
            elif ticks == 3:
                param_4.append(back)
            elif ticks == 4:
                param_5.append(back)
            elif ticks == 5:
                param_6.append(back)
            elif ticks == 6:
                param_7.append(back)
            else:
                param_8.append(back)
            ticks = ticks + 1
    transform = [param_4]
    # create a list that contains each parameter list to be averaged
    averages = []
    deviations = []
    # create a list of actual averages
    for param in transform:
        no_zeros = []
        for val in param:
            if val < .0000001:
                continue
            else:
                no_zeros.append(val)
        avg_no_zeros = mean(no_zeros)
        averages.append(avg_no_zeros)
        sum_squares = sum([((val - avg_no_zeros) * (val - avg_no_zeros)) for val in no_zeros])
        deviation = (sum_squares/ len(no_zeros)) ** .5
        deviations.append(deviation)

    # append the day's averages for each parameter into an overarching list
    final_product.append(averages)
    devs.append(deviations)

    # increment the day, wash rinse and repeat
    count =  count + 1

print(final_product)
print(devs)

