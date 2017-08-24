import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='3-1'  breadcrunbs={['工作', '前端开发', 'WebGL']}>
		<CommonRenderRelative useIframe={true} relativePathName={`${WEB_ROOT}assets/images/webDev/webgl/`} relativeFileName='relative.json' />
	</WorkPage>
};