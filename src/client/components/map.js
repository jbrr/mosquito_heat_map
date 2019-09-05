import React from 'react';
import '../styles/map.css';
import 'leaflet_css';
import 'leaflet_marker';
import 'leaflet_marker_2x';
import 'leaflet_marker_shadow';
import 'leaflet'
import { Map, Marker, Popup, TileLayer, GeoJSON } from 'react-leaflet'

class DrawMap extends React.Component {
  constructor() {
    super()
    this.state = {
      lat: null,
      lng: null,
      zoom: 1,
      isLoaded: false,
      error: null,
      geoJson: null
    };
  }

  componentDidMount() {
    fetch('http://127.0.0.1:5000/api/v0/locations')
        .then(res => res.json())
        .then(
            result => {
                this.setState({
                    lat: result.features[0].geometry.coordinates[0],
                    lng: result.features[0].geometry.coordinates[1],
                    geoJson: result,
                    isLoaded: true
                });
            },
            (error) => {
                this.setState({
                    isLoaded: true,
                    error
                })
            }
        )
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
    const position = [this.state.lat, this.state.lng]
    if (error) {
        return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
        return <div>Loading...</div>;
    } else {
        return (
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
            );
        }
    }
}

export default DrawMap;
