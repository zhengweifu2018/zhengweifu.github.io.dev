import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

require('../../../assets/images/twoToolDev/ai/relative.pro');

export default () => {
	return <WorkPage siderSelectedKey='6-1'  breadcrunbs={['工作', '平面工具开发', 'AI']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}assets/images/twoToolDev/ai/`} relativeFileName='relative.json' />
	</WorkPage>
};