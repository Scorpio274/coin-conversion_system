// import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';
import Home from './components/Home';
import History from './components/History';
import SetAlert from './components/SetAlert';
import Login from './components/Login';
import Signup from './components/Signup';
import Footer from './components/Footer';

const App = () => {
    return (
        <Router>
            <div>
            {/* <div class="absolute  inset-0 -z-10 h-full w-full bg-violet-950 [background:radial-gradient(125%_125%_at_50%_10%,#fff_40%,#63e_100%)]">
            </div> */}
                <Navbar /><br /><br />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/history" element={<History />} />
                    <Route path="/set-alert" element={<SetAlert />} />
                    <Route path="/login" element={<Login />} />
                    
                    <Route path='/signup' element={<Signup/>}/>
                </Routes>
                <Footer/>
            </div>
        </Router>
    );
};

export default App;
