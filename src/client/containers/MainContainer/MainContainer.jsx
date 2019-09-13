import React from 'react';
import MapContainer from '../MapContainer';
import LeaderboardContainer from '../LeaderboardContainer';
import SidebarContainer from '../SidebarContainer';

class MainContainer extends React.Component {
  constructor(props) {
    super(props)
    this.handleToggleMapLeaderboard = this.handleToggleMapLeaderboard.bind(this);
    this.state = {
      showMap: true
    };
  }

  handleToggleMapLeaderboard() {
    var showMap = !this.state.showMap;
    this.setState({ showMap: showMap });
  }

  render() {
    var displayMapOrLeaderboard = this.state.showMap ? <MapContainer /> : <LeaderboardContainer />;
    return(
      <div className='row no-gutters'>
        {displayMapOrLeaderboard}
        <SidebarContainer
          toggleMapAndLeaderboard={this.handleToggleMapLeaderboard}
        />
      </div>
    )
  }
}

export default MainContainer;