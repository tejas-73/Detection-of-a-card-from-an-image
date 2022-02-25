# Detection-of-a-card-from-an-image
Detection of a card from an image is a well recognised problem in computer vision. Here is a way to implement the same. 
Card Images I have considered is in Images folder

I also tried on some apparel images. Some House images. And the results are more or less quite convincing.
These Images are in Extra_Images folder
# Methods of Implementation
# 1) Using Patched K-Means Clustering and Averaging.
Most of the Images that we see today have illumination effects in them, because of which, the clustering algorithm may get misled by unwanted clustering resulting in illumination artifacts.

The method to tackle this was to take patches and cluster intensities in it. taking a class mean intensity will reduce the high intensity values present in a patch and will enhance low intensity values. Thus we can make better classification and our algorithm wont get mislead.

The number of patches to consider was arbitrary and it does matter what the outputs we might get at the end. I have kept the patches to be 64.

In this algorithm, there is a requirement of patches to be in even powers of 2, because the algorithm is implemented in such a way and else it might throw error.
# 2) Using YUV colour scheme to reduce the effect of illumination changes and segment.
As discussed, illumination is a big reason to worry when comming to image segmentation. Therefore, I have also implemented a way to reduce the illumination effects.

YUV format is used to seperate out the parts of images that are responsible for giving Illuminance and chrominance. Hence we can easily alter them.

The input image was fed such that illumination effects are minimum and segmentation was directly done into two classes.

# Illustrations of image results
**Image 1:**

![card (11)](https://user-images.githubusercontent.com/97820591/155699736-ff6f4d59-8e32-4717-831b-7aa16923c4f3.jpg) 

(Notice Illumination effects)

![1](https://user-images.githubusercontent.com/97820591/155700988-d404aebe-d93e-4fee-b0a7-dbeaeac453c8.jpg) 

This was segmentation from method1

![3](https://user-images.githubusercontent.com/97820591/155700890-73c0ca65-d200-4a2b-9d44-4fec25242e9c.jpg)

This was Segmentation from Method 2


**Image 2:**

![card (18)](https://user-images.githubusercontent.com/97820591/155701434-66b85507-3146-4a2e-9625-e9a86c6707af.jpg) 

(Note that card has multiple intensities)

![1](https://user-images.githubusercontent.com/97820591/155701523-65d28c4d-3e94-45ca-88b2-45a62d54ac99.jpg) 

This was from method1

![2](https://user-images.githubusercontent.com/97820591/155701569-ce79a6ab-7756-4002-a744-538897af894f.jpg) 

This was from method2


**Image 3:**

![card (51)](https://user-images.githubusercontent.com/97820591/155702035-570acc6c-d89b-4704-a3c8-54a7238ba4ee.jpg) 

(Note colour of card and background is same)

![1](https://user-images.githubusercontent.com/97820591/155702133-d350278d-dd8e-44c0-970e-85dacb80ad3b.jpg) 

This is from Method1


![3](https://user-images.githubusercontent.com/97820591/155702183-e100b8fc-f32c-40c1-a93e-adec7870484d.jpg) 

This is from Method2


**Image 4:**

![image (7)](https://user-images.githubusercontent.com/97820591/155702625-ecf529aa-39fa-4bc7-a626-8e9aad5b2011.jpg) 


![1](https://user-images.githubusercontent.com/97820591/155702714-bc7787cd-d6ef-46ba-a79c-e896e20ed633.jpg) 

This was from Method1


![3](https://user-images.githubusercontent.com/97820591/155702747-4b126117-f029-4f54-bf0b-13ecc82b48e9.jpg) 

This was from Method2


**Image 5:**

![image (11)](https://user-images.githubusercontent.com/97820591/155702992-10d31351-7dc8-494d-bd06-c4719671c49b.jpg)


![1](https://user-images.githubusercontent.com/97820591/155703042-a1e60887-717f-467a-979e-6cb1b54a2a0c.jpg) 

This was from Method1


![3](https://user-images.githubusercontent.com/97820591/155703107-9eb42649-0659-4392-8576-f0e46e40c7df.jpg)

This was from Method2


**Image 6:**

![card (49)](https://user-images.githubusercontent.com/97820591/155703235-51db70d5-97bd-45b9-8ad8-ee44323868ab.jpg) 


![1](https://user-images.githubusercontent.com/97820591/155703352-df263fcd-76dd-47f8-961c-928277141200.jpg) 

This was from method1


![2](https://user-images.githubusercontent.com/97820591/155703403-273906a1-f0db-4713-9247-ae88c07157b4.jpg) 

This was from method2

**Image 7:**

![image (8)](https://user-images.githubusercontent.com/97820591/155705171-1165a33e-c95b-4f92-93a1-afc267db18b3.jpg)


![1](https://user-images.githubusercontent.com/97820591/155705276-3a411e89-0caf-463b-839f-18bf0f194f8c.jpg)

This was from Method1

![3](https://user-images.githubusercontent.com/97820591/155705328-e178f3cf-0807-4551-b82f-00b0d345ea41.jpg)

This was from Method2


**Image 8:**

![card (50)](https://user-images.githubusercontent.com/97820591/155705516-b5622f0e-3ca2-4a57-8daa-45b0492455bc.jpg)



![1](https://user-images.githubusercontent.com/97820591/155705563-6473c6b7-52bf-4f3c-b2b1-e3495716f163.jpg)

This was from Method1

![3](https://user-images.githubusercontent.com/97820591/155705634-4ab501ba-72d9-46af-950a-b1872aeec594.jpg)

This was from Method2

**Image 9:**

![card (48)](https://user-images.githubusercontent.com/97820591/155705813-f172bd3c-d928-4569-a045-a47f621d3748.jpg)



![1](https://user-images.githubusercontent.com/97820591/155705921-05af9b44-fa03-4086-8980-0fe56fc65b57.jpg)

This was from Method1

![3](https://user-images.githubusercontent.com/97820591/155705990-f19738a0-229b-45f2-95e7-473d03edd76d.jpg)

This was from Method2


# General Comments
Ofcourse method1 can take preprocessed images from method2 and perform much better, but the results didnt appeared to be much fascinating. 

One method worked on some images and badly failed on other and viceversa. So, this might give an intuition for why merging both methods may give more worse results.

The results for some images in the dataset were also not much perfectly segmented, but one can easily apply Hough Transform to get lines, which can easily ensure with high probability of detection of card. 

Also see that the final image has only two colours as far as method1 is concerned for the segmentation purpose. Method2 directly gives us segmentation of image.
One can definitely try for more images!
