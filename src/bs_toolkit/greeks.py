# this file contains the code for the option greeks

# importing python libraries and other files
from .black_scholes import BlackScholes
from . import black_scholes
import math
from scipy import stats

# greeks class for calculating the greeks
class Greeks:
    def __init__(self, bs: BlackScholes):
        self.bs = bs


    # method that calculates delta 
    def delta(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        # calculating delta for calls and puts
        delta_call = math.exp(-self.bs.q * self.bs.T) * stats.norm.cdf(d1)
        delta_put = math.exp(-self.bs.q * self.bs.T) * (stats.norm.cdf(d1)-1)
        
        # returning specific delta value depending on user input value
        if self.bs.option_type == "call":
            return delta_call
        elif self.bs.option_type == "put":
            return delta_put
    
    
    # method that calculates gamma 
    def gamma(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        #calculating gamma
        gamma = (math.exp(-self.bs.q * self.bs.T) * stats.norm.pdf(d1)) / (self.bs.S * self.bs.sigma * math.sqrt(self.bs.T))
        # returning gamma
        return gamma


    # method that calculates vega 
    def vega(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        #calculating vega
        vega = self.bs.S * math.exp(-self.bs.q * self.bs.T) * math.sqrt(self.bs.T) * stats.norm.pdf(d1)
        # returning vega
        return vega
    
    
    # method that calculates theta
    def theta(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        #calculating theta for calls and puts
        theta_fraction = (-self.bs.S * math.exp(-self.bs.q * self.bs.T) * stats.norm.pdf(d1) * self.bs.sigma) / 2 * math.sqrt(self.bs.T)
        theta_call = theta_fraction + self.bs.q * self.bs.S * math.exp(-self.bs.q * self.bs.T) * stats.norm.cdf(d1) - self.bs.r * self.bs.K * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(d2)
        theta_put = theta_fraction - self.bs.q * self.bs.S * math.exp(-self.bs.q * self.bs.T) * stats.norm.cdf(-d1) + self.bs.r * self.bs.K * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(-d2)
        
        # returning specific theta value depending on user input value
        if self.bs.option_type == "call":
            return theta_call
        elif self.bs.option_type == "put":
            return theta_put
    
    
    # method that calculates rho 
    def rho(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()

        # calculating rho for calls and puts
        rho_call = self.bs.K * self.bs.T * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(d2)
        rho_put = -self.bs.K * self.bs.T * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(-d2)

        # returning specific rho value depending on user input value
        if self.bs.option_type == "call":
            return rho_call
        elif self.bs.option_type == "put":
            return rho_put