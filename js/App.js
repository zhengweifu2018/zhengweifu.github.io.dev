import React from 'react';
import ReactDOM from 'react-dom';

import { HashRouter, Route, Link } from 'react-router-dom';

import IndexPage from './components/IndexPage';

import WorkPage from './components/Work/WorkPage';

import ResumePage from './components/ResumePage';

import ThreeMakePage from './components/Work/ThreeMakePage';

import ThreeModelToolPage from './components/Work/ThreeModelToolPage';
import ThreeLightingRenderToolPage from './components/Work/ThreeLightingRenderToolPage';
import ThreeBindAnimationToolPage from './components/Work/ThreeBindAnimationToolPage';
import ThreeOtherToolPage from './components/Work/ThreeOtherToolPage';

import MenuPage from './components/Work/React/MenuPage';
import ButtonPage from './components/Work/React/ButtonPage';
import IconPage from './components/Work/React/IconPage';

// engine
import ThreeEngineDVS3DPage from './components/Work/ThreeEngineDVS3DPage';
import ThreeEngineUnity3DPage from './components/Work/ThreeEngineUnity3DPage';
import ThreeEngineUnrealPage from './components/Work/ThreeEngineUnrealPage';

let App = (props) => {
	return <div>
		<Route exact path='/' component={IndexPage} />
		<Route exact path='/resume' component={ResumePage} />
		<Route exact path='/work/threemake' component={ThreeMakePage}/>
		<Route exact path='/work/threemodeltool' component={ThreeModelToolPage}/>
		<Route exact path='/work/threeLRtool' component={ThreeLightingRenderToolPage}/>
		<Route exact path='/work/threeBAtool' component={ThreeBindAnimationToolPage}/>
		<Route exact path='/work/threeothertool' component={ThreeOtherToolPage}/>
		<Route exact path='/work/reactmenu' component={MenuPage}/>
		<Route exact path='/work/reactbutton' component={ButtonPage}/>
		<Route exact path='/work/reacticon' component={IconPage}/>
		<Route exact path='/work/enginedvs3d' component={ThreeEngineDVS3DPage}/>
		<Route exact path='/work/engineunity3d' component={ThreeEngineUnity3DPage}/>
		<Route exact path='/work/engineunreal' component={ThreeEngineUnrealPage}/>
	</div>
}

ReactDOM.render(<HashRouter>
	<App />
</HashRouter>, document.getElementById('app'));