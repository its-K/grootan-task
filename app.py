from flask import Flask,render_template,jsonify
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
usersdata=[
    {"name":"Kishore","age":21,"dob":"04-11-2000","email":"kishore4110@gmail.com","firstname":"Kishore","lastname":"B","img":"https://avatars.githubusercontent.com/u/31382690?v=4","more":{"address":"1/119 unkown village, udumalpet","district":"tiruppur","pincode":642122}},
    {"name":"Person1","age":24,"dob":"04-11-1986","email":"person1@gmail.com","firstname":"Person","lastname":"1","img":"https://thumbs.dreamstime.com/b/vector-illustration-avatar-dummy-icon-set-image-stock-design-logo-collection-137159370.jpg","more":{"address":"1/23,unknown location","district":"texas","pincode":641024}},
    {"name":"Person2","age":26,"dob":"04-11-1879","email":"person2@gmail.com","firstname":"Person","lastname":"2","img":"https://image.freepik.com/free-vector/man-avatar-profile-round-icon_24640-14044.jpg","more":{"address":"2/23,unknown location","district":"dublin","pincode":641223}},
    {"name":"Person3","age":25,"dob":"04-11-1995","email":"person3@gmail.com","firstname":"Person","lastname":"3","img":"https://pixy.org/src/31/315160.png","more":{"address":"3/34,unknown location","district":"paris","pincode":560231}},
    {"name":"Person4","age":27,"dob":"04-11-1987","email":"person4@gmail.com","firstname":"Person","lastname":"4","img":"https://thumbs.dreamstime.com/b/vector-illustration-avatar-dummy-logo-set-image-stock-isolated-object-icon-collection-137161298.jpg","more":{"address":"4/45,unknown location","district":"austin","pincode":543212}},
    {"name":"Person5","age":45,"dob":"04-11-1984","email":"person5@gmail.com","firstname":"Person","lastname":"5","img":"https://image.freepik.com/free-vector/man-avatar-profile-round-icon_24640-14044.jpg","more":{"address":"5/12,unknown location","district":"ireland","pincode":243544}},
    {"name":"Person6","age":12,"dob":"04-11-2010","email":"person6@gmail.com","firstname":"Person","lastname":"6","img":"https://www.w3schools.com/w3images/avatar5.png","more":{"address":"6,32,unknown location","district":"coimbatore","pincode":642123}},
    {"name":"Person7","age":49,"dob":"04-11-1989","email":"person7@gmail.com","firstname":"Person","lastname":"7","img":"https://image.freepik.com/free-vector/man-avatar-profile-round-icon_24640-14044.jpg","more":{"address":"7/11,unknown location","district":"karur","pincode":643212}},
    {"name":"Person8","age":34,"dob":"04-11-1983","email":"person8@gmail.com","firstname":"Person","lastname":"7","img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkfF6nBhidhIzL330CYtg70I8tpDBGJ2YjBPnE9D9gY0iLmGu563WBIab4KBexSDv7kG8&usqp=CAU","more":{"address":"8/12,unknown location","district":"ooty","pincode":642123}},
    {"name":"Person9","age":34,"dob":"04-11-1983","email":"person8@gmail.com","firstname":"Person","lastname":"7","img":"https://image.freepik.com/free-vector/man-avatar-profile-round-icon_24640-14044.jpg","more":{"address":"8/12,unknown location","district":"ooty","pincode":642123}}
]

@app.route('/users')
@cross_origin()
def users():
    return jsonify(usersdata)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)