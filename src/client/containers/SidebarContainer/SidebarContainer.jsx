import React from 'react';
import PropTypes from 'prop-types';
import Checkbox from '../../components/Checkbox'

class SidebarContainer extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return(
      <div className='col-3' id='sidebar'>
        <Checkbox 
          checkedValue = "Map"
          uncheckedValue = "Leaderboard"
          clickHandler = { this.props.toggleMapAndLeaderboard }
        />
      </div>
    );
  }
}

SidebarContainer.propTypes = {
  toggleMapAndLeaderboard: PropTypes.func
}

export default SidebarContainer;