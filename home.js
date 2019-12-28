const React = require('react');
const ReactDOM = require('react-dom'); 

class HomeScreen extends React.Component {
    render() {
        return(
            <h1>This is a test!</h1>
        );
    }
}

ReactDOM.render(<HomeScreen />, document.getElementById("root"));