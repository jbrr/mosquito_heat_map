import React from 'react';
import PropTypes from 'prop-types';
import Checkbox from '../../components/Checkbox';
import Dropdown from '../../components/Dropdown';
import { getGenera } from '../../utils/Apis';
import './styles';

class SidebarContainer extends React.Component {
  constructor(props) {
    super(props)
    this.formatForDropdown = this.formatForDropdown.bind(this);
    this.toggleSelected = this.toggleSelected.bind(this);
    this.handleGenusDropdownClick = this.handleGenusDropdownClick.bind(this);
    this.handleGenusTitle = this.handleGenusTitle.bind(this);
    this.state = {
      isLoaded: false,
      genera: [],
      error: null
    }
  }

  componentDidMount() {
    getGenera()
    .then(result => {
      this.setState({
        isLoaded: true,
        genera: this.formatForDropdown(result.data, 'genera')
      });
    })
    .catch(error => {
      this.setState({
        isLoaded: true,
        error: error
      });
    });
  }

  formatForDropdown(result, key) {
    for (var i = 0; i < result.length; i++) {
      result[i].selected = false;
      result[i].key = key;
    }
    return result;
  }

  toggleSelected(id, key) {
    let temp = this.state[key];
    temp[id].selected = !temp[id].selected;
    this.setState({
      [key]: temp
    });
  }

  handleGenusDropdownClick(item) {
    this.toggleSelected(item.id, item.key);
    this.props.addOrRemoveLayer(item);
  }

  handleGenusTitle() {
    var selectedItems = this.state.genera.filter(item => item.selected);
    console.log(selectedItems)
    if (selectedItems.length === 0) {
      console.log('in length 0')
      return 'Filter by genus';
    } else if (selectedItems.length === 1) {
      console.log('in length 1')
      return selectedItems[0].name;
    } else {
      return 'Displaying ' + selectedItems.length + ' genera';
    }
  }

  render() {
    return(
      <div className='col-3' id='sidebar'>
        <Checkbox 
          checkedValue = 'Map'
          uncheckedValue = 'Leaderboard'
          clickHandler = { this.props.toggleMapAndLeaderboard }
        />
        <Dropdown
          title = { this.handleGenusTitle() }
          list = { this.state.genera }
          handleClick = { this.handleGenusDropdownClick }
        />
      </div>
    );
  }
}

SidebarContainer.propTypes = {
  toggleMapAndLeaderboard: PropTypes.func,
  addOrRemoveLayer: PropTypes.func
}

export default SidebarContainer;