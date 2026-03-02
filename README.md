# BLACK SCHOLES PROJECT


## Description:
In this project I implementated the black scholes formula in python, along with the following greeks: delta, gamma, vega, theta and rho.
I also Implemented the iterative method of finding the implied volatility of the option using the Newton Raphson method.
This is my first project exploring quantitative finance so my motivation for this project was to learn more about the Black Scholes model while also developing my skills with object oriented programming in python.


## Features:
    - Black-Scholes pricing for calls & puts
    - Greeks calculations
    - Newton–Raphson implied volatility solver
    - Object-oriented architecture


## File/folder structure of the project:
    Black-Scholes-Project/
    │── src/
    │   └── bs_toolkit/
    │       │── __init__.py
    │       │── black_scholes.py
    │       │── greeks.py
    │       │── implied_vol.py
    │
    │── README.md

## Installation & Requirements:
This project requires the Scipy library, as well as the built-in Math library
This project requires Python 3.11+ 

To install the project use the following bash commands:

    git clone https://github.com/georgeponto/Black-Scholes-Project.git
    cd Black-Scholes-Project


To run the each file without any errors use the follwing bash commands:

    for Mac OS - "python3 -m src.bs_toolkit.black_scholes"
    for Mac OS - "python3 -m src.bs_toolkit.greeks"
    for Mac OS - "python3 -m src.bs_toolkit.implied_vol"

    for Windows OS - "python -m src.bs_toolkit.black_scholes"
    for Windows OS - "python -m src.bs_toolkit.greeks"
    for Windows OS - "python -m src.bs_toolkit.implied_vol"


To install the scipy library use the following bash commands:

    for Mac OS - "pip3 install scipy"

    for Windows OS - "pip install scipy"

