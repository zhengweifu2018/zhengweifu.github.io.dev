import React, { Component } from 'react';
import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import ApiTable from './ApiTable';

import { GridList, Slider, InputNumberSlider, InputNumberSliderGroup, Label, Paper } from 'zele-react';

import SyntaxHighlighter from 'react-syntax-highlighter';
import { xcode } from 'react-syntax-highlighter/dist/styles';

import { WEB_ROOT } from '../../../config';

const SliderExampleSimple = [
    "import React from 'react';",
    "import { GridList, Slider, InputNumberSlider, InputNumberSliderGroup, Paper } from 'zele-react';",
    "",
    "export default () => {",
    "   <div>",
    "        <Paper style={{padding: 10, border: '1px solid #e9e9e9'}}><GridList>",
    "            <Slider default={0.5} min={0} max={1}/>",
    "            <Slider default={5} min={0} max={100} type='INT'/>",
    "        </GridList></Paper>",
    "        <Paper style={{padding: 10, border: '1px solid #e9e9e9'}}><GridList>",
    "            <InputNumberSlider defaultValue={0.5} min={0} max={1}/>",
    "            <InputNumberSlider defaultValue={5} min={0} max={100} type='INT'/>",
    "        </GridList></Paper>",
    "        <Paper style={{padding: 10, border: '1px solid #e9e9e9'}}><GridList>    ",
    "            <InputNumberSliderGroup defaults={[0.5, 0.5, 0.3]} min={0} max={1} title='浮点数'/>",
    "            <InputNumberSliderGroup defaults={[10, 20, 30]} min={0} max={100} type='INT' lock={true} title='整数'/>",
    "        </GridList></Paper>",
    "   </div>",
    "};",
].join('\n');

export default () => {
    return <WorkPage siderSelectedKey='3-2-6' breadcrunbs={['工作', '前端开发', 'React 组件', 'Slider 滑动输入条']}>
        <div><Label content='演示' fontSize={20} height={40} color='#000'/></div>
        <CodeBox title='Slider, InputNumberSlider, InputNumberSliderGroup' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{SliderExampleSimple}</SyntaxHighlighter>}>
            <Paper style={{padding: 10, border: '1px solid #e9e9e9'}}><GridList>
                <Slider default={0.5} min={0} max={1}/>
                <Slider default={5} min={0} max={100} type='INT'/>
            </GridList></Paper>
            <Paper style={{padding: 10, border: '1px solid #e9e9e9'}}><GridList>
                <InputNumberSlider defaultValue={0.5} min={0} max={1}/>
                <InputNumberSlider defaultValue={5} min={0} max={100} type='INT'/>
            </GridList></Paper>
            <Paper style={{padding: 10, border: '1px solid #e9e9e9'}}><GridList>    
                <InputNumberSliderGroup defaults={[0.5, 0.5, 0.3]} min={0} max={1} title='浮点数'/>
                <InputNumberSliderGroup defaults={[10, 20, 30]} min={0} max={100} type='INT' lock={true} title='整数'/>
            </GridList></Paper>
        </CodeBox>
        <div><Label content='API' fontSize={20} height={40} color='#000'/></div>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Slider/`} fileName='Slider.json' title='Slider' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Slider/`} fileName='InputNumberSlider.json' title='InputNumberSlider' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Slider/`} fileName='InputNumberSliderGroup.json' title='InputNumberSliderGroup' titleSize={14}/>
    </WorkPage>
};
