
import math

# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

#getting the mean
# data = [20,69,56,90,40,99,86,100,70,69,80,65,57,82,90,70,79,39,90,80,86,53,97,95,88,47,100,56,97,100] #list of x or y
# data=[60,61,65,63,98,99,90,95,91,96]

# finding mean
def mean(data):
    # Step1 : To find total number to length in a list called data
    n= len(data)
    # n= len(data) -1
    # n= len(data[0]) - 1
    # n= len(data[0])
    total =0
    for x in data:
        total += int(x)

# Step2: Mean Formula
    # mean = total + n
    #mean = n / total
    mean = total / n
    # mean = total - n
    return mean



# squaring and getting the values
squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

#getting sum
sum =0
for i in squared_list:
    sum =sum + i

#dividing the sum by the total values
result = sum/ (len(data)-1)

# Step3: getting the deviation by taking square root of the result
# std_deviation = math.sqt(result)
# std_deviation = math.squareroot(result)
# std_deviation = MATH.sqrt(result)
std_deviation = math.sqrt(result)
print(std_deviation)
#print("derived using predefined function ",statistics.stdev(data))