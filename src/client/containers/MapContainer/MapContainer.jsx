import React from 'react';
import { Transition, TransitionGroup } from 'react-transition-group';
import PropTypes from 'prop-types';
import './styles.css';
import 'leaflet_css';
import 'leaflet_marker';
import 'leaflet_marker_2x';
import 'leaflet_marker_shadow';
import 'leaflet'
import { Map, Marker, Popup, TileLayer, GeoJSON } from 'react-leaflet'
import { getSubsiteLocations } from '../../utils/Apis';
import GeneraLayer from '../../components/GeneraLayer';
import Loader from '../../components/Loader';

class MapContainer extends React.Component {
  constructor(props) {
    super(props);
    this.displayMap = this.displayMap.bind(this);
    this.renderGeneraLayers = this.renderGeneraLayers.bind(this);
    this.state = {
      zoom: 6,
      isLoaded: false,
      error: null,
      locationGeoJson: null,
      generaLayers: []
    };
  }

  componentDidMount() {
    getSubsiteLocations()
    .then(result => {
      this.setState({
        locationGeoJson: result.data,
        isLoaded: true
      });
    })
    .catch(error => {
      this.setState({
        isLoaded: true,
        error
      });
    });
  }

  componentDidUpdate(prevProps) {
    if (this.props.layers && prevProps.layers != this.props.layers) {
      var newGeneraLayers = this.props.layers.filter(layer => layer.layer === 'genera');
      this.setState({
        generaLayers: newGeneraLayers
      });
    }
  }

  renderGeneraLayers() {
    if (this.state.generaLayers.length > 0) {
      return this.state.generaLayers.map((layer) => (
        <GeneraLayer key={layer.item.name} layer={layer} />
      ));
    }
  }

  onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.name) {
      layer.bindPopup(feature.properties.name);
    }
  }

  getStyle(feature, layer) {
    return {
      color: '#006400',
      weight: 5,
      opacity: 0.65
    }
  }

  //TODO: This should be it's own component
  displayMap() {
    // Middle of the United States
    const position = [39.8283, -98.5795]
    const generaLayers = this.renderGeneraLayers();
    console.log(generaLayers)
    if (this.state.error) {
      return <div>Error: {this.state.error.message}</div>;
    } else {
      return (
        <div id="map">
          <Map ref='map' center={position} zoom={this.state.zoom}>
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url='https://{s}.tile.osm.org/{z}/{x}/{y}.png'
            />
            { generaLayers }
          </Map>
        </div>
      );
    }
  }

  render() {
    const isLoaded = this.state.isLoaded;
    const display = this.state.isLoaded ? ['map', this.displayMap()] : ['loader', <Loader />];
    return (
      <TransitionGroup className='this-ol-map'>
        <Transition key={ display[0] } in={ isLoaded } timeout={ 350 }>
          { display[1] }
        </Transition>
      </TransitionGroup>
    );
  }
}

MapContainer.propTypes = {
  layers: PropTypes.array
}

export default MapContainer;
