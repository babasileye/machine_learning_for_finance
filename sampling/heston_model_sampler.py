import numpy as np

def heston_model_sampler(init_states,init_vols,mu,kappa,theta,nu,T,M,N,min_square_vol):
   '''
   Heston model sampler with states and volatilities noises assumed uncorrelated
   Inputs:
   init_state: initial states
   init_vols: initial volatilities
   mu: states drift
   theta: volatility steady state value
   nu: volatilities volatility
   M: number of time steps
   T: time horizon
   N: number of trajectories
   min_square_vol: volatility minimum value
   Outputs:
   states: sampled stated trajectories
   squared_vols: sampled states squared volatilities
   '''
   dt = float(T)/M
   time_steps = [m*dt for m in range(M)]
   noise_s = np.random.normal(0,1,[N,M])
   noise_v = np.random.normal(0,1,[N,M])
   states = np.zeros((N,M), dtype=float)
   squared_vols = np.zeros((N,M), dtype=float)
   states[:,0] = init_states
   squared_vols[:,0] = init_vols*init_vols
   for m in range(1,M,1):
      squared_vols[:,m]=np.maximum(squared_vols[:,m-1] + kappa*(theta-squared_vols[:,m-1])*dt+nu*np.sqrt(dt*squared_vols[:,m-1])*noise_v[:,m],min_square_vol)
      states[:,m]=states[:,m-1]*(1+mu*dt+np.sqrt(dt*squared_vols[:,m-1])*noise_s[:,m])
   return states,squared_vols,time_steps
