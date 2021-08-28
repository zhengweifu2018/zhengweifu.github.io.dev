import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='5-4'  breadcrunbs={['工作', '引擎开发', '装修设计云']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}assets/images/engineDev/DecoDesign/`} relativeFileName='relative.json' />
	</WorkPage>
};