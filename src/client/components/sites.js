import GeoJSON from 'react-leaflet';

function Sites(url) {
    fetch(url)
        .then(res => res.json())
        .then(result => {
            result = JSON.parse(result)
            return {
                isLoaded: true,
                geoJSON: result
            }
        },
        (error) => {
            return {
                isLoaded: true,
                error
            }
        }
    )
}