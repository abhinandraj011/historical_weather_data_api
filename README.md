# Weather Data Flask API

This Flask application provides an API for accessing weather data. It includes endpoints for retrieving weather data for specific stations, dates, years, and more.

## Description

The app uses Flask to create a web API that serves weather data stored in CSV files. It allows users to query weather data based on different parameters.

## Features

- Retrieves weather data for specific stations and dates.
- Supports querying weather data for specific years.
- Provides endpoints for accessing all available weather data.

## Installation

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Ensure that the necessary data files are located in the `data_small` directory.

## Usage

1. Run the Flask app with `python app.py`.
2. Access the API endpoints using HTTP requests.

### Endpoints

- `/`: Displays a homepage with weather station information.
- `/api/v1/<station>/<date>`: Retrieves weather data for a specific station and date.
- `/api/v1/<station>`: Retrieves all weather data for a specific station.
- `/api/v1/yearly/<station>/<year>`: Retrieves weather data for a specific station and year.

## Data Source

Weather data is sourced from CSV files located in the `data_small` directory. The files include information about weather stations and temperature readings.

## Technologies Used

- Flask: Web framework for creating the API.
- Pandas: Data manipulation library for handling CSV data.
- Requests: Library for making HTTP requests.

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/)
