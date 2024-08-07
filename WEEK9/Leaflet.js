let map;
let featureGroup;

function initMap() {
    map = L.map('map').setView([12.5657, 104.991], 7);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    featureGroup = L.featureGroup().addTo(map);
}

function startMST() {
    fetch('/start_mst')
        .then(response => response.json())
        .then(data => updateMap(data));
}

function nextStep() {
    fetch('/mst_step')
        .then(response => response.json())
        .then(data => updateMap(data));
}

function updateMap(data) {
    if (data.finished) {
        alert('MST algorithm completed!');
        return;
    }
    featureGroup.clearLayers();
    L.geoJSON(data.features, {
        style: function(feature) {
            return {color: feature.properties.color, weight: 3, opacity: 0.7};
        }
    }).addTo(featureGroup);
}

document.addEventListener('DOMContentLoaded', initMap);
