import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import json
import re
import random_resp



def att_sys():
    path = 'imagees'
    imagees = []
    personnames = []
    mylist = os.listdir(path)
    # print(mylist)

    for cu_img in mylist:
        current_img = cv2.imread(f'{path}/{cu_img}')
        imagees.append(current_img)
        personnames.append(os.path.splitext(cu_img)[0])

    # print(personnames)

    def faceEncodings(imagees):
        encodelist = []
        for img in imagees:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
        return encodelist

    def attendance(name):
        with open('attendance.csv', 'r+') as f:
            mydatalist = f.readlines()
            namelist = []
            for line in mydatalist:
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                time_now = datetime.now()
                tstr = time_now.strftime('%H:%M:%S')
                dstr = time_now.strftime('%d/%m/%y')
                f.writelines(f'\n{name},{tstr},{dstr}')

    encodelistKnown = faceEncodings(imagees)
    print('All encodings complete!!')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGRA2RGB)
        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodelistKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodelistKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personnames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                attendance(name)

        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) == 13:  # this is for enter key
            break

    cap.release()
    cv2.destroyAllWindows()
def capture_img():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Capture Yourself", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            name=input("enter your name")
            img_name = "{}.jpg".format(name)
            cv2.imwrite(os.path.join('imagees',img_name),frame)
            #cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))

    cam.release()

    cv2.destroyAllWindows()

def chatbot_faq():
    def load_json(file):
        with open(file) as bot_responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(bot_responses)

    # Store JSON data
    response_data = load_json("bot.json")

    def get_response(input_string):
        split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        score_list = []

        # Check all the responses
        for response in response_data:
            response_score = 0
            required_score = 0
            required_words = response["required_words"]

            # Check if there are any required words
            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            # Amount of required words should match the required score
            if required_score == len(required_words):
                # print(required_score == len(required_words))
                # Check each word the user has typed
                for word in split_message:
                    # If the word is in the response, add to the score
                    if word in response["user_input"]:
                        response_score += 1

            # Add score to list
            score_list.append(response_score)
            # Debugging: Find the best phrase
            # print(response_score, response["user_input"])

        # Find the best response and return it if they're not all 0
        best_response = max(score_list)
        response_index = score_list.index(best_response)

        # Check if input is empty
        if input_string == "":
            return "Please type something so we can chat :("

        # If there is no good response, return a random one.
        if best_response != 0:
            return response_data[response_index]["bot_response"]

        return random_resp.random_string()

    while True:
        user_input = input("You: ")
        print("Bot:", get_response(user_input))