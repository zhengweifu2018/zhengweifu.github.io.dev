import React, { Component } from 'react';

import WorkPage from './WorkPage';

import CommonRenderRelative from './CommonRenderRelative';

import { WEB_ROOT } from '../../config';

export default () => {
	return <WorkPage siderSelectedKey='1'  breadcrunbs={['工作', '三维制作']}>
		<CommonRenderRelative relativePathName={`${WEB_ROOT}images/threeMake/`} relativeFileName='relative.json' />
	</WorkPage>
};