import React, { Component } from 'react';
import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import { GridList, Icon, SimpleItem, Label } from 'zele-react';

import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/styles';

let iconTypes = [
    // Action
    'gLock',
    'gLockOpen',
    'gLockOutline',
    'gVisibility',
    'gVisibilityOff',
    'gHighlightOff',
    'gHelp',
    'gHelpOutline',
    'gDelete',
    'gDeleteForever',
    'gBuild',
    // Content
    'gClear',
    'gAddCircle',
    'gRemoveCircle',
    'gUndo',
    'gRedo',
    // Editor
    'gTitle',
    // Hardware
    'gKeyboardArrowDown',
    'gKeyboardArrowRight',
    'gKeyboardArrowLeft',
    'gKeyboardArrowUp',
    // Image
    'gImage',
    'gDehaze',
    'gTransform',
    'gBrush',
    // Navigation
    'gCheck',
    'gArrowBack',
    'gArrowDownward',
    'gArrowForward',
    'gArrowUpward',
    'gCancel'
];

const IconCodeString = "<Icon type='gLock' />";


export default () => {
    const icomElements = iconTypes.map((item, index) => {
        return <div style={{marginBottom: 10}} key={index}><SimpleItem title={item} defaultBorderColor='#e9e9e9' activeColor='#e9e9e9'>
            <Icon type={item} width={30} height={30} color='#08c'/>
            </SimpleItem></div>;
    });


    return <WorkPage siderSelectedKey='3-2-3' breadcrunbs={['工作', '前端开发', 'React 组件', 'Icon 图标']}>
        
        <div><Label content='如何使用' fontSize={20} height={40}/></div>
        <div><Label content='使用 <Icon /> 标签声明组件，指定图标对应的 type 属性，示例代码如下:' fontSize={14} height={30}/></div>
        <SyntaxHighlighter language='javascript' style={docco}>{IconCodeString}</SyntaxHighlighter>
        <div><Label content='图标列表' fontSize={20} height={40}/></div>
        <CodeBox title='Icon 类型'>
            <GridList cols={6}>
                {icomElements}
            </GridList>
        </CodeBox>
        <h2>API</h2>
    </WorkPage>
};
