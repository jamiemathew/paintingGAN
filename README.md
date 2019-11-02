# paintingGAN

## Overview
Generative Adversarial Networks can be used to generate new images, new paintings which can look like the painting of the known painter.  A project which consists of a  discriminator network and a generator network.
Goals
<li>Create a clean dataset of images of VanGogh if dimension 64 x 64 and rename the images from 0.jpg, 1.jpg, 2.jpg and so on.</li>
<li>Implement GAN on the dataset to Generate painting that looks like that of Van Gogh.</li>

<br><br>

## Usage:

### Step 1 - Gather training data
Made the GAN model on a dataset of paintings by Van Gogh found from kaggle  https://www.kaggle.com/gfolego/vangogh
<br>
I wrote the following code for downloading the images: 
https://github.com/jamiemathew/paintingGAN/blob/master/misc/downloadimages.py

<br><br>
### Step 2 - Prepare the training data
The following code contains information about the dataset.
https://github.com/jamiemathew/paintingGAN/blob/master/tflib/wikiartGenre.py
<br>
I following code resizes the images into 64 x 64 pixels dimensions.
https://github.com/jamiemathew/paintingGAN/blob/master/misc/resize.py

<br><br>
### Step 3 - Modify files
TRAINING THE MODEL
<br>
The generator initially takes in random rgb numbers and generates an image.This generated image is fed into the discriminator alongside a stream of images taken from the actual, ground-truth dataset.The discriminator takes in both real and fake images and returns probabilities, a number between 0 and 1, with 1 representing a prediction of authenticity and 0 representing fake. So you have a double feedback loop:The discriminator is in a feedback loop with the ground truth of the images, which we know.The generator is in a feedback loop with the discriminator.
<br>
Libraries used:
<br>
time
functools
math
numpy
Tensorflow
Image
Urllib.request
scipy.misc
Imageio
 
<br><br>
### Step 4 - Make art!
Run GANGogh.py
