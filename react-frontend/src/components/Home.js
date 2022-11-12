import React from "react";
import {useNavigate} from "react-router-dom";

require('react-dom');
window.React2 = require('react');
console.log(window.React1 === window.React2);

//css import

//assets imports


function Home(){
    const navigate = useNavigate()
    return(
        <div className="home">
            <h1 className="pm-parking">Pitman Parking</h1>
            <div className="btn">
                <ul>
                    <li>
                        <button onClick={()=>navigate('/parking_spots')} className="prk_btn" type="button"></button>
                    </li>
                </ul>
            </div>
        </div>
    );
}

export default Home;