import React, { Component, PropTypes } from 'react';

import { Layout, Breadcrumb, Icon } from 'antd';

const { Header, Content, Sider, Footer } = Layout;

import HeaderPage from '../HeaderPage';

import SiderPage from './SiderPage';

// import 'antd/lib/content/style';

class WorkPage extends Component {
	static propTypes = {
		children: PropTypes.node,
		siderSelectedKey: PropTypes.string,
		breadcrunbs: PropTypes.array
	};

	static defaultProps = {
		siderSelectedKey: '1',
		breadcrunbs: ['工作', '三维制作']
	};

	render() {
		const { children } = this.props;

		return <Layout style={{backgroundColor: 'transparent'}}>
			<Header className="header" style={{
				backgroundColor: 'transparent',
				marginBottom: 20,
				padding: 0
			}}>
				<HeaderPage selected='work'/>
			</Header>
			<Layout>
				<Sider width={200} style={{ background: '#fff',  borderRight: '1px solid #e9e9e9' }}>
					<SiderPage selected={this.props.siderSelectedKey}/>
				</Sider>
				<Layout style={{ padding: 0 }}>
					<Breadcrumb style={{ margin: '12px 24px' }}>
						{this.props.breadcrunbs.map((item, index) => {
							return <Breadcrumb.Item key={index}>{item}</Breadcrumb.Item>;
						})}
					</Breadcrumb>
					<Content style={{ background: '#fff', padding: 24, margin: 0, minHeight: 280 }}>
          				{ children }
        			</Content>
				</Layout>
			</Layout>
			<Footer style={{ textAlign: 'center', borderTop: '1px solid #e9e9e9' }}>
		    	The Design ©2017 Created by Fun.Zheng
		    </Footer>
		</Layout>
	}
}

export default WorkPage;