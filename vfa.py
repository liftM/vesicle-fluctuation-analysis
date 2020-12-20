import pims
import cv2 as cv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
import skimage.filters as skif


# Configure matplotlib backend.
matplotlib.use('pdf')

# TODO: Parse arguments.

# Given a TIFF stack layer, get the ideal circle and the fluctuation amplitudes.
# TODO: use parsed argument, not hardcoded file paths.
images = pims.as_grey(pims.open('./.scratch/input/Cy5POPCPB_stack.tiff'))
img = images[0]

# Compute intermediates.
edges = skif.sobel(img)

# Render figures.
# TODO: use parsed argument, not hardcoded file paths.
with bpdf.PdfPages('./.scratch/output/out.pdf') as pdf:
  plt.imshow(img)
  plt.title('Input image')
  pdf.savefig()
  plt.close()

  plt.imshow(edges)
  plt.title('Sobel edges')
  pdf.savefig()
  plt.close()
