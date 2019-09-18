import React from 'react';
import { Transition, TransitionGroup } from 'react-transition-group';
import MapContainer from '../MapContainer';
import LeaderboardContainer from '../LeaderboardContainer';
import SidebarContainer from '../SidebarContainer';
import './styles';

class MainContainer extends React.Component {
  constructor(props) {
    super(props);
    this.handleToggleMapLeaderboard = this.handleToggleMapLeaderboard.bind(this);
    this.defaultStyle = this.defaultStyle.bind(this);
    this.transitionStyles = this.transitionStyles.bind(this);
    this.state = {
      showMap: true
    };
  }

  handleToggleMapLeaderboard() {
    var showMap = !this.state.showMap;
    this.setState({ showMap: showMap });
  }

  defaultStyle() {
    return ({
      transition: `opacity 300ms ease-in-out`,
      opacity: 0,
    })
  }

  transitionStyles() {
    return ({
      entering: { opacity: 1 },
      entered:  { opacity: 1 },
      exiting:  { opacity: 0 },
      exited:  { opacity: 0 },
    })
  };

  render() {
    var displayMapOrLeaderboard = this.state.showMap ? ['map', <MapContainer />] : ['leaderboard', <LeaderboardContainer />];
    var showMap = this.state.showMap
    return(
      <div className='row no-gutters'>
        <TransitionGroup className='col-9 main'>
          <Transition key={ displayMapOrLeaderboard[0] } in={ showMap } timeout={350}>
            {state => (
              <div style={{
                ...this.defaultStyle(),
                ...this.transitionStyles()[state]
              }}>
                 { displayMapOrLeaderboard[1] }
              </div>
            )}
          </Transition>
        </TransitionGroup>
        <SidebarContainer
          toggleMapAndLeaderboard={this.handleToggleMapLeaderboard}
        />
      </div>
    )
  }
}

export default MainContainer;