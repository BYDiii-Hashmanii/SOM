import os
import cv2
import csv

label_dic={'cardboard':0,'glass':1,'metal':2,'paper':3,'plastic':4,'trash':5}
l=list(label_dic.keys())#['a','b','c']
with open(f'Bewerage_110.csv','w',newline='')as csvfile:
    for i in l: #'a', 'b', 'c'
        writer=csv.writer(csvfile)
        path = 'C:/Users/Cv/Desktop/5th semester/Garbage classification/Garbage classification/Garbage classification//' + i
        for r,d,f in os.walk(path):
            for filename in f:
                if '.jpg'in filename:
                    record=[]
                    file_path=os.path.join(path,filename)
                    image=cv2.imread(file_path)
                    image=cv2.resize(image,(110,110))
                    #rest of processing
                    label=label_dic[i]#0,1,2
                    record.append(label)
                    final_image=image.flatten()
                    record.extend(final_image)
                    writer.writerow(record)                    