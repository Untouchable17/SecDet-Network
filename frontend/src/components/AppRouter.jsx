import React, { useContext } from 'react';
import {
    Navigate,
    Routes,
    Route
} from 'react-router-dom';

import {publicRoutes, authRoutes} from "../routes";
import { Context } from '../index';
import consts from '../utils/consts';


const AppRouter = () => {

    const isAuth = false;

    return (
        <div>
            <Routes>
                {isAuth && authRoutes.map(({path, Component}) =>
                    <Route key={path} path={path} element={<Component />} exact/>
                )}
                {publicRoutes.map(({path, Component}) =>
                    <Route key={path} path={path} element={<Component />} exact/>
                )}
            </Routes>
        </div>
    );
};

export default AppRouter;