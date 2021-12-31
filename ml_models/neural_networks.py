import tensorflow as tf

def create_feedworward_network_model(input_dim,hidden_layers_sizes,layers_activation,output_dim,output_activation):
   '''
   Create a simple feedforward neural network model using Tensorflow/Keras APIs taking a vector as input
   Inputs:
   input_dim: input dimention
   hidden_layers_sizes: list specifying layers sizes. Its length is the number of hidden layers
   layers_activation: hidden layers activation function ('relu','sigmoid','tanh',... )
   output_dim: output dimension
   output_activation: output activatiob function
   	'linear' for regression
   	'sigmoid' for binary classification
   	'softmax': for multi class classification
   Outputs:
   ffn_model: feedfoward network model
   '''
   nb_hidden_layers=len(hidden_layers_sizes)
   inputs = tf.keras.Input(shape=(input_dim,))
   for n in range(nb_hidden_layers):
      if n==0:  		
         layer_output=tf.keras.layers.Dense(hidden_layers_sizes[n],activation=layers_activation)(inputs)
      else:
         layer_output=tf.keras.layers.Dense(hidden_layers_sizes[n], activation=layers_activation)(layer_output)
   outputs=tf.keras.layers.Dense(output_dim,activation=output_activation)(layer_output)
   ffn_model = tf.keras.Model(inputs,outputs,name='feed_forward_network')
   return ffn_model
