import cv2
import mediapipe as mp


def draw_shape():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode = False,
        max_num_hands = 1,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5
    )
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("unable to open camera")
        exit()

    line_anchor1 = []
    line_anchor2 = []
    base_image = None
    combined = None
    c=0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)


        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                h, w, c = frame.shape
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                idx, idy = int(index_tip.x * w), int(index_tip.y * h)

                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thx,thy = int(thumb_tip.x * w), int(thumb_tip.y * h)

                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    #mp_hands.HAND_CONNECTIONS
                )

                key = cv2.waitKey(1)
                if key == ord('s'):
                    line_anchor1.append((idx,idy))
                    line_anchor2.append((thx,thy))
                for i,j in zip(line_anchor1,line_anchor2):
                    cv2.line(frame,i,j,(0,255,0),3)
            

                if (idx,idy) and (thx,thy):
                    cv2.circle(frame,(idx,idy),10,(255,0,0),-1)#blue
                    cv2.circle(frame,(thx,thy),10,(0,0,255),-1)#red
                    cv2.line(frame,(idx,idy),(thx,thy),(255,255,255),3)


        cv2.imshow('finger tracking',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def write():
    l1 = []
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode = False,
        max_num_hands = 1,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5
    )
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("unable to open camera")
        exit()
    
    while cap.isOpened():
        success,frame = cap.read()
        if not success:
            print("must close camera")
            break
    
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                h, w, c = frame.shape
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                

                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    #mp_hands.HAND_CONNECTIONS
                )

                key = cv2.waitKey(1)
                if key == ord('s'):
                    idx, idy = int(index_tip.x * w), int(index_tip.y * h)
                    l1.append((idx,idy))
                
                for i in l1:
                    cv2.circle(frame,(i[0],i[1]),5,(255,0,255),-1)
                
        cv2.imshow('finger tracking',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


choice = int(input("enter 1 to write and 2 to draw lines :"))
if choice == 1:
    write()
elif choice == 2:
    draw_shape()
else:
    print("invalid choice")
