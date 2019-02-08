#This file contains various denoiseing techniques using the denoising filters

#https://scipy-lectures.org/packages/scikit-image/auto_examples/plot_filter_coins.html

import numpy as np
from skimage import filters, restoration
import torch

def applyDenoisingFilter(img, filter= 'median'):
    adv_images = adv_images.detach().cpu().squeeze(0).numpy()
    filtered_images= filters.gaussian(adv_images, sigma=2)
    filtered_images= torch.from_numpy(filtered_images).unsqueeze(0)
    return filtered_images

