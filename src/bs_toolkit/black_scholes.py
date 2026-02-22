import math
from scipy import stats

implied_volatility = 0.2 # implied volatility is initially a 20% estimation

class BlackScholes:
    def __init__(self, spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float, dividend_yield: float, sigma: float, option_type: str, market_price: float):
        self.S = spot_price 
        self.K = strike_price
        self.T = time_to_maturity
        self.r = risk_free_rate
        self.q = dividend_yield
        self.option_type = option_type
        self.market_price = market_price
        self.sigma = sigma
        
        # validating variables
        if self.S <= 0 or self.K <= 0 or self.sigma <= 0:
            raise ValueError("Spot price, Strike price and Implied volatility must be positive.")
        elif self.T < 0 or self.q < 0:
            raise ValueError("Time to maturity and Dividend yield must not be negative.")
    
        
    # calculating d1 and d2 values and outputing them as a tuple of real numbers
    def d1_d2(self) -> tuple[float ,float]:
        d1 = (math.log(self.S / self.K)  +  (self.r - self.q + 0.5 * self.sigma**2) * self.T)  /  (self.sigma * math.sqrt(self.T))
        d2 = d1 - self.sigma*(math.sqrt(self.T))

        return d1, d2


    # implementing black scholes formula for calls and puts
    def price(self) -> float:
        # getting d1 & d2 values
        d1, d2 = self.d1_d2()

        # calculating both call and put prices
        Call = self.S * math.exp(-self.q*self.T) * stats.norm.cdf(d1)  -  self.K * math.exp(-self.r * self.T) * stats.norm.cdf(d2)
        Put = self.K * math.exp(-self.r * self.T) * stats.norm.cdf(-d2)  -  self.S * math.exp(-self.q * self.T) * stats.norm.cdf(-d1)
        
        # returning specific option price depending on option_type value
        if self.option_type == "call":
            return Call
        elif self.option_type == "put":
            return Put
        else:
            raise ValueError("Option type must either be a Put or a Call.")
        


    

spot_price = float(input("Enter the Spot Price of the option: "))
strike_price = float(input("Enter the Strike Price of the option: "))
time_to_maturity = float(input("Enter the Time to Maturity of the option: "))
risk_free_rate = float(input("Enter the Risk Free Rate of the option: "))
dividend_yield = float(input("Enter the Dividend Yield of the option: "))
option_type = input("Enter the Option Type (call/put): ")
market_price = float(input("Enter the Market Price of the option"))
 
        
option = BlackScholes(spot_price,
                      strike_price,
                      time_to_maturity,
                      risk_free_rate,
                      dividend_yield,
                      implied_volatility,
                      option_type,
                      market_price)


