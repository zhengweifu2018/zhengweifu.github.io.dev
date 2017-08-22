import React, { Component, PropTypes } from 'react';

import { Menu, Icon } from 'antd';

class HeaderPage extends React.Component {

	static propTypes = {
		selected: PropTypes.string
	};

	static defaultProps = {
		selected: 'main'
	};

	onClickHandle(option) {
		let webPath = '/';
		switch(option.key) {
			case 'work':
				webPath = '/work/threemodeltool';
				break;
			case 'resume':
				webPath = '/resume';
				break;
		}
		window.location.href = '#' + webPath;

	}

  	render() {
		return <Menu
			selectedKeys={[this.props.selected]}
			mode="horizontal"
			onClick={this.onClickHandle.bind(this)}
			style={{ lineHeight: '64px' }}
		>
			<Menu.Item key="main">
				首页
			</Menu.Item>
			<Menu.Item key="work">
				工作
			</Menu.Item>
			<Menu.Item key="resume">
				简历
			</Menu.Item>
		</Menu>
	}
}

export default HeaderPage;