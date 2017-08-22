import React, { Component } from 'react';

import { Menu, Button } from 'antd';

import { Route } from 'react-router-dom';

import HeaderPage from './HeaderPage';

import { WEB_ROOT } from '../config';

export default () => {
	return <div>
		<HeaderPage selected='resume'/>
		<iframe style={{
			marginTop: 20,
			width: '100%',
			height: 3000
		}} src={`${WEB_ROOT}resume.html`} frameBorder="0" scrolling="no" marginWidth="0" marginHeight="0"></iframe>
	</div>
}