from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import glob
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# this is a PIL image
for py in glob.glob("cropped/F10/phrases/01/05/*"):
    img = load_img(py)
#img = load_img('cropped/F02/phrases/01/01/color_001.jpg')
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
# this is a Numpy array with shape (1, 3, 150, 150)
    x = x.reshape((1,) + x.shape)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir='preview', save_prefix='', save_format='jpeg'):
        i += 1
        if i > 20:
            break  # otherwise the generator would loop indefinitely
