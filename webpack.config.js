"use strict"

const webpack = require("webpack"),
      path = require("path"),
      HtmlWebpackPlugin = require("html-webpack-plugin"),
      srcPath = path.resolve(__dirname, "src/client");

module.exports = {
    target: "web",
    cache: true,
    entry: path.resolve(srcPath, "index.js"),
    devServer: {
        contentBase: path.join(__dirname, 'dist')
    },
    resolve: {
        alias: {
            leaflet_css: __dirname + "/node_modules/leaflet/dist/leaflet.css",
            leaflet_marker: __dirname + "/node_modules/leaflet/dist/images/marker-icon.png",
            leaflet_marker_2x: __dirname + "/node_modules/leaflet/dist/images/marker-icon-2x.png",
            leaflet_marker_shadow: __dirname + "/node_modules/leaflet/dist/images/marker-shadow.png"
        }
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.html$/,
                use: [
                  {
                    loader: "html-loader"
                  }
                ]
            },
            {
                test:/\.css$/,
                use:['style-loader','css-loader']
            },
            {
                test: /\.(png|jpg)$/,
                loader: "file-loader?name=images/[name].[ext]"
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        template: "./src/client/index.html",
        filename: "./index.html"
        })
    ],
    output: {
        path: path.resolve(__dirname, "dist"),
        publicPath: "dist/",
        filename: "[name].js"
    }
}