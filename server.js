var express = require('express');
//var MongoDB = require('mongodb').MongoClient;
const mongoose = require('mongoose');
const mongKey = require('./keys').mongoURI;
const {User} = require('./User');
const app = express();
const bodyParser = require('body-parser');
var path = require('path')
mongoose.connect(mongKey).then(()=>{
    console.log("DB connected");
}).catch((error)=>{console.log(error);});

app.get('/', (req, res) => {
    res.send("Hello, World!");
})
app.get('/home.js', (req, res) => {
    res.sendFile(path.join(__dirname + "/home.js"))
})
app.get('/home', (req, res) => {
    res.sendFile(path.join(__dirname + "/Home.html"));
})
app.use(bodyParser.json());
app.post('/signup', (req, res)=>{
    const user = new User({
        name: req.body.name,
        email: req.body.email,
        password: req.body.password
    })
    user.save((err, response)=>{
        if (err) {
            res.status(400).send(err);
        }
        res.status(200).send(response);
    });
});

app.listen(3000, () => {
    console.log("Listening on port 3000");
});