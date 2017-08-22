import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='5-2'  breadcrunbs={['工作', '引擎开发', 'Unity3D']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}images/engineDev/unity3d/`} relativeFileName='relative.json' />
	</WorkPage>
};