import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import { checkAuthenticated, load_user } from '../actions/Auth';
import Navbar from '../components/Navbar/Navbar';

const Layout = (props) => {

    useEffect(() => {

        props.checkAuthenticated();
        props.load_user();

    }, []);

    return (
        <div className="Layout">
            <Navbar />
            {props.children}
        </div>
    );
};


export default connect(null, { checkAuthenticated, load_user }) (Layout);