import math
from matplotlib import cm
import matplotlib.pyplot as plt
from flask import Flask, render_template
import csv
from pylab import *
app = Flask(__name__)
app.config["DEBUG"] = True

# Helper function that calculates the sum of the concentration and the total count of entries. returns both in a tuple in form (sum, count)
def calculate_sum_count():
    with open('raw_data/concentration.timeseries.csv', 'r') as file:
        sum_concentration, total_count = 0, 0
        csvreader = csv.reader(file)
        # grab the headers of each column
        headers = next(csvreader)
        for row in csvreader:
            sum_concentration += float(row[headers.index('concentration')])
            total_count += 1
    return sum_concentration, total_count

# Endpoint that returns mean of the concentration
@app.route('/get-mean', methods = ['GET'])
def api_mean():
    return 'The mean of the concentration is ' + str(calculate_sum_count()[0]/calculate_sum_count()[1]) + '.'

# Endpoint that returns the standard deviation of the concentration
@app.route('/get-std-deviation', methods = ['GET'])
def api_std_deviation():
    mean = calculate_sum_count()[0]/calculate_sum_count()[1]
    distance_from_mean_sum = 0
    with open('raw_data/concentration.timeseries.csv', 'r') as file:
        csvreader = csv.reader(file)
        # grab the headers of each column
        headers = next(csvreader)
        for row in csvreader:
            distance_from_mean_sum += (float(row[headers.index('concentration')]) - mean) ** 2
        standard_deviation = math.sqrt(distance_from_mean_sum/calculate_sum_count()[1])
    return 'The standard deviation of the concentration is ' + str(standard_deviation) + '.'

# Endpoint that returns the sum of the concentration
@app.route('/get-sum', methods = ['GET'])
def api_sum():
    return 'The total sum of the concentration is ' + str(calculate_sum_count()[0]) + '.'

# Endpoint that returns the png visualization of the concentration
@app.route("/get-image",  methods = ['GET'])
def api_image():
    with open('raw_data/concentration.timeseries.csv', 'r') as file:
        x_values, y_values, z_values, concentration_values = [], [], [], []
        csvreader = csv.reader(file)
        # grab the headers of each column
        headers = next(csvreader)
        for row in csvreader:
            x_values.append(float(row[headers.index('x')]))
            y_values.append(float(row[headers.index('y')]))
            z_values.append(float(row[headers.index('z')]))
            concentration_values.append(float(row[headers.index('concentration')]))
        # plot the values and save as a png
        matplotlib.use('agg')
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, projection='3d')
        color_map = cm.ScalarMappable(cmap=cm.hsv)
        color_map.set_array(concentration_values)
        ax.scatter(x_values, y_values, z_values, marker='s', s=200, c=cm.hsv([i / max(concentration_values) for i in concentration_values]))
        plt.colorbar(color_map, None, plt.gca())
        ax.set_title("3D Heatmap of Concentration")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        filename = 'static/concentration_heat_map.png'
        plt.savefig(filename)
        return render_template("index.html", user_image=filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)