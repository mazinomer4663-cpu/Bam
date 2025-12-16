import imageio.v3 as iio

filenames = ['Omning_It', 'Mark..', 'Just_think_a_lil.']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

