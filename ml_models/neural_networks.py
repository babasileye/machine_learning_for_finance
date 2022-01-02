import tensorflow as tf

def create_feedworward_network_model(input_dim,hidden_layers_sizes,layers_activation,output_dim,output_activation):
   '''
   Create a simple feedforward neural network model using Tensorflow/Keras APIs taking a vector as input
   Inputs:
   input_dim: input dimention
   hidden_layers_sizes: list specifying layers sizes. Its length is the number of hidden layers
   layers_activation: hidden layers activation function ('relu','sigmoid','tanh',... )
   output_dim: output dimension
   output_activation: output activation function
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
   
def create_autoencoder(input_dim,encoding_layers_sizes,layers_activation,output_activation):
   '''
   An autoencoder is a neural network that replicates it self through a bottleneck layer
   The network is constituted by an encoder and a decoder. The encoder encodes the input
   into an embedding vector. The decoder decodes the embedding vector back into the output
   Inputs:
   input_dim: input dimention
   encoding_layers_sizes: list specifying encoding layers sizes.
   layers_activation: layers activation function ('relu','sigmoid','tanh',... )
   output_activation: output activation function ('linear','sigmoid','softmax')
   Outputs:
   encoder: encoding model
   autoencoder: full autoencoder (encoding-decoding) model
   '''
   inputs = tf.keras.Input(shape=(input_dim,))
   nb_encoding_layers=len(encoding_layers_sizes)
   for n in range(nb_encoding_layers):
      if n==0:  		
         encoded=tf.keras.layers.Dense(encoding_layers_sizes[n],activation=layers_activation)(inputs)
      else:
         encoded=tf.keras.layers.Dense(encoding_layers_sizes[n],activation=layers_activation)(encoded)
   decoding_layers_sizes=encoding_layers_sizes[::-1][1:]
   nb_decoding_layers=nb_encoding_layers-1
   for n in range(nb_decoding_layers):
      if n==0:
         decoded=tf.keras.layers.Dense(decoding_layers_sizes[n],activation=layers_activation)(encoded)
      else:
         decoded=tf.keras.layers.Dense(decoding_layers_sizes[n],activation=layers_activation)(decoded)
   decoded=tf.keras.layers.Dense(input_dim,activation=output_activation)(decoded)
   encoder=tf.keras.Model(inputs,encoded,name='encoder')
   autoencoder=tf.keras.Model(inputs,decoded,name='autoencoder')
   return encoder,autoencoder
      
      
      
      
