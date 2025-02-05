import os

from ultralytics import YOLO
import cv2
# medium_model_path = "/content/gdrive/MyDrive/yolov8/Object-Detection/coin-det/yolo-medium/train/weights/best.pt"
# small_model_path = "/content/gdrive/MyDrive/yolov8/Object-Detection/coin-det/yolo-small/runs/detect/train/weights/best.pt"

#model_path = "/content/runs/detect/train/weights/best.pt"
model = YOLO("weights/best.pt")


def write_label_bounding_box(img, class_id, x1, y1, x2, y2, score,result):
  score_str = 'Score: {:.2f}'.format(score)
  class_name = result.names[int(class_id)].replace("₹", "")
  text = class_name + ' ' + score_str

  if class_id == 0:
      color = (255, 128, 0)
  elif class_id == 1:
      color = (0, 165, 255)
  elif class_id == 2:
      color = (147, 20, 255)
  elif class_id == 3:
      color = (255, 0, 255)
  else:
      color = (0, 0, 0)  # Default color

  cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 20)
  cv2.putText(img, text, (int(x1), int(y1 - 30)), cv2.FONT_HERSHEY_SIMPLEX, 4, color, 20, cv2.LINE_AA)

  return img

def prediction(img,model):
  #img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
  results = model(img)#[0]
  result = results[0]
  threshold = 65
  output = {}
  output['₹1'],output['₹2'],output['₹5'],output['₹10'] = 0,0,0,0

  for i in result.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = i
    if score >= threshold/100:
      pred_class = result.names[class_id]

      output[pred_class] += 1
      img = write_label_bounding_box(img,class_id,x1, y1, x2, y2,score,result)


  total = (output['₹1'])+(2*output['₹2'])+(5*output['₹5'])+(10*output['₹10'])

  text = f"Total = {total}"
  font = cv2.FONT_HERSHEY_SIMPLEX
  font_scale = 1
  color = (0, 255, 0)
  thickness = 2
  #text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
  height, width, _ = img.shape
  #print(height,width)

  # Define the position for the text (adjust as needed)
  x = height - 1000  # X-coordinate (vertical)
  y = width - 1000   # Y-coordinate (horizontal)
  x,y = 500,300

  # Put text on the image
  cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 10, color, 30, cv2.LINE_AA)

  return img

path = "Projects/Coin_Detection/Coins/1.jpg"
img = cv2.imread(path)
img = prediction(img,model)
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resize",resized)

cv2.waitKey(0)