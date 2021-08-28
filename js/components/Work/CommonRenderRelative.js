import React, { Component, PropTypes } from 'react';

import axios from 'axios';

import CodeBox from '../CodeBox';

import SyntaxHighlighter from 'react-syntax-highlighter';
import { xcode } from 'react-syntax-highlighter/dist/styles';

class CommonRenderRelative extends Component {
	constructor(props) {
		super(props);

		this.state = {
			scripts : []
		}

		const relativeDir = this.props.relativePathName;

		axios.get(relativeDir + this.props.relativeFileName + '?' + (new Date()).getTime().toString()).then((res) => {
			const data = res.data;
			for(const d of data) {
				// console.log(d);
				let each = {name: d.name, bgColor: d.bgColor, type: d.type, isVideo: false}
				if(this.props.useIframe) {
					each.webPath = d.webPath;
					each.webHeight = d.webHeight;
				} else {
					each.isVideo = !!d.isVideo;
					each.imagePath = relativeDir + d.imagePath;
				}
				// console.log(relativeDir + d.scriptPath)
				if(d.scriptPath !== undefined) {
					axios.get(relativeDir + d.scriptPath).then((res) => {
						each.code = res.data;
						// console.log(res.data);
						let scripts = this.state.scripts;
						scripts.push(each);
						this.setState({scripts: scripts});
					}).catch(e => console.log(e));
				} else {
					let scripts = this.state.scripts;
					scripts.push(each);
					this.setState({scripts: scripts});
				}
			}
		}).catch(e => console.log(e));
	}

	static propTypes = {
		relativePathName: PropTypes.string.isRequired,
		relativeFileName: PropTypes.string.isRequired,
		useIframe: PropTypes.bool
	};

	static defaultProps = {
		useIframe: false
	};

	renderItems() {
		return this.state.scripts.map((item, index) => {
			const contentElement = this.props.useIframe
			? <iframe style={{
					width: '100%',
					height: item.webHeight
				}} src={item.webPath} frameBorder="0" scrolling="no" marginWidth="0" marginHeight="0"></iframe>
				: <div style={{ textAlign: 'center', backgroundColor: item.bgColor }}>
					{item.isVideo ? <video src={item.imagePath} style={{ maxWidth: '100%' }} controls="controls">您的浏览器不支持 video 标签。</video> : <img src={item.imagePath} style={{ maxWidth: '100%' }} />}</div>;

			const shl = item.code !== undefined ? 
				<SyntaxHighlighter language={item.type} style={xcode}>{item.code}</SyntaxHighlighter> : undefined;
			
			return <CodeBox key={index} title={item.name} codeComponent={shl} open={true}>
	            {contentElement}
	        </CodeBox>
		});
	}

	render() {
		return <div>
			{this.renderItems()}
		</div>;
	}
};

export default CommonRenderRelative;