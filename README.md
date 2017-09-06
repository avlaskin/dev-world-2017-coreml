These are support links for the talk:

- Wiki on Accelerating change: https://en.wikipedia.org/wiki/Accelerating_change
- CNN comparison in terms of operations: https://culurciello.github.io/tech/2016/06/20/training-enet.html
- Reference PDF - comparison DNNs and operations/power/memory : https://arxiv.org/abs/1605.07678
- Neurons rewiring experiment - original paper https://www.ncbi.nlm.nih.gov/pubmed/1527604
- Machine for deep learning : https://www.oreilly.com/learning/build-a-super-fast-deep-learning-machine-for-under-1000
- EGPU with 1080Ti: https://9to5mac.com/2017/04/19/akitio-node-gtx-1080-ti-gpu-macbook-pro-gaming-egpu/
- Coriander - CUDA compiled for OpenCL 1.2 - https://github.com/hughperkins/Coriander
- Quantum Computing in NSW: https://www.youtube.com/user/UNSW

Follow Andrew Ng on YouTube:
- https://www.youtube.com/watch?v=F1ka6a13S9I
- https://www.youtube.com/watch?v=pfFyZY1RPZU


Good learning resources for Machine Learning and Deep Learning:
- Great staring point for you ML education. By Andrew Ng: https://www.coursera.org/learn/machine-learning -
- NEW!!! Deep Learning course by Andrew Ng: https://www.coursera.org/specializations/deep-learning
- Blog by Andrej Karpthy about Deep Learning: http://karpathy.github.io
- MIT Online book: http://www.deeplearningbook.org
- Keras tutorials: https://elitedatascience.com/keras-tutorial-deep-learning-in-python
- CNN course: http://cs231n.github.io/convolutional-networks/


How to set up Keras on Mac (assuming that you have Python installed):
```
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py
sudo pip install tensorflow# for tensorflow-gpu see below
sudo pip install keras# coremltools now supports keras 2.x
sudo pip install coremltools
cd ~/.keras# Here we need to check if keras backend is tensorflow
cat keras.json
```

And your ~/.keras/keras.json should look something like this:
```
{
    "image_dim_ordering": "tf",
    "epsilon": 1e-07,
    "floatx": "float32",
    "backend": "tensorflow"
}
```

To use (external or internal for old Macs) Nvidia GPU we need to install following:
1. The NVIDIA drivers associated with CUDA.
2. CUDA Toolkit 8.0 [v8.0.61]
3. cuDNN v5.1 for CUDA 8.0.[v5.1] (this needs Nvidia developer account) - (Should be installed with DYLD_LIBRARY_PATH set)
4. GPU card with CUDA compute capability 3.0 or higher.
5. Set up DYLD_LIBRARY_PATH to be exported with cuda/lib and cuDNN/lib paths included.
6. After that we can install tensorflow-gpu

```sudo pip install tensorflow-gpu```

Enjoy!


This repo has an example of Keras Neural network that does learn XOR function. Although training set is excessive (takes all possible cases) - it is a good starting point for understanding on how you can do Keras model for iOS.


Contacts:
- Twitter: @avlaskin
- Email: alex@avlaskin.com
