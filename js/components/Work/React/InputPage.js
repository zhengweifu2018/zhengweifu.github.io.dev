import React, { Component } from 'react';
import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import ApiTable from './ApiTable';

import { Label } from 'zele-react';

import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/styles';

import { WEB_ROOT } from '../../../config';


const InputCodeString = "<Input placeholder='在这里输入值' />\n\n<InputNumber value={10} />";

export default () => {
    return <WorkPage siderSelectedKey='3-2-5' breadcrunbs={['工作', '前端开发', 'React 组件', 'Input 输入框']}>
        <div><Label content='如何使用' fontSize={20} height={40} color='#000'/></div>
        <div><Label content='使用 <Input /> 标签声明组件，指定输入框对应的属性，示例代码如下:' fontSize={14} height={30}/></div>
        <SyntaxHighlighter language='html' style={docco}>{InputCodeString}</SyntaxHighlighter>
        <div><Label content='API' fontSize={20} height={40} color='#000'/></div>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Input/`} fileName='Input.json' title='Input' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Input/`} fileName='InputNumber.json' title='InputNumber' titleSize={14}/>
    </WorkPage>
};