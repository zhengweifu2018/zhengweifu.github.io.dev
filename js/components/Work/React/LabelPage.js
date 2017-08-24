import React, { Component } from 'react';
import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import ApiTable from './ApiTable';

import { Label } from 'zele-react';

import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/styles';

import { WEB_ROOT } from '../../../config';


const LabelCodeString = "<Label content='zele-react' height={30} color='#f85635'/>";

export default () => {
    return <WorkPage siderSelectedKey='3-2-7' breadcrunbs={['工作', '前端开发', 'React 组件', 'Input 输入框']}>
        <div><Label content='如何使用' fontSize={20} height={40} color='#000'/></div>
        <div><Label content='使用 <label /> 标签声明组件，指定对应的属性，示例代码如下:' fontSize={14} height={30}/></div>
        <SyntaxHighlighter language='html' style={docco}>{LabelCodeString}</SyntaxHighlighter>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/`} fileName='Label.json' titleColor='#000'/>
    </WorkPage>
};