import argparse
import numpy as np
import pims
import cv2 as cv
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
import skimage
from skimage import filters, exposure, feature, transform, color, draw

# Set matplotlib configuration.
mpl.use("pdf")
mpl.rcParams["image.cmap"] = "gray"

# Parse user arguments.
parser = argparse.ArgumentParser()
parser.add_argument('--dark_image', help='filepath to image captured in the dark')
parser.add_argument('--flat_image', help = 'filepath to uniform image captured under lighting')
parser.add_argument('--target_images', help='filepath to target images')
args = parser.parse_args()

# Given a TIFF stack layer, get the ideal circle and the fluctuation amplitudes.
# TODO: use parsed argument, not hardcoded file paths.
# images = pims.as_grey(pims.open("./.scratch/input/Cy5POPCPB_stack.tiff"))
images = pims.as_grey(pims.open("./.scratch/input/TS_test_40x.tiff_files/*.tiff"))
img = images[0]

# gamma_corrected = exposure.adjust_gamma(img, gamma=0.5)

gamma_corrected = exposure.equalize_hist(img)

# vmin, vmax = np.percentile(img, q=(0.5, 99.5))
# gamma_corrected = exposure.rescale_intensity(img, in_range=(vmin, vmax))

# gamma_corrected = exposure.equalize_adapthist(img, clip_limit=0.03)

# Compute intermediates.
# edges = filters.sobel(img)
edges = feature.canny(gamma_corrected)

# Circle detection
hough_radii = np.arange(20, 35, 2)
hough_res = transform.hough_circle(edges, hough_radii)
accums, cx, cy, radii = transform.hough_circle_peaks(hough_res, hough_radii, total_num_peaks=1)
print(cx)
print(cy)
print(radii)

# Render figures.
# TODO: use parsed argument, not hardcoded file paths.
with bpdf.PdfPages("./.scratch/output/out.pdf") as pdf:
    plt.imshow(img)
    plt.title("Input image")
    pdf.savefig()
    plt.close()

    plt.imshow(gamma_corrected)
    plt.title("Gamma corrected")
    pdf.savefig()
    plt.close()

    plt.imshow(edges)
    plt.title("Sobel edges")
    pdf.savefig()
    plt.close()

    edges = color.gray2rgb(edges)
    for center_y, center_x, radius in zip(cy, cx, radii):
        circy, circx = draw.circle_perimeter(center_y, center_x, radius, shape=edges.shape)
        edges[circy, circx] = (220, 20, 20)
    plt.imshow(edges)
    plt.title("Circles")
    pdf.savefig()
    plt.close()
