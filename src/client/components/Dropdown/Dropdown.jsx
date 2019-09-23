import React from 'react';
import PropTypes from 'prop-types';
import FontAwesome from 'react-fontawesome';
import './styles';

class Dropdown extends React.Component {
  constructor(props) {
    super(props);
    this.close = this.close.bind(this);
    this.toggleList = this.toggleList.bind(this);
    this.state = {
      open: false,
      title: this.props.title
    };
  }

  componentDidUpdate(prevProps) {
    if (this.props.title && prevProps.title != this.props.title) {
      this.setState({
        title: this.props.title
      });
    }
    const open = this.state.open;
    setTimeout(() => {
      if (open) {
        window.addEventListener('click', this.close);
      }
      else{
        window.removeEventListener('click', this.close);
      }
    }, 0);
  }

  componentWillUnmount(){
    window.removeEventListener('click', this.close)
  }

  toggleList() {
    this.setState(prevState => ({
      open: !prevState.open
    }));
  }

  close(timeOut){
    this.setState({
      open: false
    });
  }

  render() {
    const list = this.props.list;
    const handleClick = this.props.handleClick;
    const listOpen = this.state.open;
    const headerTitle = this.state.title;

    return(
      <div className='dd-wrapper'>
        <div className="dd-header" onClick={() => this.toggleList()}>
          <div className='dd-header-title'>{headerTitle}</div>
          {listOpen
            ? <FontAwesome name='angle-up' size='2x'/>
            : <FontAwesome name='angle-down' size='2x'/>
          }
        </div>
        {listOpen && 
          <ul className='dd-list'>
            {list.map((item) => (
             <li 
                className='dd-list-item'
                key={item.name}
                onClick={ () =>
                  handleClick(item)
              }>
                {item.name} {item.selected && <FontAwesome name='check'/>}
              </li>
            ))}
          </ul>
        }
      </div>
    )
  }
}

Dropdown.propTypes = {
  handleClick: PropTypes.func,
  list: PropTypes.array,
  title: PropTypes.string
}

export default Dropdown;