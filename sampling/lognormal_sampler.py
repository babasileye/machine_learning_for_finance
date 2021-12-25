import numpy as np

def lognormal_price_sampler(r,sigma,initial_state,T,M,N):
   '''
   Sample log normal price trajectories
   Inputs:
   r: interest rate
   sigma: volatility
   initial_state: stock inital price
   T: time horizon
   M: numbers of time steps
   N: number of trajectories
   Outputs:
   states: sampled trajectories
   time_steps: time steps
   ''' 
   dt = float(T)/float(M)
   time_steps = [m*dt for m in range(M)]
   states = np.zeros((N,M),dtype=float)
   states[:,0] = initial_state
   xsi = np.random.normal(0, 1, [N,M])
   for m in range(1,M,1):
      dW = np.sqrt(dt) * xsi[:,m]
      states[:,m] = states[:,m-1]*np.exp((r-sigma*sigma/2)*dt+sigma*dW)
   return states,time_steps
