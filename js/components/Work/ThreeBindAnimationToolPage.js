import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='2-3'  breadcrunbs={['工作', '三维工具开发', '绑定 & 动画']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}images/threeToolDev/bind_animation/`} relativeFileName='relative.json' />
	</WorkPage>
};