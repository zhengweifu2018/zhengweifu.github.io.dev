const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const SRC_PATH = path.join(__dirname, '../src');
const GLOBAL_STYLE_PATH = path.join(__dirname, '../src/app/styles');
// const GLOBAL_STYLE_PATH = SRC_PATH + '/app/styles';
const NODE_MODULES_PATH = path.join(__dirname, '../node_modules');
const isDev = (Array.isArray(process.argv) ? process.argv.join('') : process.argv).indexOf('development') > -1;

function md5File(path) {
    var data = fs.readFileSync(path);
    var md5Value = crypto.createHash('md5').update(data, 'utf8').digest('hex');
    return md5Value
}

module.exports = {
    entry: {
        index: SRC_PATH + '/app/ui/AppNoSeparate.js',
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, '../dist')
    },
    module: {
        rules: [{
            test: /\.js$/,
            use: ['babel-loader?cacheDirectory=true'],
            include: SRC_PATH
        },
        {
            test: /\.jsx?$/,
            use: ['babel-loader?cacheDirectory=true'],
            include: SRC_PATH
        },
        // {
        //     test: /\.js$/,
        //     loader: ['eslint-loader'],
        //     enforce: 'pre',
        //     include: SRC_PATH
        // },
        {
            test: /\.(png|jpg|gif|svg|eot|ttf|woff)$/,
            use: [{
                loader: 'url-loader',
                options: {
                    limit: 8192,
                    fallback: 'file-loader'
                }
            }]
        },
        {
            test: /\.css$/,
            exclude: [NODE_MODULES_PATH,GLOBAL_STYLE_PATH],
            use: [
                'style-loader',
                {
                    loader: 'css-loader',
                    options: {
                        modules: true,
                        localIdentName: '[name]__[local]-[hash:base64:5]'
                    }
                }
            ]
        },
        {//处理antd的样式和全局样式，不走css-modules处理
            test: /\.css$/,
            include: [NODE_MODULES_PATH,GLOBAL_STYLE_PATH],
            use: [
                {
                    loader: MiniCssExtractPlugin.loader,
                },
                'css-loader'
            ]
        },
        {
            test: /\.less$/,
            use: [{
                loader: 'style-loader'
            },
            {
                loader: 'css-loader'
            },
            {
                loader: 'less-loader',
                options: {
                    javascriptEnabled: true
                }
            }
            ]
        }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        mainFiles: ['index'],
        // alias: {
        //     pages: SRC_PATH + '/app/ui/pages',
        //     components: SRC_PATH + '/app/ui/components',
        //     '@': SRC_PATH
        // }
    },
    plugins: [
        new HtmlWebpackPlugin({
            filename: 'index.html',
            template: SRC_PATH + '/template.html',
            isDev,
        }),

        new MiniCssExtractPlugin({
            filename: '[name].css',
            chunkFilename: '[id].css'
        }),

        new CopyWebpackPlugin([
            { from: 'assets' },
            { from: 'bimplatform' }
        ]),
    ]
};