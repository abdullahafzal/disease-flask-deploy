import flask
from flask import request, jsonify
import sqlite3

from flask_cors import CORS
app = flask.Flask(__name__)
CORS(app)

conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('CREATE TABLE IF NOT EXISTS MyUsers (firstName TEXT, lastName TEXT, ins_ID TEXT, city TEXT, dob TEXT, date TEXT)') #Run this line just one time to create table

@app.route('/prediction', methods=['POST'])
def api_image():
    # Database
    # firstName = request.args['fname']
    # lastName = request.args['lname']
    # ins_ID = request.args['ins_ID']
    # city = request.args['city']
    # dob = request.args['dob']
    # date1 = request.args['date']
    #
    # with sqlite3.connect("database.db") as con:
    #     cur = con.cursor()
    #     cur.execute('INSERT INTO MyUsers VALUES(?, ?, ? ,? ,? ,?)',(firstName, lastName, ins_ID, city, dob, date1))
    #
    #     con.commit()
    #     print("Record successfully added")
    #
    # model_name = request.args["model"]
    # photo = request.files['photo']
    # in_memory_file = io.BytesIO()
    # photo.save(in_memory_file)
    # data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
    # color_image_flag = 1
    # orig = cv2.imdecode(data, color_image_flag)
    # model_path = ""
    #
    # # load the pre-trained network
    # print("[INFO] loading pre-trained network...")
    # if model_name in "cancer":
    #     print("cancer model loaded")
    #     model_path = r"breast_cancer_model.model" # Please enter the path for breast-cancer model
    #
    # elif model_name in "malaria":
    #     print("Maalaria model loaded")
    #     model_path = r"malaria_model.model" # Please enter the path for Malaria model
    #
    # elif model_name in "spiral":
    #     print("Spiral model loaded")
    #     model_path = r"spiral_model.model" # Please enter the path for Spiral model
    #
    #     if random.randint(3,6)%2:
    #         print("IFFFFFFFFFFFFFFFFFFFFFFFFFFff")
    #         res = {"Prediction":"0"}
    #         return jsonify(res)
    #
    # elif model_name in "wave":
    #     print("Wave model loaded")
    #     model_path = r"wave_model.model" # Please enter the path for wave model
    #
    #
    # model = load_model(model_path)
    # # initialize our list of results
    # results = []
    #
    # # pre-process our image by converting it from BGR to RGB channel
    # # ordering (since our Keras mdoel was trained on RGB ordering),
    # # resize it to 64x64 pixels, and then scale the pixel intensities
    # # to the range [0, 1]
    # image = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    # image = cv2.resize(image, (48, 48))
    # image = image.astype("float") / 255.0
    #
    # # order channel dimensions (channels-first or channels-last)
    # # depending on our Keras backend, then add a batch dimension to
    # # the image
    # image = img_to_array(image)
    # image = np.expand_dims(image, axis=0)
    #
    # # make predictions on the input image
    # pred = model.predict(image)
    #
    # print("pred: ", pred)
    # pred = pred.argmax(axis=1)[0]
    #
    # # an index of zero is the 'parasitized' label while an index of
    # # one is the 'uninfected' label
    # label = "UnInfected" if pred == 0 else "Infected"
    # color = (0, 0, 255) if pred == 0 else (0, 255, 0)
    #
    # # resize our original input (so we can better visualize it) and
    # # then draw the label on the image
    # orig = cv2.resize(orig, (128, 128))
    # cv2.putText(orig, label, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
    #             color, 2)
    #
    # # add the output image to our list of results
    # results.append(orig)
    #
    # # show the output montage
    # #cv2.imshow("Results", montage)
    # #cv2.waitKey(0)
    #
    # # else:
    # #     return "Error: No image address field provided."
    #
    # # Use the jsonify function from Flask to convert our list of
    # # Python dictionaries to the JSON format.
    # res = {}
    pred = 1
    if pred == 1:
        res = {"Prediction":"1"}
        print(res)
    else:
        res = {"Prediction":"0"}
        print(res)
    return jsonify(res)

app.run()


