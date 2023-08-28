import math
import matplotlib.pyplot as plt
from flask import Flask
from flask import request, jsonify
import csv
app = Flask(__name__)
app.config["DEBUG"] = True

def calculate_sum_count():
    with open('concentration.timeseries.csv', 'r') as file:
        total_concentration = 0
        total_count = 0
        csvreader = csv.reader(file)
        # grab the headers of each row to determine which row the concentration is in
        headers = next(csvreader)
        index = 0
        for i in range(len(headers)):
            if headers[i] == 'concentration':
                index = i
                break
        for row in csvreader:
            total_concentration += float(row[index])
            total_count += 1
    return total_concentration, total_count

# Endpoint that returns mean of the concentration
@app.route('/get-mean', methods = ['GET'])
def api_mean():
    return 'The mean of the concentration is ' + str(calculate_sum_count()[0]/calculate_sum_count()[1]) + '.'

# Endpoint that returns the standard deviation of the concentration
@app.route('/get-std-deviation', methods = ['GET'])
def api_std_deviation():
    mean = calculate_sum_count()[0]/calculate_sum_count()[1]
    distance_from_mean_sum = 0
    with open('concentration.timeseries.csv', 'r') as file:
        csvreader = csv.reader(file)
        # grab the headers of each row to determine which row the concentration is in
        headers = next(csvreader)
        index = 0
        for i in range(len(headers)):
            if headers[i] == 'concentration':
                index = i
                break
        for row in csvreader:
            distance_from_mean_sum += (float(row[index]) - mean) ** 2
        standard_deviation = math.sqrt(distance_from_mean_sum/calculate_sum_count()[1])
    return 'The standard deviation of the concentration is ' + str(standard_deviation) + '.'

# Endpoint that returns the sum of the concentration
@app.route('/get-sum', methods = ['GET'])
def api_sum():
    return 'The total sum of the concentration is ' + str(calculate_sum_count()[0]) + '.'

# Endpoint that returns the png visualization of the concentration
@app.route("/get-image",  methods = ['GET'])
def api_image():
    with open('concentration.timeseries.csv', 'r') as file:
        x_values, y_values = [], []
        csvreader = csv.reader(file)
        # grab the headers of each row to determine which row the x and y values are in
        headers = next(csvreader)
        x_index = 0
        y_index = 0
        for i in range(len(headers)):
            if headers[i] == 'x':
                x_index = i
                continue
            if headers[i] == 'y':
                y_index = i
                continue
        for row in csvreader:
            x_values.append(float(row[x_index]))
            y_values.append(float(row[y_index]))
        plt.plot(x_values, y_values)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Visualization of the concentration')
        plt.show()
    return 'this is the png visualization'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)