import React, { Component, PropTypes } from 'react';

import { Icon } from 'antd';

class CodeBox extends Component {
	constructor(props) {
		super(props);

		this.state={
			open: props.open
		};
	}

	static propTypes = {
		children: PropTypes.node,
		codeComponent: PropTypes.node,
		borderColor: PropTypes.string,
		title: PropTypes.string,
		bottomSize: PropTypes.number,
		open: PropTypes.bool
	};

	static defaultProps = {
		open: false,
		borderColor: '#e9e9e9',
		bottomSize: 20,
		title: 'tile'
	};

	render() {
		const { children, codeComponent, borderColor, title, bottomSize } = this.props;
		const padding = 10;
		const isOpen = this.state.open && codeComponent !== undefined;
		const codeIcon = codeComponent !== undefined ?
			<span style={{
					position: 'absolute',
					top: padding + 2,
					right: padding + 2
				}} onClick={e => {
					this.setState({open: !this.state.open});
				}}><Icon type={this.state.open ? 'code-o' : 'code'} style={{ fontSize: 16, color: '#08c' }}/></span> :
			'';
		return <div style={{
			border: `1px solid ${borderColor}`,
			borderRadius: 4,
			marginBottom: bottomSize
		}}>
			<div style={{padding: padding}}>{children}</div>
			<div style={{
				borderTop: `1px solid ${borderColor}`,
				padding: padding,
				position: 'relative'
			}}>
				<h3>{title}</h3>
				{codeIcon}
			</div>
			<div style={{
				display: isOpen ? 'block' : 'none',
				borderTop: `1px dashed ${isOpen ? borderColor : 'transparent'}`,
				maxHeight: 500,
				overflow: 'auto',
				padding: padding - 6
			}}>
				{codeComponent}
			</div>
		</div>;
	}
}

export default CodeBox;