import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='3-1'  breadcrunbs={['工作', '引擎开发', 'DVS3D']}>
		<CommonRenderRelative useIframe={true} relativePathName={`${WEB_ROOT}assets/images/webDev/webgl/`} relativeFileName='relative.json' />
	</WorkPage>
};