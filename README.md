# BLACK SCHOLES PROJECT


## Description:
In this project I implemented the black scholes formula in python, along with the following greeks: delta, gamma, vega, theta and rho.
I also implemented an iterative method of finding the implied volatility of the option using the Newton Raphson method.
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
    │       ├── __init__.py
    │       ├── black_scholes.py
    │       ├── greeks.py
    │       └── implied_vol.py
    │
    └── README.md

## Usage:
bs variables are in the form of (spot_price, strike_price,
                                time_to_maturity, risk_free_rate,
                                dividend_yield, implied_volatility,
                                option_type, market_price)

    from bs_toolkit.black_scholes import BlackScholes
    from bs_toolkit.greeks import Greeks
    from bs_toolkit.implied_vol import ImpliedVolatility

    bs = BlackScholes(100, 105, 30, 0.05, 0.05, 0.2, "call", 2.0)
    g = Greeks(bs)
    iv = ImpliedVolatility(bs, g)
      
    print(bs.price())
    print(g.delta())
    print(iv.newton_raphson())

## Installation & Requirements:
This project requires the Scipy library, as well as the built-in math module
This project requires Python 3.11+ 

To install the project use the following bash commands:

    git clone https://github.com/georgeponto/Black-Scholes-Project.git
    cd Black-Scholes-Project


To run each file without any errors use the following bash commands:
for Mac OS:

    python3 -m src.bs_toolkit.black_scholes
    python3 -m src.bs_toolkit.greeks
    python3 -m src.bs_toolkit.implied_vol

for Windows OS:

    python -m src.bs_toolkit.black_scholes
    python -m src.bs_toolkit.greeks
    python -m src.bs_toolkit.implied_vol


To install the scipy library use the following bash commands:
for Mac OS:

    pip3 install scipy

for Windows OS:
    
    pip install scipy

## LICENSE
This project is licensed under the MIT License. See the LICENSE file for details.
