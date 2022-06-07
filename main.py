# main.py

from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('small-beach.jpg')
pix = im.load()

fig, ax = plt.subplots()

def cc(input):
    return (input[0]/255, input[1]/255, input[2]/255)

for i in range(300):
    for j in range(300):
        ax.add_patch(plt.Circle(((j/im.size[1]), (i/im.size[0])), 1/1000, color=cc(pix[i, j])))

fig.savefig('output.png')
