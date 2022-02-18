import React, {createContext} from 'react';
import { Provider } from "react-redux";
import ReactDOM from 'react-dom';
import {
    BrowserRouter,
    Routes,
    Route,
    Redirect
} from 'react-router-dom';

import App from './App';
import store from "./store";
import './index.css';

export const Context = createContext(null)

ReactDOM.render(

    <Provider store={store}>
        <App />
    </Provider>,

    document.getElementById('root')
);
