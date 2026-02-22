from .black_scholes import BlackScholes
from . import black_scholes
import math
from scipy import stats


class Greeks:
    def __init__(self, bs: BlackScholes):
        self.bs = bs

    
    def delta(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        # calculating delta for calls and puts
        delta_call = math.exp(-self.bs.q * self.bs.T) * stats.norm.cdf(d1)
        delta_put = math.exp(-self.bs.q * self.bs.T) * (stats.norm.cdf(d1)-1)
        
        if self.bs.option_type == "call":
            return delta_call
        elif self.bs.option_type == "put":
            return delta_put
        
        
    def gamma(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        #calculating gamma
        gamma = (math.exp(-self.bs.q * self.bs.T) * stats.norm.pdf(d1)) / (self.bs.S * self.bs.sigma * math.sqrt(self.bs.T))
        
        return gamma
    
    
    def vega(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        #calculating vega
        vega = self.bs.S * math.exp(-self.bs.q * self.bs.T) * math.sqrt(self.bs.T) * stats.norm.pdf(d1)
        
        return vega
    
    
    def theta(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()
        
        #calculating theta for calls and puts
        theta_fraction = (-self.bs.S * math.exp(-self.bs.q * self.bs.T) * stats.norm.pdf(d1) * self.bs.sigma) / 2 * math.sqrt(self.bs.T)
        theta_call = theta_fraction + self.bs.q * self.bs.S * math.exp(-self.bs.q * self.bs.T) * stats.norm.cdf(d1) - self.bs.r * self.bs.K * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(d2)
        theta_put = theta_fraction - self.bs.q * self.bs.S * math.exp(-self.bs.q * self.bs.T) * stats.norm.cdf(-d1) + self.bs.r * self.bs.K * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(-d2)
        
        if self.bs.option_type == "call":
            return theta_call
        elif self.bs.option_type == "put":
            return theta_put
    
    
    def rho(self) -> float:
        # defining variable d1
        d1, d2 = self.bs.d1_d2()

        # calculating rho for calls and puts
        rho_call = self.bs.K * self.bs.T * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(d2)
        rho_put = -self.bs.K * self.bs.T * math.exp(-self.bs.r * self.bs.T) * stats.norm.cdf(-d2)

        if self.bs.option_type == "call":
            return rho_call
        elif self.bs.option_type == "put":
            return rho_put
        
g = Greeks(black_scholes.option)

print(g.vega())