import os
import imageio

def create_gif(fps, img_path, destination, name='/animation'):

    images = []
    file_names = os.listdir(img_path)
    files = sorted([int(file.split('.')[0]) for file in file_names])
    for file in files:
        # Read the image of each picture
        images.append(imageio.imread(img_path + str(file) + ".png"))

        print("Incorporated sim:", file)
    # Save it as a gif!
    imageio.mimsave(destination + name +'.gif', images,
                     fps=fps)

path = ".../K-NN/Figures/Normalized_Test/"
destination = ".../K-NN/Figures/"

create_gif(1, path, destination)