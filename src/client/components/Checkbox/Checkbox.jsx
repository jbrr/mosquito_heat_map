import React from 'react';
import PropTypes from 'prop-types';
import './styles';

class Checkbox extends React.Component {
  constructor(props) {
    super(props)
    this.handleChange = this.handleChange.bind(this);
    this.decideValue = this.decideValue.bind(this);
    this.state = {
      checked: false,
      labelValue: this.props.uncheckedValue
    };
  }

  decideValue(checked) {
    if (checked) {
      return this.props.checkedValue;
    } else {
      return this.props.uncheckedValue;
    }
  };

  handleChange() {
    var checked = !this.state.checked;
    var labelValue = this.decideValue(checked);
    this.props.clickHandler();
    this.setState({
      checked: checked,
      labelValue: labelValue });

  };

  render() {
    return (
      <section className="slider-checkbox">
          <input 
            type="checkbox"
            id={this.state.labelValue}
            checked={this.state.checked}
            onChange={this.handleChange}
          />
        <label className="label" htmlFor={this.state.labelValue}>{ this.state.labelValue }</label>
      </section>
    );
  }
}

Checkbox.propTypes = {
  checkedValue: PropTypes.string,
  uncheckedValue: PropTypes.string,
  clickHandler: PropTypes.func
};

export default Checkbox;