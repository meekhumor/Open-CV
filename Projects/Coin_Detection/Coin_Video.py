import cv2
from ultralytics import YOLO
model = YOLO("weights/last.pt")

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

  cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
  cv2.putText(img, text, (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv2.LINE_AA)

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
  x,y = 50,30

  # Put text on the image
  cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 4, cv2.LINE_AA)

  return img



# Open the video file

cap = cv2.VideoCapture(2)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_path = 'output_video.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        #results = model(frame)

        # Visualize the results on the frame
        #annotated_frame = results[0].plot()
        annotated_frame = prediction(frame,model)
        # cv2.imshow(annotated_frame)
        out.write(annotated_frame)
        # Convert annotated_frame to OpenCV format
        annotated_frame = annotated_frame[:, :, ::-1]

        # Display the annotated frame
        cv2.imshow("ann", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()