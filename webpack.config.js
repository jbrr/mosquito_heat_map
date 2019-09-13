"use strict"

const webpack = require("webpack"),
      path = require("path"),
      HtmlWebpackPlugin = require("html-webpack-plugin"),
      {CleanWebpackPlugin} = require('clean-webpack-plugin'),
      MiniCssExtractPlugin = require('mini-css-extract-plugin'),
      srcPath = path.resolve(__dirname, "src/client"),
      dotenv = require("dotenv"),
      env = dotenv.config({ path: srcPath + '/.env' }).parsed,
      WebpackMd5Hash = require("webpack-md5-hash"),
      LinkTypePlugin = require('html-webpack-link-type-plugin').HtmlWebpackLinkTypePlugin;

const envKeys = Object.keys(env).reduce((prev, next) => {
    prev[`process.env.${next}`] = JSON.stringify(env[next]);
    return prev;
  }, {});

module.exports = {
  target: "web",
  cache: true,
  entry: {main: path.resolve(srcPath, "index.js")},
  devServer: {
    contentBase: './dist',
    hot: true,
    writeToDisk: true
  },
  resolve: {
    alias: {
      leaflet_css: __dirname + "/node_modules/leaflet/dist/leaflet.css",
      leaflet_marker: __dirname + "/node_modules/leaflet/dist/images/marker-icon.png",
      leaflet_marker_2x: __dirname + "/node_modules/leaflet/dist/images/marker-icon-2x.png",
      leaflet_marker_shadow: __dirname + "/node_modules/leaflet/dist/images/marker-shadow.png"
    },
    modules: [srcPath, 'node_modules', 'public'],
    extensions: ['.js', '.jsx', '.scss', '.css']
    },
  module: {
    rules: [
      {
        test: /\.js(x)?$/,
        exclude: /node_modules/,
        loaders: ["babel-loader"]
      },
      {
        test: /\.html$/,
        loaders: ["html-loader"]
      },
      {
        test: /\.scss$/,
        use: [
          "style-loader",
          MiniCssExtractPlugin.loader,
          "css-loader",
          "sass-loader"
        ]
      },
      {
        test: /\.css$/,
        use: ['style-loader','css-loader'] 
      },
      {
        test: /\.(png|jpg)$/,
        loader: "file-loader?name=images/[name].[ext]"
      }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: "style.[hash].css"
    }),
    new HtmlWebpackPlugin({
      inject: false,
      hash: true,
      template: './src/client/index.ejs',
      filename: './index.html',
      minify: {
        collapseWhitespace: true,
        removeComments: true,
        removeRedundantAttributes: true,
        useShortDoctype: true
      }
    }),
    new webpack.DefinePlugin(envKeys),
    new WebpackMd5Hash(),
    new LinkTypePlugin()
  ],
  output: {
    path: path.resolve(__dirname, "dist"),
    publicPath: "dist/",
    filename: '[name].[hash].js'
  }
}