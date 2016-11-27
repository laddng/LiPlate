from matplotlib import pyplot as plt;

def showResults(images, plates, plate_numbers):

  for index, image in enumerate(images):
    plotImage(image, plates[index], plate_numbers[index], index);

  plt.show();

  return True;

def plotImage(image, plate, plate_number, index):

  plt.figure(index);

  return True;

