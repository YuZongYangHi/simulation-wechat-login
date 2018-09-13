import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router,Route,Link,Switch} from 'react-router-dom'
import Login from './commponent/common/login'
import App from './App';

class Home extends React.Component {
    constructor(props) {
        super(props)
    } 

    render() {
        return (
            <div>
                <Router>
                    <Switch>
                        <Route exact path="/login" component={Login}></Route>
                        {/*<Route exact path="/" component={App}></Route>*/}
                    </Switch>
                </Router>
            </div>
        )
    }
}

ReactDOM.render(<Home />, document.getElementById('root'));
