from datetime import date
import random

date_now = date.today()

def input_data(date_now):
    while True:
        input_name = raw_input("Enter your name: ")
        if input_name:
            break
    while True:
        input_year = raw_input("Enter your birth year: ")
        if input_year.isdigit() and len(input_year) < 5:
            if int(input_year) < date_now.year and int(input_year) > 1900:
                break
            else:
                print ("wrong year, please enter again")
    age_now = date_now.year - int(input_year)
    print "{0}, your age is {1}".format(input_name, age_now)
    result(input_name, age_now)

def result(input_name, age_now):
    print
    if age_now < 18:
        print "Ubderage, your age less then 18"
    else:
        print "Adult"

input_data(date_now)

# nubers generator
numb_range = []
for x in range(10):
   numb_range.append(random.randint(1, 10))
print "Random numbers = ", numb_range

# finding the sum of even numbers and odd numbers
add_list = 0
even_list = 0
for numb in numb_range:
 if numb % 2:
  add_list = add_list + numb
 else:
  even_list = even_list + numb
print "sum of odd numbers is: ", add_list
print "sum of even numbers is: ", even_list

# sorted numbers
numb_range.sort(reverse=False)
print "Sorted numbers = ", numb_range
numb_range.sort(reverse=True)
print "Reversed numbers = ", numb_range


# sum min and max numbers
sum_min_max = min(numb_range) + max(numb_range)
print "Sum min and max = ", sum_min_max

#test jkdfhgkjdhg

new = range(12)
for i in new:
    print i