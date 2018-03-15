#This code allows you to select a single image and artificially adjust the
#exposure using gamma shift. The resulting comparagram is instead an insight
#on how the gamma adjustment works.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_gamma(image, gamma):
    invGamma=1.0/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def plot_data(image, adj_image):
    npimage = np.array(image)
    npadj_image = np.array(adj_image)

    img_b = npimage[:,:,0].flatten()
    #img_g = npimage[:,:,1].flatten()
    #img_r = npimage[:,:,2].flatten()

    for i in range(0, 15):
        print(i)
        adj_img_b = npadj_image[i,:,:,0].flatten()
        #adj_img_g = npadj_image[i,:,:,1].flatten()
        #adj_img_r = npadj_image[i,:,:,2].flatten()
        plt.scatter(adj_img_b, img_b, s=0.3, label="gamma = %.1f" % (i))
        #plt.scatter(adj_img_g, img_g, s=0.3)
        #plt.scatter(adj_img_r, img_r, s=0.3)

    plt.ylabel('Adjusted Gamma')
    plt.xlabel('Original Photo')
    plt.show()

def show_img(adj_image, gamma_val):
    cv2.namedWindow('gamma = %.1f' % (gamma_val))
    cv2.imshow('gamma = %.1f' % (gamma_val), adj_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    # Adjust the below line for the path to your image
    image = cv2.imread('image.jpg')
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gets a bunch of gamma-adjusted images
    adj_image = []
    for i in range(1, 16):
        adj_image.append(adjust_gamma(image, i/10))

    show_img(adj_image[2], 0.3)
    show_img(adj_image[4], 0.5)
    show_img(adj_image[9], 1.0)
    show_img(adj_image[14], 1.5)

    plot_data(image, adj_image)
