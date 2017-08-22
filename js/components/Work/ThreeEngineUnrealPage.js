import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='5-3'  breadcrunbs={['工作', '引擎开发', 'Unreal']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}images/engineDev/unreal/`} relativeFileName='relative.json' />
	</WorkPage>
};