const path = require('path');

module.exports = {
  entry: './home/home.js',
  output: {
    filename: 'correct.js',
    path: path.resolve(__dirname, 'home'),
  },
  module:{
    rules: [
        {
          test: /\.m?js$/,
          exclude: /(node_modules|bower_components)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
              plugins: ['@babel/plugin-proposal-object-rest-spread']
            }
          }
        },
        {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            use: [
              {
                loader: 'babel-loader',
                options: {
                  presets: ['react']
                }
              }
            ],
          }
      ]
  }
};