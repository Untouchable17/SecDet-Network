import React, { useState } from 'react';
import { Navigate } from 'react-router-dom';
import { connect } from 'react-redux';

import { verify } from '../../actions/Auth';


const Activate = ({ verify, match }) => {

    const [verified, setVerified] = useState(false);

    const verify_account = e => {

        const uid = match.params.uid;
        const token = match.params.token;

        verify(uid, token);
        setVerified(true);

    };

    if (verified) {
        return <Navigate to='/' />
    }

    return (
        <div className='container mt-5'>
            <div>
                <h1>Активируйте свой аккаунт</h1>
                <button onClick={verify_account}>Verify</button>
            </div>
        </div>
    )
};

export default connect(null, { verify }) (Activate);