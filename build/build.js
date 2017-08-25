const fs = require('fs');

const path = require('path');

const buildConfig = require('./build_config');

const deleteFolderRecursive = (path) => {

    let files = [];

    if( fs.existsSync(path) ) {

        files = fs.readdirSync(path);

        files.forEach(function(file,index){

            const curPath = path + "/" + file;

            if(fs.statSync(curPath).isDirectory()) { // recurse

                deleteFolderRecursive(curPath);

            } else { // delete file

                fs.unlinkSync(curPath);

            }

        });

        fs.rmdirSync(path);

    }

};

(() => {
	const argvs = process.argv.splice(2);

	console.log(argvs[1], argvs[1] != 0)
	let webpackCommonConfig = buildConfig(false, argvs[1] != 0);
	if(argvs[0] === "server") {
		webpackCommonConfig = buildConfig(true, argvs[1] != 0);
		deleteFolderRecursive(path.resolve(__dirname, '../dist'));
	}

	const configJS = [
		"exports.WEB_ROOT = './';",
		"exports.PUBLIC_PATH = exports.WEB_ROOT + 'dist/';"
	];

	fs.writeFileSync('../js/config.js', configJS.join('\n'));

	fs.writeFileSync('webpack.config.js', webpackCommonConfig);
})();