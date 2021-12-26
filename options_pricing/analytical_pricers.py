import logging
import numpy as np
from scipy.stats import norm

EPSILON = 10e-10 # used to avoid division by 0

def compute_discount_factor(interest_rate,time_horizon):
   '''
   Compute discount factor
   Inputs:
   interest_rate: interest rate
   time_horizon: time horizon
   Outputs:
   d: discount factor
   '''
   d = np.exp(-interest_rate*time_horizon)
   return d
   
def compute_vanilla_option_price(r,sigma,initial_state,T,K,option_type):
   '''
   Compute Black-Scholes based analytical vanila European option price
   Inputs:
   r: interest rate
   sigma: volatility
   initial_state: initial underlying price
   T: time to expiry (maturity) in years
   K: option strike price
   option_type: option type, either "call" or "put"
   Outputs:
   price: option price given inputs parameters
   '''
   if option_type in ["call","put"]:
      F=initial_state*np.exp(r*T)
      d1=(np.log(F/K)+(sigma*sigma/2.0)*T)/(sigma*np.sqrt(T+EPSILON))
      d2=d1-sigma*np.sqrt(T)
      discount_factor=compute_discount_factor(interest_rate=r,time_horizon=T)
      if option_type=="call":
         price = discount_factor*(F*norm.cdf(d1)-K*norm.cdf(d2))
      else:
         price = discount_factor*(K*norm.cdf(-d2)-F*norm.cdf(-d1))
   else:
   EP
      logging.debug(f"Undefined vanilla option type {option_type}")
      price = np.nan
   return price

