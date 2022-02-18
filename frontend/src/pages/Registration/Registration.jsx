import { Link, Navigate } from 'react-router-dom';
import React, { useState } from 'react';
import { connect } from 'react-redux';

import { signup } from '../../actions/Auth';


const SignUp = ({ signup, isAuthenticated }) => {

    const [accountCreated, setAccountCreated] = useState(false);

    const [formData, setFormData] = useState({
        name: "",
        email: "",
        password: "",
        re_password: ""
    });

    const { name, email, password, re_password } = formData;

    const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

    const onSubmit = e => {

        e.preventDefault();

        if (password === re_password){
            signup(name, email, password, re_password);
            setAccountCreated(true);
        }

    };

    if (isAuthenticated) {
        return <Navigate to='/' />
    }

    if (accountCreated) {
        return <Navigate to='/login' />
    }

    return (
        <div className='container mt-5'>
            <h1>Sign Up</h1>
            <p>Sign Up your account</p>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group'>
                    <input
                        required
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='name'
                        type='text'
                        value={name}
                        placeholder='Введите никнейм'
                    />
                </div>
                <div className='form-group'>
                    <input
                        required
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='email'
                        type='email'
                        value={email}
                        placeholder='Укажите почту'
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
                        placeholder='Создайте пароль'
                    />
                </div>
                <div className='form-group'>
                    <input
                        required
                        minLength='5'
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='re_password'
                        type='password'
                        value={password}
                        placeholder='Повторите пароль'
                    />
                </div>
                <button className='btn btn-primary' type='submit'>Зарегистрироваться</button>
            </form>
            <p className='mt-3'>
                Уже зарегистрированы? <Link to="/login">Войти</Link>
            </p>

        </div>
    )
};


const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { signup     }) (SignUp);