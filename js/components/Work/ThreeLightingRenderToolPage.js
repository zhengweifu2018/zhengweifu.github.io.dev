import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='2-2'  breadcrunbs={['工作', '三维工具开发', '灯光 & 渲染']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}images/threeToolDev/lighting_render/`} relativeFileName='relative.json' />
	</WorkPage>
};