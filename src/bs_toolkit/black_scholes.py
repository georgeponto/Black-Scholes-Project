# this file contains the code for the black scholes formula 
# this file also contains some of the code for the CLI 

# importing python libraries / modules
import math
from scipy import stats

# black scholes class for pricing options 
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
        
        # validating input variables to be within realistic bounds
        if self.S <= 0 or self.K <= 0 or self.sigma <= 0 or self.market_price <= 0:
            raise ValueError("Spot price, Strike price, Market price and Implied volatility must be positive.")
        elif self.T < 0 or self.q < 0:
            raise ValueError("Time to maturity and Dividend yield must not be negative.")
        elif self.option_type != "put" or self.option_type != "call":
            raise ValueError("Option type must either be a put or call.")

        
        
    # calculating d1 and d2 values and outputing them as a tuple of real numbers for easier future calculations
    def d1_d2(self) -> tuple[float ,float]:
        d1 = (math.log(self.S / self.K)  +  (self.r - self.q + 0.5 * self.sigma**2) * self.T)  /  (self.sigma * math.sqrt(self.T))
        d2 = d1 - self.sigma*(math.sqrt(self.T))

        return d1, d2


    # main implementation of black scholes formula for calls and puts
    def price(self) -> float:
        # asigning d1 & d2 values
        d1, d2 = self.d1_d2()

        # calculating both call and put prices
        Call = self.S * math.exp(-self.q*self.T) * stats.norm.cdf(d1)  -  self.K * math.exp(-self.r * self.T) * stats.norm.cdf(d2)
        Put = self.K * math.exp(-self.r * self.T) * stats.norm.cdf(-d2)  -  self.S * math.exp(-self.q * self.T) * stats.norm.cdf(-d1)
        
        # returning specific option price depending on user input value
        if self.option_type == "call":
            return Call
        elif self.option_type == "put":
            return Put
        

# welcome message to user running the programme 
print("\nWelcome to the Black Scholes Calculator...\n")

# inputing the parameters of the model
spot_price = float(input("Enter the Spot Price of the option: "))
strike_price = float(input("Enter the Strike Price of the option: "))
time_to_maturity = float(input("Enter the Time to Maturity of the option(in days): ")) /365 # TTM input in days and converted to years
risk_free_rate = float(input("Enter the Risk Free Rate of the option: "))
dividend_yield = float(input("Enter the Dividend Yield of the option: "))
option_type = input("Enter the Option Type (call/put): ")
market_price = float(input("Enter the Market Price of the option: "))

implied_volatility = 0.2 # implied volatility is initially a 20% estimation
 
# instance for variables to price option
option = BlackScholes(spot_price,
                      strike_price,
                      time_to_maturity,
                      risk_free_rate,
                      dividend_yield,
                      implied_volatility,
                      option_type,
                      market_price)