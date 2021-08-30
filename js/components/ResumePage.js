import React, { Component } from 'react';

import ReactDOM from 'react-dom';

import { Route } from 'react-router-dom';

import HeaderPage from './HeaderPage';

import { WEB_ROOT } from '../config';

// export default () => {
// 	return <div>
// 		<HeaderPage selected='resume'/>
// 		<iframe style={{
// 			marginTop: 20,
// 			width: '100%',
// 			height: 4000
// 		}} src={`${WEB_ROOT}resume.html?` + (new Date()).getTime().toString()} frameBorder="0" scrolling="no" marginWidth="0" marginHeight="0"></iframe>
// 	</div>
// }

export default class ResumePage extends React.Component {
	constructor() {
		super();
		this.state = {
			iFrameHeight: 0
		}
  	}
   
	render() {
	  	return <div>
			<HeaderPage selected='resume'/>
			<iframe style={{
				width: '100%', marginTop: 20, height: `${this.state.iFrameHeight}px`, overflow: 'visible'
			}} onLoad={() => {
				const obj = ReactDOM.findDOMNode(this).children[1];
				console.log(obj);
				if (this.state.iFrameHeight <= 0) {
					this.setState({
						"iFrameHeight": obj.contentWindow.document.body.scrollHeight
					});
				}
			}} 
			src={`${WEB_ROOT}resume.html?` + (new Date()).getTime().toString()} 
			width="100%" 
			height={this.state.iFrameHeight} 
			scrolling="no" 
			frameBorder="0"/>
	  	</div>;
	}
  }