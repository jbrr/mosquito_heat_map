import React from 'react';
import './styles.css';
import 'leaflet_css';
import 'leaflet_marker';
import 'leaflet_marker_2x';
import 'leaflet_marker_shadow';
import 'leaflet'
import { Map, Marker, Popup, TileLayer, GeoJSON } from 'react-leaflet'
import { getSubsiteLocations } from '../../utils/Apis';

class MapContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      zoom: 5,
      isLoaded: false,
      error: null,
      geoJson: null
    };
  }

  componentDidMount() {
    getSubsiteLocations()
    .then(result => {
      this.setState({
        geoJson: result.data,
        isLoaded: true
      });
    })
    .catch(error => {
      this.setState({
        isLoaded: true,
        error
      })
    })
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

  render() {
    const isLoaded = this.state.isLoaded
    const error = this.state.error
    // Middle of the United States
    const position = [39.8283, -98.5795]
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div className="col-9" id="map">
          <Map center={position} zoom={this.state.zoom}>
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url='https://{s}.tile.osm.org/{z}/{x}/{y}.png'
            />
            <GeoJSON
              data={this.state.geoJson}
              onEachFeature={this.onEachFeature}
              style={this.getStyle}
            />
          </Map>
        </div>
      );
    }
  }
}

export default MapContainer;
