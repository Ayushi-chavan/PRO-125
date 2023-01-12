from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
	'id': 1,
	'Name': request.json['Name'],
	'Contact':request.json.get('Contact', ""),
	'done':False

}]


@app.route("/add-data", methods=["POST"])
def add_task():
	if not request.json:
		return jsonify({
			"status": "error",
			"message": "Please provide the data!"
		}, 400)
  contact = {
    'id': contacts[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
    }
  contacts.append(contact)
  return jsonify({
    "status":"success",
    "message": "Task added succesfully!"
    })

if(__name__=="__main__"):
    app.run(debug=True)

X = np.load('image.npz')['arr_0']
y = pd.read_csv("labels.csv")["labels"]

print(pd.Series(y).value_cunts())

classes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nclasses = len(classes)


X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=9, train_size=3500, test_size=500)

def get_prediction(image):

	im_pil = Image.open(image)
	image_bw = im_pil.convert('L')
	image_bw_resized = image_bw.resize((22,30), Image.ANTIALIAS)
	pixel_filter = 20
	min_pixel = np.percentile(image_bw_resized, pixel_filter)
	image_bw_resized_inverted_scaled = np.clip(image_bw_resized-min_pixel, 0,255)
	max_pixel = np.max(image_bw_resized)


	image_bw_resized_inverted_scaled = np.asarray(image_bw_resized_inverted_scaled)/max_pixel
	test_sample = np.array(image_bw_resized_inverted_scaled).reshape(1,660)
	test_pred = clf.predict(test_sample)
	return test_pred[0]

    @app.route("/predict-alphabet",methods=["	POST"])

def predict_data():

	image = request.files.get("alphabet")
	prediction = get_prediction(image)
	return jsonify({
		"prediction": prediction
}), 200