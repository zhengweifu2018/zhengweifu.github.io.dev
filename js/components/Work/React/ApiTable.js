import React, { Component, PropTypes } from 'react';

import { Label } from 'zele-react';

import { Table } from 'antd';

import axios from 'axios';

const columns = [{
  title: '参数',
  dataIndex: 'parameter',
  key: 'parameter',
}, {
  title: '说明',
  dataIndex: 'intrduce',
  key: 'intrduce',
}, {
  title: '类型',
  dataIndex: 'type',
  key: 'type',
}, {
  title: '默认值',
  dataIndex: 'default',
  key: 'default',
}];

class ApiTable extends Component {
	constructor(props) {
		super(props);

		this.state = {
			dataSource : []
		}

		const relativeDir = this.props.pathName;

		axios.get(relativeDir + this.props.fileName).then((res) => {
			const data = res.data.map((item, index) => {
				return Object.assign({}, item, {key: index})
			});
			this.setState({dataSource: data});
		}).catch(e => console.log(e));
	}

	static propTypes = {
		pathName: PropTypes.string.isRequired,
		fileName: PropTypes.string.isRequired,
		title:PropTypes.string,
		titleSize: PropTypes.number,
		titleHeight: PropTypes.number,
		titleColor:PropTypes.string
	};

	static defaultProps = {
		title: 'API',
		titleSize: 20,
		titleHeight: 40,
		titleColor: 'rgb(158, 158, 158)'
	};

	render() {
		return <div>
			<div><Label content={this.props.title} fontSize={this.props.titleSize} height={this.props.titleHeight} color={this.props.titleColor}/></div>
        	<Table dataSource={this.state.dataSource} columns={columns} bordered={true} pagination={false}/>
		</div>;
	}
};

export default ApiTable;