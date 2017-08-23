import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='4-1'  breadcrunbs={['工作', '后端开发', 'PHP']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}assets/images/serverDev/php/`} relativeFileName='relative.json' />
	</WorkPage>
};