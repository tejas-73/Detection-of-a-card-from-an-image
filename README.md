# Detection-of-a-card-from-an-image
Detection of a card from an image is a well recognised problem in computer vision. Here is a way to implement the same. 
Card Images I have considered is in Images folder

I also tried on some apparel images. Some House images. And the results are more or less quite convincing.
These Images are in Extra_Images folder
# Methods of Implementation
# 1) Using Patched K-Means Clustering and Averaging.
Most of the Images that we see today have illumination effects in them, because of which, the clustering algorithm may get misled by unwanted clustering resulting in illumination artifacts.

The method to tackle this was to take patches and cluster intensities in it. taking a class mean intensity will reduce the high intensity values present in a patch and will enhance low intensity values. Thus we can make better classification and our algorithm wont get mislead.

The number of patches to consider was arbitrary and it does matter what the outputs we might get at the end.

In this algorithm, there is a requirement of patches to be in even powers of 2, because the algorithm is implemented in such a way and else it might throw error.
# 2) Using YUV colour scheme to reduce the effect of illumination changes and segment.
As discussed, illumination is a big reason to worry when comming to image segmentation. Therefore, I have also implemented a way to reduce the illumination effects.

YUV format is used to seperate out the parts of images that are responsible for giving Illuminance and chrominance. Hence we can easily alter them.

The input image was fed such that illumination effects are minimum and segmentation was directly done into two classes.
# General Comments
Ofcourse method1 can take preprocessed images from method2 and perform much better, but the results didnt appeared to be much fascinating. 

The results for one method worked on some images and badly failed on other and viceversa. So, Maybe the case that merging the two might give much more worst results.

The results for some images in the dataset were also not much perfectly segmented, but one can easily apply Hough Transform to get lines, which can easily ensure with high probability of detection of card. 

Also see that the final image has only two colours as far as method1 is concerned for the segmentation purpose. Method2 directly gives us segmentation of image.

One can definitely try for more images!

