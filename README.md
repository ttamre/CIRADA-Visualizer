<h1 align="center">CIRADA FIRST Data Visualizer</h1>

<div align="center" style="padding-bottom:20px">
    <img src="https://img.shields.io/badge/flask-2.0.2-blueviolet" />
    <img src="https://img.shields.io/badge/waitress-2.0.0-blue" />
    <img src="https://img.shields.io/badge/astropy-4.3.1-orange" />
    <img src="https://img.shields.io/badge/pillow-8.4.0-lightgrey" />
    <img src="https://img.shields.io/badge/markupsafe-2.0.1-red" />
    <img src="https://img.shields.io/badge/pytest-6.2.5-9cf" /> 
    <img src="https://img.shields.io/badge/license-GPL%20v3-green" />
</div>

<p align="center">
A website that processes and visualizes astronomical data based on provided FIRST data provided as FITS files.<br>This project was developed as an interview presentation for the CIRADA software developer competition.<br>This project was developed using python, flask, and astropy, with pytest and github actions for automated testing.
</p>

<div align="center">
    <img src="https://github.com/ttamre/CIRADA-Visualizer/blob/master/static/demo.gif?raw=true">
</div>

## Usage
This project requires [Python 3](https://www.python.org/downloads/)

### Clone and open the repository
```
git clone https://github.com/ttamre/CIRADA-Visualizer.git
cd CIRADA-Visualizer
```

### Open a virtual environment with Python 3
```
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies and run application
```
python -m pip install -r requirements.txt
python app.py
```
