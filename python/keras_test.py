import keras
import keras.models
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np

# Import data

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Design the model
model = Sequential()
model.add(Dense(10, input_dim=2))
model.add(Activation('tanh')) 

model.add(Dense(1))
model.add(Activation('sigmoid'))

# Compute the model
sgd = SGD(lr=0.1)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])

#optional stuff to see cool graphs
# tbCallBack = keras.callbacks.TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)
# model.fit(X, y, nb_epoch=1000, batch_size=1,callbacks=[tbCallBack])

# Train the model
model.fit(X, y, nb_epoch=2000, batch_size=1)

# Let's see what is inside
#nX = np.array([[1,1]])
#nY = model.predict(nX)
#print("Prediction for 1 XOR 1 = ")
#print(nY[0])
#print(" ")

# Export the model
import coremltools
coreml_model = coremltools.converters.keras.convert(model)
coreml_model.save("keras_model.mlmodel")

#optional stuff to save and reuse the model within Keras
#model.save('keras_weights.h5') # hdf5 format
#model_json_string = model.to_json()
#fh = open('keras_model.json','w')
#fh.write(model_json_string)
#fh.close()
