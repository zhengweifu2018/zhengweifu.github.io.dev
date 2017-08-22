import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='2-1'  breadcrunbs={['工作', '三维工具开发', '模型']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}images/threeToolDev/model/`} relativeFileName='relative.json' />
	</WorkPage>
};