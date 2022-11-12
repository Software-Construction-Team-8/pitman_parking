import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
//component imports
import Home from './components/Home';
//import ParkingSpots from './components/Parking_Spots';

require('react-dom');
window.React2 = require('react');
console.log(window.React1 === window.React2);

function App(){
    return(
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />}></Route>
            </Routes>
        </Router>
    )
}

export default App;