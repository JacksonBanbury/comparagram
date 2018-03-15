import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot_data(image, image2):
    npimage = np.array(image)
    npimage2 = np.array(image2)

    img_b = npimage[:,:,0].flatten()
    img_g = npimage[:,:,1].flatten()
    img_r = npimage[:,:,2].flatten()

    img2_b = npimage2[:,:,0].flatten()
    img2_g = npimage2[:,:,1].flatten()
    img2_r = npimage2[:,:,2].flatten()
    plt.scatter(img2_b, img_b, s=0.3, c='b')
    plt.scatter(img2_g, img_g, s=0.3, c='g')
    plt.scatter(img2_r, img_r, s=0.3, c='r')

    plt.ylabel('JPG')
    plt.xlabel('Raw')
    plt.show()

    return none

if __name__ == "__main__":

    image1 = cv2.imread('jpg.JPG')
    image2 = cv2.imread('raw.RW2')
    print(np.shape(image1))
    plot_data(image1, image2)
