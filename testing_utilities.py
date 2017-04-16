import base64
import urllib
import requests
import json
from PIL import Image, ImageOps
from io import BytesIO
import toolz
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def read_image_from(url):
    return toolz.pipe(url, 
                      urllib.request.urlopen,
                      lambda x: x.read(),
                      BytesIO)


def to_rgb(img_bytes):
    return Image.open(img_bytes).convert('RGB')


@toolz.curry
def resize(img_file, new_size=(100, 100)):
    return ImageOps.fit(img_file, new_size, Image.ANTIALIAS)


def to_base64(img):
    imgio = BytesIO()
    img.save(imgio, 'PNG')
    imgio.seek(0)
    dataimg = base64.b64encode(imgio.read())
    return dataimg.decode('utf-8')


def to_img(img_url):
    return toolz.pipe(img_url,
                      read_image_from,
                      to_rgb,
                      resize(new_size=(224,224)))


def img_url_to_json(url):
    img_data = toolz.pipe(url,
                          to_img,
                          to_base64)
    return json.dumps({'input':'[\"{0}\"]'.format(img_data)})


def  _plot_image(ax, img):
    ax.imshow(to_img(img))
    ax.tick_params(axis='both',       
                   which='both',      
                   bottom='off',      
                   top='off',         
                   left='off',
                   right='off',
                   labelleft='off',
                   labelbottom='off') 
    return ax


def _plot_prediction_bar(ax, r):
    perf = list(c[1] for c in r.json()['result'][0][0])
    ax.barh(range(3, 0, -1), perf, align='center', color='#55DD55')
    ax.tick_params(axis='both',       
                   which='both',      
                   bottom='off',      
                   top='off',         
                   left='off',
                   right='off',
                   labelbottom='off') 
    tick_labels = reversed(list(' '.join(c[0].split()[1:]).split(',')[0] for c in r.json()['result'][0][0]))
    ax.yaxis.set_ticks([1,2,3])
    ax.yaxis.set_ticklabels(tick_labels, position=(0.5,0), minor=False, horizontalalignment='center')

    
def plot_predictions(images, classification_results):
    if len(images)!=6:
        raise Exception('This method is only designed for 6 images')
    gs = gridspec.GridSpec(2, 3)
    fig = plt.figure(figsize=(12, 9))
    gs.update(hspace=0.1, wspace=0.001)
    
    for gg,r, img in zip(gs, classification_results, images):
        gg2 = gridspec.GridSpecFromSubplotSpec(4, 10, subplot_spec=gg)
        ax = fig.add_subplot(gg2[0:3, :])
        _plot_image(ax, img)
        ax = fig.add_subplot(gg2[3, 1:9])
        _plot_prediction_bar(ax, r)
        

