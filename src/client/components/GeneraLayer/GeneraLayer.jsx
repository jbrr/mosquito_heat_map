import React from 'react';
import PropTypes from 'prop-types';
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import { getGenusDistribution } from '../../utils/Apis';

class GeneraLayer extends React.Component {
  constructor(props) {
    super(props);
    this.formattedLocs = this.formattedLocs.bind(this);
    this.state = {
      isLoaded: false,
      formattedCoords: null,
      error: null
    };
  }

  componentDidMount() {
    getGenusDistribution(this.props.layer.item.name)
    .then(result => {
      this.formattedLocs(result.data);
    })
    .catch(error => {
      this.setState({
        isLoaded: true,
        error: error
      });
    });
  }

  formattedLocs(responseData) {
    var locs = responseData.features.map((data) => {
      var location = data.geometry.coordinates;
      location.push(data.properties.count);
      return location
    });
    this.setState({
      isLoaded: true,
      formattedCoords: locs
    });
  }

  render() {
    if (this.state.isLoaded) {
      const locations = this.state.formattedCoords;
      return (
        <HeatmapLayer
          fitBoundsOnLoad
          fitBoundsOnUpdate
          points={locations}
          longitudeExtractor={m => m[0]}
          latitudeExtractor={m => m[1]}
          intensityExtractor={m => parseFloat(m[2])}
          radius={Number(20)}
          blur={Number(15)}
          max={Number(5)}
        />
      )
    } else {
      return(<div>Loading...</div>)
    }
  }
}

GeneraLayer.propTypes = {
  layer: PropTypes.object
}

export default GeneraLayer;