import {
    LOGIN_ROUTE,
    PROFILE_ROUTE,
    REGISTRATION_ROUTE,
    RESET_PASSWORD_ROUTE,
    RESET_PASSWORD_CONFIRM_ROUTE,
    ACTIVATE_ROUTE
} from './utils/consts';

import ResetPasswordConfirm from './pages/ResetPasswordConfirm/ResetPasswordConfirm';
import ResetPassword from './pages/ResetPassword/ResetPassword';
import Registration from './pages/Registration/Registration';
import Activate from './pages/Activate/Activate';
import Profile from './pages/Profile/Profile';
import Login from './pages/Login/Login';

// Урлы, доступ к которым есть только у авторизованных пользователей
export const authRoutes = [
    {
        path: PROFILE_ROUTE,
        Component: Profile
    },

]

// Урлы, доступ к которым есть у всех пользователей
export const publicRoutes = [
    {
        path: LOGIN_ROUTE,
        Component: Login
    },
    {
        path: REGISTRATION_ROUTE,
        Component: Registration
    },
    {
        path: RESET_PASSWORD_ROUTE,
        Component: ResetPassword
    },
    {
        path: RESET_PASSWORD_CONFIRM_ROUTE + '/:uid/:token',
        Component: ResetPasswordConfirm
    },
    {
        path: ACTIVATE_ROUTE + '/:uid/:token',
        Component: Activate,
    },
]