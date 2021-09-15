# Import the necessary libraries 
from PIL import Image 
import numpy as np
     
# creating a image1 object  
im1 = Image.open("CryptoHack/General/XOR/Lemur XOR/lemur.png") 
numpydata = np.array(im1) 


# creating a image2 object  
im2 = Image.open("CryptoHack/General/XOR/Lemur XOR/flag.png") 
numpydata1 = np.array(im2) 

numpydata2 = np.bitwise_xor(numpydata,numpydata1)

# image from our numpyarray 
Image.fromarray(numpydata2).show() 
 
