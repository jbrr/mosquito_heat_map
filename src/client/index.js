import React from 'react';
import ReactDOM from 'react-dom';
import MainContainer from './containers/MainContainer';

class AppContainer extends React.Component {
  render() {
    return(
      <div>
        <MainContainer />
      </div>
    )
  }
}

ReactDOM.render(
<AppContainer />,
document.getElementById('app')
)