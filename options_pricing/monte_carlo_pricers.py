import logging
import numpy as np
from options_pricing.analytical_pricers import compute_discount_factor

def compute_monte_carlo_option_prices(r,samples,time_steps,K,option_type):
   '''
   Compute option prices using sample underlying price history
   Inputs:
   r: interest rate
   samples: sampled price history
   time_steps: sampled prices time steps
   K: strike price 
   option_type: option type ("call" for european call, "put" for european put)
   Outputs:
   option_prices: option prices
   '''
   if option_type in ["call","put"]:
      M = samples.shape[1]
      if option_type == "call":
         option_prices = [compute_discount_factor(r,time_steps[m])*np.mean(np.maximum(samples[:,m]-K,0)) for m in range(1,M,1)]
      else:
         option_prices = [compute_discount_factor(r,time_steps[m])*np.mean(np.maximum(K-samples[:,m],0)) for m in range(1,M,1)]
      price_times = np.array(time_steps)[1:]
      return option_prices,price_times
   else:
      logging.debug(f"Undefined option type {option_type}")
