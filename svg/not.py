#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2009, Sugar Labs

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys
import os
import os.path
import gettext

def main():

    myname = "not"
    mystring = "not"
    mygroup = "numbers"

    if len(sys.argv) != 2:
        print "Error: Usage is " + myname + ".py lang"
        return

    t = gettext.translation("org.laptop.TurtleArtActivity", "../locale", languages=[sys.argv[1]])
    _ = t.ugettext
    t.install()

    print _(mystring)

    data0 = \
"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?> \n \
<svg \n \
   xmlns=\"http://www.w3.org/2000/svg\" \n \
   xmlns:xlink=\"http://www.w3.org/1999/xlink\" \n \
   width=\"82\" \n \
   height=\"45\" \n \
   version=\"1.0\"> \n \
  <defs> \n \
    <linearGradient \n \
       id=\"linearGradient3166\"> \n \
      <stop \n \
         style=\"stop-color:#ffffff;stop-opacity:1;\" \n \
         offset=\"0\" \n \
         id=\"stop3168\" /> \n \
      <stop \n \
         style=\"stop-color:#ff00ff;stop-opacity:1;\" \n \
         offset=\"1\" \n \
         id=\"stop3170\" /> \n \
    </linearGradient> \n \
    <linearGradient \n \
       xlink:href=\"#linearGradient3166\" \n \
       id=\"linearGradient3172\" \n \
       x1=\"0\" \n \
       y1=\"22\" \n \
       x2=\"81\" \n \
       y2=\"22\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
  </defs> \n \
  <path \n \
     style=\"fill:url(#linearGradient3172);stroke:#a000a0;stroke-width:1.50000000000000000;stroke-opacity:1;fill-opacity:1;opacity:1\" \n \
     d=\"M 81.5,0.5 L 52.184836,1.0946482 C 48.067642,1.1781641 41.389663,1.6361149 37.299849,2.1174546 C 33.873939,2.5206579 29.222297,3.248216 25.862124,4.028389 C 22.692508,4.7643181 18.365568,5.5610531 15.36737,6.8255165 C 13.084928,7.788116 9.844096,8.9699361 7.8592915,10.452059 C 6.3063049,11.611728 4.4309072,13.439472 3.2387792,14.967684 C 2.4840103,15.935237 1.6096745,17.352305 1.1777379,18.500898 C 0.80137523,19.50171 0.5007638,20.93076 0.5,22 C 0.49928515,23.000722 0.81886695,24.324532 1.1296286,25.27578 C 1.4937185,26.390267 2.1370867,27.841955 2.8000171,28.808994 C 3.7185158,30.14884 5.2539783,31.729416 6.5314467,32.73286 C 8.1587459,34.011095 10.035683,35.507397 11.918817,36.365182 C 14.32795,37.462564 17.712344,38.523245 20.256311,39.255638 C 22.654562,39.94608 31.841463,41.630103 34.839679,41.950768 L 54,44 L 81.5,44.5 L 81.5,41.5 C 81.5,41.5 77.395011,40.863389 75.669659,40.433376 C 73.739724,39.952375 68.641131,39.216464 65.189353,36.764503 C 65.189353,36.764503 60.564346,34.279867 59.187108,32.894525 C 57.956771,31.656948 56.397781,29.312001 55.648115,27.736143 C 54.949896,26.26843 54.555327,23.752729 54.566595,22.12744 C 54.5795,20.266029 55.406924,17.791597 56.341871,16.181973 C 57.423539,14.319752 59.589033,12.29889 61.299148,10.989929 C 63.279802,9.4738913 66.304312,7.9855935 68.603232,7.0179533 C 70.547739,6.1994893 73.287879,5.4998596 75.324226,4.9482432 C 77.161021,4.4506826 81.5,4 81.5,4 L 81.5,0.5\" /> \n \
  <text \n \
     style=\"font-size:12px;text-anchor:middle;text-align:center;font-family:Bitstream Vera Sans\"> \n \
     <tspan \n \
       x=\"32\" \n \
       y=\"28\" \n \
       style=\"font-size:18\">"

    data1 = \
"</tspan></text> \n \
</svg> \n"

    FILE = open(os.path.join("../images", sys.argv[1], mygroup, myname + ".svg"), "w")
    FILE.write(data0)
    FILE.write(_(mystring).encode("utf-8"))
    FILE.write(data1)
    FILE.close()
    return

if __name__ == "__main__":
    main()