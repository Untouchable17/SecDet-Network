import { Link, Navigate } from 'react-router-dom';
import React, { useState } from 'react';
import { connect } from 'react-redux';

import { login } from '../../actions/Auth';


const Login = ({ login, isAuthenticated }) => {

    const [formData, setFormData] = useState({
        email: "",
        password: ""
    });

    const { email, password } = formData;

    const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

    const onSubmit = e => {

        e.preventDefault();
        login(email, password);

    };

    if (isAuthenticated) {
        return <Navigate to='/' />
    }

    return (
        <div className='container mt-5'>
            <h1>Войти в аккаунт</h1>
            <p>Форма для авторизации входа на аккаунт</p>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group'>
                    <input
                        required
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='email'
                        type='email'
                        value={email}
                        placeholder='Почта'
                    />
                </div>
                <div className='form-group'>
                    <input
                        required
                        minLength='5'
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='password'
                        type='password'
                        value={password}
                        placeholder='Пароль'
                    />
                </div>
                <button className='btn btn-primary' type='submit'>Войти</button>
            </form>
            <p className='mt-3'>
                Еще не зарегистрированы? <Link to="/signup">Создать аккаунт</Link>
            </p>
            <p className='mt-3'>
                Забыли пароль? <Link to="/reset-password">Восстановить пароль</Link>
            </p>
        </div>
    )
};


const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { login }) (Login);