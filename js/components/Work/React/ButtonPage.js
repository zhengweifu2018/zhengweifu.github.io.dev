import React, { Component } from 'react';
import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import { GridList, RaisedButton } from 'zele-react';

import SyntaxHighlighter from 'react-syntax-highlighter';
import { xcode } from 'react-syntax-highlighter/dist/styles';

const RaisedButtonExampleSimple = [
    "import React from 'react';",
    "import { RaisedButton } from 'zele-react';",
    "",
    "const RaisedButtonExampleSimple = () => {",
    "   <div>",
    "        <GridList cols={3}>",
    "            <RaisedButton type='primary' label='Primary' fullWidth={true} disable={true}/>",
    "            <RaisedButton fullWidth={true}/>",
    "            <RaisedButton type='danger' label='Danger' fullWidth={true}/>",
    "        </GridList>",
    "   </div>",
    "};",
    "",
    "export default RaisedButtonExampleSimple;",
].join('\n');


const RaisedButtonExampleSize = [
    "import React from 'react';",
    "import { RaisedButton } from 'zele-react';",
    "",
    "const RaisedButtonExampleSize = () => {",
    "   <div>",
    "        <GridList cols={4}>",
    "            <RaisedButton type='primary' label='Large' fullWidth={true} size='large'/>",
    "            <RaisedButton type='primary' label='Normal' fullWidth={true}/>",
    "            <RaisedButton type='primary' label='Small' fullWidth={true} size='small'/>",
    "            <RaisedButton type='primary' label='Mini' fullWidth={true} size='mini'/>",
    "        </GridList>",
    "   </div>",
    "};",
    "",
    "export default RaisedButtonExampleSize;",
].join('\n');

export default () => {
    return <WorkPage siderSelectedKey='3-2-2' breadcrunbs={['工作', '前端开发', 'React 组件', 'Button 按钮']}>
        <h2>代码演示</h2>
        <GridList cols={2}>
            <CodeBox title='RaisedButton 类型' codeComponent={<SyntaxHighlighter language='javascript' style={xcode}>{RaisedButtonExampleSimple}</SyntaxHighlighter>}>
                <GridList cols={3}>
                    <RaisedButton type='primary' label='Primary' fullWidth={true} disable={true}/>
                    <RaisedButton fullWidth={true}/>
                    <RaisedButton type='danger' label='Danger' fullWidth={true}/>
                </GridList>
            </CodeBox>
            <CodeBox title='RaisedButton 大小' codeComponent={<SyntaxHighlighter language='javascript' style={xcode}>{RaisedButtonExampleSize}</SyntaxHighlighter>}>
                <GridList cols={4}>
                    <RaisedButton type='primary' label='Large' fullWidth={true} size='large'/>
                    <RaisedButton type='primary' label='Normal' fullWidth={true}/>
                    <RaisedButton type='primary' label='Small' fullWidth={true} size='small'/>
                    <RaisedButton type='primary' label='Mini' fullWidth={true} size='mini'/>
                </GridList>
            </CodeBox>
        </GridList>
        <h2>API</h2>
    </WorkPage>
};
