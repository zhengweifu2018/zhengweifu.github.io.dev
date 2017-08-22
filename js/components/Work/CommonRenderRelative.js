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

		axios.get(relativeDir + this.props.relativeFileName).then((res) => {
			const data = res.data;
			for(const d of data) {
				// console.log(d);
				let each = {name: d.name, imagePath: relativeDir + d.imagePath, bgColor: d.bgColor, type: d.type}
				if(d.scriptPath !== undefined) {
					axios.get(relativeDir + d.scriptPath).then((res) => {
						each.code = res.data;
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
		relativeFileName: PropTypes.string.isRequired
	};

	static defaultProps = {};

	renderItems() {
		return this.state.scripts.map((item, index) => {
			const shl = item.code !== undefined ? 
				<SyntaxHighlighter language={item.type} style={xcode}>{item.code}</SyntaxHighlighter> : undefined;
			return <CodeBox key={index} title={item.name} codeComponent={shl}>
	            <div style={{textAlign: 'center', backgroundColor: item.bgColor}}><img src={item.imagePath} style={{maxWidth: '100%'}} /></div>
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