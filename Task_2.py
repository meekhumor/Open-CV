import cv2 
import numpy as np 

# finding largest diamond in top panel of image
def detect_large_diamond(img):
    left_width = []
    right_width = []
    distance = []
    height_element = 0

    # finding the height of the leftmost element of first diamond
    width = img.shape[1] - 1
    while (width > 0):
        height = img.shape[0] - 1
        while (height > 0):
            if (img[height,width] < 100):
                height_element = height
            height = height - 1
        width = width - 1

    # finding and storing the width of leftmost element and rightmost element of all the diamond
    width = 0
    while (width <= img.shape[1]-1):
        height= 0
        while (height <= height_element):
            if (img[height,width] < 100  and height == height_element and (img[height, width+1] > 100 or img[height, width-1] > 100)):
                if(img[height, width+1] > 100):
                    right_width.append(width)
                if(img[height, width-1] > 100):
                    left_width.append(width)
                cv2.circle(img, (width,height),5,100, thickness = cv2.FILLED) #(img, location, size,color,thickness) 
                break
            height = height + 1
        width = width + 1

    left = np.array(left_width)
    right = np.array(right_width)

    # finding and storing the distance of all diamond 
    distance = right - left
    idx = np.argmax(distance) # index of max element in this list represent location of larger diamond
    std = np.std(distance) # standard deviation of all the distances

    # cv2.imshow("img",img)

    return idx,std

# finding index of larger rhombus in top_panel and left_panel 
def diamond_index(img):
    rotated_img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    index1,std1 = detect_large_diamond(img)
    index2,std2 = detect_large_diamond(rotated_img_90)

    if(std1 < 2):
        rotated_img_180 = cv2.rotate(img, cv2.ROTATE_180)
        index1, index2 = diamond_index(rotated_img_180)

    return index1,6-index2


# reading the input image 
img = cv2.imread('Task_2\\task3_pics\\tc2-3.png',0)
img = img[40:760, 40:560]

index1, index2= diamond_index(img)

left_panel = ["ace", "2", "3", "4", "5", "6"]
top_panel = ["heart", "club", "spade", "diamond"]

# printing the desired output
print(left_panel[index2-1], 'of', top_panel[index1-1])

cv2.waitKey(0)


# -------------------------------------------------- Previous Solution ---------------------------------------------------------

# import cv2 
# import numpy as np 

# # finding distance of diagonal (rhombus):
# def diagonal_distance(img):
#     single_rhombus = img[40:160, 40:160] # cropping out image such that it contain single rhombus
#     left_width = 0
#     right_width = 0
#     # traversing in a image matrix from top to bottom
#     for w in range(0,single_rhombus.shape[1]):
#         for h in range(0,single_rhombus.shape[0]):
#             # Checking if the pixel intensity is below the threshold
#             if (single_rhombus[h, w] < 100):
#                 left_width = w
#                 break
#         else:
#             continue
#         break
#     for w in range(0,single_rhombus.shape[1]):
#         for h in range(0,single_rhombus.shape[0]):
#             if (single_rhombus[h, w] < 100):
#                 right_width = w
#                 break
        
#     distance = right_width - left_width
#     return distance + 3


# # function to split the image into two desired segment
# def split_image(img):

#     # Cropping image
#     cropped_img = img[40:760, 40:560]
#     height,width = cropped_img.shape[:2]

#     top_panel = cropped_img[0:120, 100:width]
#     left_panel = cropped_img[0:height , 0:120]

#     # Displaying desired segment
#     # cv2.imshow('Top panel', top_panel)
#     # cv2.imshow('Left panel', left_panel)

#     return (top_panel, left_panel)

# # function to detect larger rhombus
# def detect_rhombus(img):
    
#     # finding the height of the element of first rhombus
#     width=0
#     count = 0
#     height_element = 0

#     while (width < img.shape[1]):
#         height = 0
#         while (height < img.shape[0]):
#             if (img[height,width] < 100):
#                 height_element = height
#                 break
#             height = height + 1
#         else:
#             width = width + 1
#             continue
#         break

#     # print(height_element)

#     # finding no. of rhombus in the image till larger rhombus is found
#     while (width < img.shape[1]):
#         height=0
#         while (height < img.shape[0]):
#             if (img[height,width] < 150):
#                 if (height < height_element+2 and height > height_element-2):
#                     # print(width,height)
#                     count = count + 1
#                     # cv2.circle(img, (width,height),5,0, thickness = cv2.FILLED) #(img, location, size,color,thickness)

#                 # increasing width by distance of diagonal to jump over current rhombus such that we can find leftmost point of next rhombus
#                 width = width + 80
#                 break
#             height = height + 1
#         if (img[height_element,width] < 150): # if we found dark spot after jumping over rhombus then that rhombus is larger and hence we must break the loop
#             break
#         width = width + 1

#     # cv2.imshow('', img) # it displays leftmost point of all rhombus till larger rhombus is found 
#     return count

# # displaying index of larger rhombus in top_panel ans left_panel 
# def rhombus_index(img):
#     top_panel,left_panel = split_image(img)
#     rotated_left_panel = cv2.rotate(left_panel, cv2.ROTATE_90_COUNTERCLOCKWISE)

#     index1 = detect_rhombus(top_panel)
#     index2 = detect_rhombus(rotated_left_panel)

#     return index1,index2

# # reading the input image 
# img = cv2.imread('task3_pics\\tc1-3.png',0) 

# index1,index2 = rhombus_index(img)

# left_panel = ["ace", "2", "3", "4", "5", "6"]
# top_panel = ["heart", "club", "spade", "diamond"]

# # printing the desired output
# if(index1 == 4 and index2 == 6):
#     rotated_img = cv2.rotate(img, cv2.ROTATE_180)
#     rotated_index1,rotated_index2 = rhombus_index(rotated_img)

#     print(left_panel[rotated_index2-1], 'of', top_panel[rotated_index1-1])

# else:
#     print(left_panel[index2-1], 'of', top_panel[index1-1])

# cv2.waitKey(0)
