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
    this.addOrRemoveLayer = this.addOrRemoveLayer.bind(this);
    this.defaultStyle = this.defaultStyle.bind(this);
    this.transitionStyles = this.transitionStyles.bind(this);
    this.state = {
      showMap: true,
      mapLayers: []
    };
  }

  handleToggleMapLeaderboard() {
    var showMap = !this.state.showMap;
    this.setState({ showMap: showMap });
  }

  addOrRemoveLayer(item) {
    if (item.selected) {
      var layer = {
        layer: item.key,
        item: item
      };
      var joined = this.state.mapLayers.concat(layer);
      this.setState({
        mapLayers: joined
      });
    } else {
      var updatedLayers = this.state.mapLayers.filter(element => (
        element.item.id !== item.id
      ));
      console.log(item)
      console.log(this.state.mapLayers)
      console.log(updatedLayers)
      this.setState({
        mapLayers: updatedLayers
      });
    }
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
    var displayMapOrLeaderboard = this.state.showMap ? ['map', <MapContainer layers={ this.state.mapLayers } />] : ['leaderboard', <LeaderboardContainer />];
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
          addOrRemoveLayer={this.addOrRemoveLayer}
        />
      </div>
    )
  }
}

export default MainContainer;