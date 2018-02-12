import json
import matplotlib.pyplot as plt
import numpy as np
from . import multi_image


def parse_output(tie_prob, sleeves_prob, casual_prob, strip_prob,beard_prob,shade_prob):    
    tmp = []
    formal_flag="Formal" if casual_prob[0]['tag']=='Formal' else "Casual"
    beard_flag="yes" if beard_prob[0]['tag']=='Beard Man' else "NO"
    tie_flag="yes" if tie_prob[0]['tag']=='With Tie' else "NO"
    p_shirt="yes" if strip_prob[0]['tag']=='Plain Shirts' else "NO"
    full_sleaves="Full" if sleeves_prob[0]['tag']=='Full Sleavs' else "Half"
    shade="Dark" if shade_prob[0]['tag']=='Dark' else "Light"
    
    tag_dic={'Attrie Type':formal_flag,'Beard':beard_flag,'Tie':tie_flag,'Plain Shirt':p_shirt,'Sleaves':full_sleaves,'Shade':shade}
    return tag_dic


def predict(path):
    tie_prob = multi_image.tie_or_not(path)
    sleevs_prob = multi_image.full_half(path)
    casual_prob = multi_image.formal_casual(path)
    strip_prob = multi_image.plain_strip(path)
    beard_prob= multi_image.beard(path)
    shad_prob=multi_image.shades(path)
    #print(tie_prob, sleevs_prob, casual_prob, strip_prob,beard_prob,shad_prob)
    return(parse_output(tie_prob, sleevs_prob, casual_prob, strip_prob,beard_prob,shad_prob))

# print(predict('/home/lucifer/Desktop/beard/beard/media/images%20(6).jpeg'))
