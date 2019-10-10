import pytesseract
import pandas as pd
from PIL import Image
import sys
import os
os.system("darknet.exe detector test cfg/obj.data cfg/yolo-obj.cfg backup/yolo-obj_final.weight argv[1]")
pytesseract
img=Image.open(sys.argv[1])
text=pytesseract.image_to_string(img)
#print(text)
dataset=pd.read_csv("RTO.csv")
list1,list2,list3=[],[],[]
list1=dataset['RegNo']
list2=dataset['State']
list3=dataset['Place']
#input=input("Enter Reg Number")
for i in range(len(list1)):
	if (list1[i]==text[0,4]):
		a=list2[i]
		b=list3[i]
x=a+" "+b
print(x)