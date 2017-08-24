import React, { Component } from 'react';

import WorkPage from '../WorkPage';

import CodeBox from '../../CodeBox';

import { Menu, SubMenu, MenuItem, MenuItemGroup, Icon, GridList, Label } from 'zele-react';

import ApiTable from './ApiTable';

import { WEB_ROOT } from '../../../config';

const MenuExampleHDark = [
    "import React from 'react';",
    "import { Menu, SubMenu, MenuItem, MenuItemGroup, Icon } from 'zele-react';",
    "",
    "const MenuExampleHDark = () => {",
    "    <Menu theme='dark'>",
    "        <MenuItem icon={<Icon type='gImage' />}/>",
    "        <SubMenu icon={<Icon type='gBrush' />}>",
    "           <MenuItem />",
    "           <MenuItemGroup icon={<Icon type='gTransform' />}>",
    "               <MenuItem /> ",
    "            </MenuItemGroup>",
    "           <MenuItem />  ",
    "        </SubMenu>",
    "        <MenuItem />",
    "        <SubMenu>",
    "           <MenuItem />",
    "           <MenuItem />  ",
    "        </SubMenu>",
    "    </Menu>",
    "};",
    "",
    "export default MenuExampleHDark;"
].join('\n');

const MenuExampleHLight = [
    "import React from 'react';",
    "import { Menu, SubMenu, MenuItem, MenuItemGroup, Icon } from 'zele-react';",
    "",
    "const MenuExampleHLight = () => {",
    "   <Menu theme='light'>",
    "       <MenuItem icon={<Icon type='gImage' />}/>",
    "       <SubMenu icon={<Icon type='gBrush' />}>",
    "          <MenuItem />",
    "          <MenuItemGroup icon={<Icon type='gTransform' />}>",
    "              <MenuItem /> ",
    "           </MenuItemGroup>",
    "          <MenuItem />  ",
    "       </SubMenu>",
    "       <MenuItem />",
    "       <SubMenu>",
    "          <MenuItem />",
    "          <MenuItem />  ",
    "       </SubMenu>",
    "   </Menu>",
    "};",
    "",
    "export default MenuExampleHLight;"
].join('\n');


const MenuExampleVDark = [
    "import React from 'react';",
    "import { Menu, SubMenu, MenuItem, MenuItemGroup, Icon } from 'zele-react';",
    "",
    "const MenuExampleVDark = () => {",
    "    <Menu mode='vertical'>",
    "        <MenuItem />",
    "        <SubMenu open={true}>",
    "           <MenuItem />",
    "           <MenuItem />  ",
    "        </SubMenu>",
    "        <MenuItem icon={<Icon type='gImage' />}/>",
    "        <SubMenu open={true}>",
    "            <MenuItem />",
    "            <SubMenu open={true}>",
    "               <MenuItem />",
    "               <MenuItem />  ",
    "            </SubMenu>",
    "            <MenuItemGroup icon={<Icon type='gTransform' />}>",
    "                <MenuItem />",
    "                <MenuItem />  ",
    "            </MenuItemGroup>",
    "          <MenuItem />  ",
    "        </SubMenu>",
    "    </Menu>",
    "};",
    "",
    "export default MenuExampleVDark;"
].join('\n');

const MenuExampleVLight = [
    "import React from 'react';",
    "import { Menu, SubMenu, MenuItem, MenuItemGroup, Icon } from 'zele-react';",
    "",
    "const MenuExampleVLight = () => {",
    "    <Menu mode='vertical' theme='light'>",
    "        <MenuItem />",
    "        <SubMenu open={true}>",
    "           <MenuItem />",
    "           <MenuItem />  ",
    "        </SubMenu>",
    "        <MenuItem icon={<Icon type='gImage' />}/>",
    "        <SubMenu open={true}>",
    "            <MenuItem />",
    "            <SubMenu open={true}>",
    "               <MenuItem />",
    "               <MenuItem />  ",
    "            </SubMenu>",
    "            <MenuItemGroup icon={<Icon type='gTransform' />}>",
    "                <MenuItem />",
    "                <MenuItem />  ",
    "            </MenuItemGroup>",
    "          <MenuItem />  ",
    "        </SubMenu>",
    "    </Menu>",
    "};",
    "",
    "export default MenuExampleVLight;"
].join('\n');

import SyntaxHighlighter from 'react-syntax-highlighter';
import { xcode } from 'react-syntax-highlighter/dist/styles';

export default () => {
    return <WorkPage siderSelectedKey='3-2-1' breadcrunbs={['工作', '前端开发', 'React 组件', 'Menu 菜单']}>
        <div><Label content='演示' fontSize={20} height={40} color='#000'/></div>
        <CodeBox title='顶栏黑色' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{MenuExampleVDark}</SyntaxHighlighter>}>
            <Menu theme='dark'>
                <MenuItem icon={<Icon type='gImage' />}/>
                <SubMenu icon={<Icon type='gBrush' />}>
                   <MenuItem />
                   <MenuItemGroup icon={<Icon type='gTransform' />}>
                       <MenuItem /> 
                    </MenuItemGroup>
                   <MenuItem />  
                </SubMenu>
                <MenuItem />
                <SubMenu>
                   <MenuItem />
                   <MenuItem />  
                </SubMenu>
            </Menu>
        </CodeBox>
        <CodeBox title='顶栏亮色' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{MenuExampleHLight}</SyntaxHighlighter>}>
            <Menu theme='light'>
                <MenuItem icon={<Icon type='gImage' />}/>
                <SubMenu icon={<Icon type='gBrush' />}>
                   <MenuItem />
                   <MenuItemGroup icon={<Icon type='gTransform' />}>
                       <MenuItem /> 
                    </MenuItemGroup>
                   <MenuItem />  
                </SubMenu>
                <MenuItem />
                <SubMenu>
                   <MenuItem />
                   <MenuItem />  
                </SubMenu>
            </Menu>
        </CodeBox>
        <GridList>
            <CodeBox title='侧栏黑色' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{MenuExampleVLight}</SyntaxHighlighter>}>
                <Menu mode='vertical'>
                    <MenuItem />
                    <SubMenu open={true}>
                       <MenuItem />
                       <MenuItem />  
                    </SubMenu>
                    <MenuItem icon={<Icon type='gImage' />}/>
                    <SubMenu open={true}>
                        <MenuItem />
                        <SubMenu open={true}>
                           <MenuItem />
                           <MenuItem />  
                        </SubMenu>
                        <MenuItemGroup icon={<Icon type='gTransform' />}>
                            <MenuItem />
                            <MenuItem />  
                        </MenuItemGroup>
                      <MenuItem />  
                    </SubMenu>
                </Menu>
            </CodeBox>
            <CodeBox title='侧栏亮色' codeComponent={<SyntaxHighlighter language='jsx' style={xcode}>{MenuExampleVLight}</SyntaxHighlighter>}>
                <Menu mode='vertical' theme='light'>
                    <MenuItem />
                    <SubMenu open={true}>
                       <MenuItem />
                       <MenuItem />  
                    </SubMenu>
                    <MenuItem icon={<Icon type='gImage' />}/>
                    <SubMenu open={true}>
                        <MenuItem />
                        <SubMenu open={true}>
                           <MenuItem />
                           <MenuItem />  
                        </SubMenu>
                        <MenuItemGroup icon={<Icon type='gTransform' />}>
                            <MenuItem />
                            <MenuItem />  
                        </MenuItemGroup>
                      <MenuItem />  
                    </SubMenu>
                </Menu>
            </CodeBox>
        </GridList>
        <div><Label content='API' fontSize={20} height={40} color='#000'/></div>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Menu/`} fileName='Menu.json' title='Menu' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Menu/`} fileName='SubMenu.json' title='SubMenu' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Menu/`} fileName='MenuItemGroup.json' title='MenuItemGroup' titleSize={14}/>
        <ApiTable pathName={`${WEB_ROOT}assets/reactComponentApiTable/Menu/`} fileName='MenuItem.json' title='MenuItem' titleSize={14}/>
    </WorkPage>
};