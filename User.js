const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
      },
      email: {
        type: String,
        required: true
      },
      password: {
        type: String,
        required: true
      },
      favorites: {
          type: [{type: String}],
          required: false
      }
});

const User = mongoose.model("Users", UserSchema);

module.exports = {User};