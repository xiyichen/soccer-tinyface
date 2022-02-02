import pafy
import cv2
import face_recognition

videos = []

for p in videos:
	n, url = p
	print(n)
	print(url)
	vPafy = pafy.new(url)
	play = vPafy.getbest(preftype="mp4")
	print(play.resolution)

	#start the video
	cap = cv2.VideoCapture(play.url)
	fps = cap.get(cv2.CAP_PROP_FPS)
	count = 0
	start = cv2.CAP_PROP_POS_MSEC
	timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
	calc_timestamps = [0.0]
	prev = 0
	while (True):
		ret,frame = cap.read()
		if frame is None:
			break
		face_locations = face_recognition.face_locations(frame)
		for t in face_locations:
			print(t)
			top, right, bottom, left = t
			h = bottom-top
			w = right-left
			if h >= 25 and w >= 25 and h <= 60 and w <= 60:
				cropped_face = frame[top:bottom, left:right]
				ts = cap.get(cv2.CAP_PROP_POS_MSEC)
				cts = calc_timestamps[-1] + 1000/fps
				time = int(abs(ts - cts))
				cv2.imwrite('./results/' + str(n) + '/' + str(time) + '_' + str(count) + '.jpg', cropped_face)
				count += 1

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

cap.release()
cv2.destroyAllWindows()
