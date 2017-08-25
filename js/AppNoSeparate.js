// 不分离各个页面代码

import React from 'react';
import ReactDOM from 'react-dom';

import { HashRouter, Route } from 'react-router-dom';

import IndexPage from './components/IndexPage';

import ResumePage from './components/ResumePage';

import ThreeMakePage from './components/Work/ThreeMakePage';

import ThreeModelToolPage from './components/Work/ThreeModelToolPage';
import ThreeLightingRenderToolPage from './components/Work/ThreeLightingRenderToolPage';
import ThreeBindAnimationToolPage from './components/Work/ThreeBindAnimationToolPage';
import ThreeOtherToolPage from './components/Work/ThreeOtherToolPage';


// web
import WebGLPage from './components/Work/WebGLPage';

import MenuPage from './components/Work/React/MenuPage';
import ButtonPage from './components/Work/React/ButtonPage';
import IconPage from './components/Work/React/IconPage';
import GridPage from './components/Work/React/GridPage';
import InputPage from './components/Work/React/InputPage';
import SliderPage from './components/Work/React/SliderPage';
import LabelPage from './components/Work/React/LabelPage';

// server
import PhpPage from './components/Work/PhpPage';

// engine
import ThreeEngineDVS3DPage from './components/Work/ThreeEngineDVS3DPage';
import ThreeEngineUnity3DPage from './components/Work/ThreeEngineUnity3DPage';
import ThreeEngineUnrealPage from './components/Work/ThreeEngineUnrealPage';

//
import AIPage from './components/Work/AIPage';

let App = (props) => {
	return <div>
		<Route exact path='/' component={ThreeMakePage} />
		<Route exact path='/resume' component={ResumePage} />
		<Route exact path='/work/threemake' component={ThreeMakePage}/>
		<Route exact path='/work/threemodeltool' component={ThreeModelToolPage}/>
		<Route exact path='/work/threeLRtool' component={ThreeLightingRenderToolPage}/>
		<Route exact path='/work/threeBAtool' component={ThreeBindAnimationToolPage}/>
		<Route exact path='/work/threeothertool' component={ThreeOtherToolPage}/>
		<Route exact path='/work/webgl' component={WebGLPage}/>
		<Route exact path='/work/reactmenu' component={MenuPage}/>
		<Route exact path='/work/reactbutton' component={ButtonPage}/>
		<Route exact path='/work/reacticon' component={IconPage}/>
		<Route exact path='/work/reactgrid' component={GridPage}/>
		<Route exact path='/work/reactinput' component={InputPage}/>
		<Route exact path='/work/reactslider' component={SliderPage}/>
		<Route exact path='/work/reactlabel' component={LabelPage}/>
		<Route exact path='/work/php' component={PhpPage}/>
		<Route exact path='/work/enginedvs3d' component={ThreeEngineDVS3DPage}/>
		<Route exact path='/work/engineunity3d' component={ThreeEngineUnity3DPage}/>
		<Route exact path='/work/engineunreal' component={ThreeEngineUnrealPage}/>
		<Route exact path='/work/ai' component={AIPage}/>
	</div>
}


ReactDOM.render(<HashRouter>
	<App />
</HashRouter>, document.getElementById('app'));