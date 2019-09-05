import GeoJSON from 'react-leaflet';

function Site(props) {
    return (
        <GeoJSON
            key={props.properties.name}
            data={props}
        />
    )
}