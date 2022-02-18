import { Navigate } from 'react-router-dom';
import React, { useState } from 'react';
import { connect } from 'react-redux';

import { reset_password_confirm } from '../../actions/Auth';


const ResetPasswordConfirm = ({ match, reset_password_confirm }) => {

    const [requestSent, setRequestSent] = useState(false);

    const [formData, setFormData] = useState({
        new_password: "",
        re_new_password: ""
    });

    const { new_password, re_new_password } = formData;

    const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

    const onSubmit = e => {

        e.preventDefault();

        const uid = match.params.uid;
        const token = match.params.token;

        reset_password_confirm(uid, token, new_password, re_new_password);
        setRequestSent(true);
    };

    if (requestSent) {
        return <Navigate to='/' />
    }

    return (
        <div className='container mt-5'>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group'>
                    <input
                        required
                        minLength='5'
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='new_password'
                        type='password'
                        value={new_password}
                        placeholder='Новый пароль..'
                    />
                </div>
                <div className='form-group'>
                    <input
                        required
                        minLength='5'
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='re_new_password'
                        type='password'
                        value={re_new_password}
                        placeholder='Подтвердите новый пароль'
                    />
                </div>

                <button className='btn btn-primary' type='submit'>Сменить пароль</button>
            </form>

        </div>
    )
};


export default connect(null, { reset_password_confirm }) (ResetPasswordConfirm);