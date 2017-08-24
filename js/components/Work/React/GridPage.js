import React, { Component } from 'react';

import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import { Grid, Col, GridList, Label } from 'zele-react';

import ApiTable from './ApiTable';

import { WEB_ROOT } from '../../../config';

const GridListExample = [
    "import React from 'react';",
    "import { GridList, Label } from 'zele-react';",
    "",
    "function createGridLists(count, gutter) {",
    "    let result = [];",
    "    for(let i = 0; i < count; i ++) {",
    "        result.push(<div key={i} style={{backgroundColor:'#ecf6fd', marginBottom: 5, textAlign: 'center'}}>",
    "            <Label height={30} content={`cols = ${count}`}/>",
    "        </div>);",
    "    }",
    "    return <GridList cols={count} gutter={gutter}>{result}</GridList>",
    "}",
    "",
    "const GridListExample = () => {",
    "    <div>",
    "        {createGridLists(1, 5)}",
    "        {createGridLists(2, 5)}",
    "        {createGridLists(3, 5)}",
    "        {createGridLists(4, 5)}",
    "        {createGridLists(5, 5)}",
    "        {createGridLists(6, 5)}",
    "        {createGridLists(7, 5)}",
    "        {createGridLists(8, 5)}",
    "        {createGridLists(9, 5)}",
    "        {createGridLists(10, 5)}",
    "    </div>",
    "};",
    "",
    "export default GridListExample;"
].join('\n');

const GridColExample = [
    "import React from 'react';",
    "import { GridList, Label } from 'zele-react';",
    "",
    "function createGridCol(widthList, gutter) {",
    "    let result = [], i = 0;",
    "    for(let w of widthList) {",
    "        result.push(<Col key={i} width={w}><div style={{backgroundColor:'#ecf6fd', marginBottom: 5, textAlign: 'center'}}>",
    "            <Label height={30} content={`width = ${w}`}/>",
    "        </div></Col>);",
    "        i ++;",
    "    }",
    "",
    "    return <Grid gutter={gutter}>{result}</Grid>",
    "}",
    "",
    "const GridColExample = () => {",
    "    <div>",
    "       {createGridCol([1], 5)}",
    "       {createGridCol([0.5, 0.5], 5)}",
    "       {createGridCol([0.2, 0.5, 0.3], 5)}",
    "       {createGridCol([0.1, 0.2, 0.3, 0.4], 5)}",
    "       {createGridCol([0.2, 0.3, 0.05, 0.2, 0.15, 0.1], 5)}",
    "    </div>",
    "};",
    "",
    "export default GridColExample;"
].join('\n');


import SyntaxHighlighter from 'react-syntax-highlighter';
import { xcode } from 'react-syntax-highlighter/dist/styles';

function createGridCol(widthList, gutter) {
    let result = [], i = 0;
    for(let w of widthList) {
        result.push(<Col key={i} width={w}><div style={{backgroundColor:'#ecf6fd', marginBottom: 5, textAlign: 'center'}}>
            <Label height={30} content={`width = ${w}`}/>
        </div></Col>);
        i ++;
    }

    return <Grid gutter={gutter}>{result}</Grid>
}

function createGridLists(count, gutter) {
    let result = [];
    for(let i = 0; i < count; i ++) {
        result.push(<div key={i} style={{backgroundColor:'#ecf6fd', marginBottom: 5, textAlign: 'center'}}>
            <Label height={30} content={`cols = ${count}`}/>
        </div>);
    }

    return <GridList cols={count} gutter={gutter}>{result}</GridList>
}

export default () => {
    return <WorkPage siderSelectedKey='3-2-4' breadcrunbs={['工作', '前端开发', 'React 组件', 'Grid 栅格']}>
        <div><Label content='演示' fontSize={20} height={40} color='#000'/></div>
        <CodeBox title='Grid + Col' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{GridListExample}</SyntaxHighlighter>}>
            {createGridCol([1], 5)}
            {createGridCol([0.5, 0.5], 5)}
            {createGridCol([0.2, 0.5, 0.3], 5)}
            {createGridCol([0.1, 0.2, 0.3, 0.4], 5)}
            {createGridCol([0.2, 0.3, 0.05, 0.2, 0.15, 0.1], 5)}
        </CodeBox>
        <CodeBox title='GridList' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{GridListExample}</SyntaxHighlighter>}>
            {createGridLists(1, 5)}
            {createGridLists(2, 5)}
            {createGridLists(3, 5)}
            {createGridLists(4, 5)}
            {createGridLists(5, 5)}
            {createGridLists(6, 5)}
            {createGridLists(7, 5)}
            {createGridLists(8, 5)}
            {createGridLists(9, 5)}
            {createGridLists(10, 5)}
        </CodeBox>
        <div><Label content='API' fontSize={20} height={40} color='#000'/></div>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Grid/`} fileName='Grid.json' title='Grid' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Grid/`} fileName='Col.json' title='Col' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Grid/`} fileName='GridList.json' title='GridList' titleSize={14}/>
    </WorkPage>
};