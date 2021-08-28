const merge = require('webpack-merge');
const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const common = require('./webpack.common.js');


module.exports = merge(common, {
    mode: 'production',
    devtool: false,
    plugins: [
        new CleanWebpackPlugin(['dist'],{
            root: path.resolve(__dirname, '../')
        }),
    ],
    optimization: {
        minimizer: [
            new TerserPlugin({
                parallel: true,
                terserOptions:{
                    output:{
                        comments: false
                    }
                }
            })
        ],
    },
    performance:{
        hints: false
    }
});