import React, { Component } from 'react';

const asyncComponent = loadComponent => (
    class AsyncComponent extends Component {
        state = {
            Component: null,
        }

        componentWillMount() {
            if (this.hasLoadedComponent()) {
                return;
            }

            loadComponent()
                .then(module => module.default)
                .then((Component) => {
                    this.setState({ Component });
                })
                .catch((err) => {
                    console.error(`Cannot load component in <AsyncComponent />`);
                    throw err;
                });
        }

        hasLoadedComponent() {
            return this.state.Component !== null;
        }

        render() {
            const { Component } = this.state;
            return (Component) ? <Component {...this.props} /> : null;
        }
    }
);

export default [
	{
        exact: true, 
        path: '/', 
        component: asyncComponent(() => import('./Components/Work/React/LabelPage'))
    },
	{
        exact: true, 
        path: '/resume', 
        component: asyncComponent(() => import('./Components/ResumePage'))
    },
	{
        exact: true, 
        path: '/work/threemake', 
        component: asyncComponent(() => import('./Components/Work/ThreeMakePage'))
    },
	{
        exact: true, 
        path: '/work/threemodeltool', 
        component: asyncComponent(() => import('./Components/Work/ThreeModelToolPage'))
    },
	{
        exact: true, 
        path: '/work/threeLRtool', 
        component: asyncComponent(() => import('./Components/Work/ThreeLightingRenderToolPage'))
    },
	{
        exact: true, 
        path: '/work/threeBAtool', 
        component: asyncComponent(() => import('./Components/Work/ThreeBindAnimationToolPage'))
    },
	{
        exact: true, 
        path: '/work/threeothertool', 
        component: asyncComponent(() => import('./Components/Work/ThreeOtherToolPage'))
    },
	{
        exact: true, 
        path: '/work/webgl', 
        component: asyncComponent(() => import('./Components/Work/WebGLPage'))
    },
	{
        exact: true, 
        path: '/work/reactmenu', 
        component: asyncComponent(() => import('./Components/Work/React/MenuPage'))
    },
	{
        exact: true, 
        path: '/work/reactbutton', 
        component: asyncComponent(() => import('./Components/Work/React/ButtonPage'))
    },
	{
        exact: true, 
        path: '/work/reacticon', 
        component: asyncComponent(() => import('./Components/Work/React/IconPage'))
    },
	{
        exact: true, 
        path: '/work/reactgrid', 
        component: asyncComponent(() => import('./Components/Work/React/GridPage'))
    },
	{
        exact: true, 
        path: '/work/reactinput', 
        component: asyncComponent(() => import('./Components/Work/React/InputPage'))
    },
	{
        exact: true, 
        path: '/work/reactslider', 
        component: asyncComponent(() => import('./Components/Work/React/SliderPage'))
    },
	{
        exact: true, 
        path: '/work/reactlabel', 
        component: asyncComponent(() => import('./Components/Work/React/LabelPage'))
    },
	{
        exact: true, 
        path: '/work/php', 
        component: asyncComponent(() => import('./Components/Work/PhpPage'))
    },
	{
        exact: true, 
        path: '/work/enginedvs3d', 
        component: asyncComponent(() => import('./Components/Work/ThreeEngineDVS3DPage'))
    },
	{
        exact: true, 
        path: '/work/engineunity3d', 
        component: asyncComponent(() => import('./Components/Work/ThreeEngineUnity3DPage'))
    },
	{
        exact: true, 
        path: '/work/engineunreal', 
        component: asyncComponent(() => import('./Components/Work/ThreeEngineUnrealPage'))
    },
    {
        exact: true, 
        path: '/work/enginedesigncloud', 
        component: asyncComponent(() => import('./Components/Work/ThreeEngineDecoDesignPage'))
    },
	{
        exact: true, 
        path: '/work/ai', 
        component: asyncComponent(() => import('./Components/Work/AIPage'))
    }
];