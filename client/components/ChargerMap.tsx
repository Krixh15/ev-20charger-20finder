import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { useEffect, useState } from "react";

type Charger = {
  ID: number;
  AddressInfo: {
    Latitude: number;
    Longitude: number;
    Title: string;
    Town?: string;
  };
};

export default function ChargerMap() {
  const [chargers, setChargers] = useState<Charger[]>([]);

  useEffect(() => {
    fetch(
      "https://api.openchargemap.io/v3/poi/?output=json&countrycode=IN&maxresults=50"
    )
      .then((res) => res.json())
      .then((data) => setChargers(data))
      .catch(console.error);
  }, []);

  return (
    <MapContainer
      center={[20.5937, 78.9629]}
      zoom={5}
      style={{ height: "80vh", width: "100%" }}
    >
      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {chargers.map((c) => (
        <Marker
          key={c.ID}
          position={[c.AddressInfo.Latitude, c.AddressInfo.Longitude]}
        >
          <Popup>
            <strong>{c.AddressInfo.Title}</strong>
            <br />
            {c.AddressInfo.Town}
            <br />
            <em>Public Charger</em>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}
