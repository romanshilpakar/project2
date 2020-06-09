import cv2
import pandas as pan

double = False
r = g = b = xcordinate = ycordinate = 0

#Read the image with opencv
img = cv2.imread('sample.png')


#Read csv file(using pandas) & give names to each column
index=["color","color_name","hex","R","G","B"]
csv = pan.read_csv('colorfile.csv', names=index, header=None)

#function to calculate minimum distance from all colors and get the most matching color
def NameOfColor(R,G,B):
    mini = 10000
    for i in range(len(csv)):
        j = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(j<=mini):
            mini = j
            colorname = csv.loc[i,"color_name"]
    return colorname



#to get x,y coordinates after mouse double click by user

def get_func(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xcordinate,ycordinate, double
        double = True
        xcordinate = x
        ycordinate = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',get_func)

while(1):

    cv2.imshow("image",img)
    if (double):
   
        #  syntax : cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #display Color name and RGB values 
        text = NameOfColor(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        # syntax : cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        # display black colour for very light colours 
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        double=False

    #Close the loop when after 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
