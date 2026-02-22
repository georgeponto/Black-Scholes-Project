from . import black_scholes
from .black_scholes import BlackScholes
from .greeks import Greeks
import math
from scipy import stats

class ImpliedVolatility:
    def __init__(self, bs: BlackScholes, g: Greeks):
        self.bs = bs
        self.g = g
        
    def newton_raphson(self) -> float:
        tol = 0.0001
        dif = self.bs.price() - self.bs.market_price
        v = self.g.vega()
        
        for i in range(100):
            # calculating new implied volatility per iteration
            i_vol = self.bs.sigma - ((self.bs.price() - self.bs.market_price) / v)
            
            # redefining variables with new implied volatility
            self.bs.sigma = i_vol
            v = self.g.vega()
            
            # raising an error if vega tends too close to 0
            if v < tol:
                raise ValueError(f"Vega is too small at {v}; Newton-Raphson not reliable")
            
        return(self.bs.sigma)

        

greeks = Greeks(black_scholes.option)
iv = ImpliedVolatility(black_scholes.option, greeks)
    
print(iv.newton_raphson())
print(black_scholes.option.price())
# python3 -m src.bs_toolkit.implied_vol