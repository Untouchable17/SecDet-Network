import { Navigate } from 'react-router-dom';
import React, { useState } from 'react';
import { connect } from 'react-redux';

import { reset_password } from '../../actions/Auth';


const ResetPassword = ({ reset_password }) => {

    const [requestSent, setRequestSent] = useState(false);

    const [formData, setFormData] = useState({
        email: "",
    });

    const { email } = formData;

    const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

    const onSubmit = e => {

        e.preventDefault();
        reset_password(email);
        setRequestSent(true);
    };

    if (requestSent) {
        return <Navigate to='/' />
    }

    return (
        <div className='container mt-5'>
            <h1>Reset Password</h1>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group'>
                    <input
                        required
                        onChange={e => onChange(e)}
                        className='form-control'
                        name='email'
                        type='email'
                        value={email}
                        placeholder='email'
                    />
                </div>

                <button className='btn btn-primary' type='submit'>Сменить пароль</button>
            </form>

        </div>
    )
};


export default connect(null, { reset_password }) (ResetPassword);