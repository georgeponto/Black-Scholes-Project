# this file contains the code for finding the implied volatility using the newton raphson method
# this file also contains some of the code for the CLI 

# importing python libraries and other files
from . import black_scholes
from .black_scholes import BlackScholes
from .greeks import Greeks

# implied volatility class for finding implied volatility
class ImpliedVolatility:
    def __init__(self, bs: BlackScholes, g: Greeks):
        self.bs = bs
        self.g = g
    
    # method for newton raphson method of finding volatility
    def newton_raphson(self) -> float:
        # asigning variables required 
        tolerance = 0.0001
        v = self.g.vega()
        iterations = 100 # how many times the loop will run in finding implied volatility 
        
        # loop iteratively finding implied volatility
        for i in range(iterations):
            # calculating new implied volatility per iteration
            i_vol = self.bs.sigma - ((self.bs.price() - self.bs.market_price) / v)
            
            # redefining variables with new implied volatility
            self.bs.sigma = i_vol
            v = self.g.vega()
            
            # raising an error if vega tends too close to 0
            if v < tolerance:
                raise ValueError(f"Vega is too small at {v}; Newton-Raphson not reliable")
        # returning final iteration of implied volatility 
        return(self.bs.sigma)

        
# asigning methods to variables to be outputted
greeks = Greeks(black_scholes.option)
iv = ImpliedVolatility(black_scholes.option, greeks)

# outputing the greeks, implied volatility and option price
print(f"The delta of the option is: {greeks.delta()}")
print(f"The gamma of the option is: {greeks.gamma()}")
print(f"The vega of the option is: {greeks.vega()}")
print(f"The theta of the option is: {greeks.theta()}")
print(f"The rho of the option is: {greeks.rho()}")
print(f"The implied volatility of the option is: {iv.newton_raphson()}")
print(f"The calculated price of the option is: {black_scholes.option.price()}")

# run the project with the following bash command...  python3 -m src.bs_toolkit.implied_vol