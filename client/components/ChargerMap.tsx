import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import { useEffect, useState } from "react";
import L from "leaflet";
import type { ChargerLocation } from "@shared/api";

delete (L.Icon.Default.prototype as { _getIconUrl?: () => string })._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
});

export default function ChargerMap() {
  const [chargers, setChargers] = useState<ChargerLocation[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  useEffect(() => {
    const loadChargers = async () => {
      try {
        setIsLoading(true);
        setErrorMessage(null);
        const response = await fetch("/api/chargers");

        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }

        const data = (await response.json()) as ChargerLocation[];
        setChargers(data);
      } catch (error) {
        console.error("Failed to load chargers:", error);
        setErrorMessage("Unable to load chargers right now.");
      } finally {
        setIsLoading(false);
      }
    };

    void loadChargers();
  }, []);

  return (
    <div className="relative overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
      <div className="absolute left-4 top-4 z-[400] rounded-full bg-white/90 px-4 py-2 text-xs font-semibold text-slate-700 shadow">
        {isLoading && "Loading chargers..."}
        {!isLoading && errorMessage && errorMessage}
        {!isLoading && !errorMessage && `Showing ${chargers.length} chargers`}
      </div>
      <MapContainer
        center={[20.5937, 78.9629]}
        zoom={5}
        style={{ height: "70vh", width: "100%" }}
      >
        <TileLayer
          attribution="&copy; OpenStreetMap contributors"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {chargers.map((charger) => (
          <Marker
            key={charger.ID}
            position={[
              charger.AddressInfo.Latitude,
              charger.AddressInfo.Longitude,
            ]}
          >
            <Popup>
              <strong>{charger.AddressInfo.Title}</strong>
              <br />
              {charger.AddressInfo.Town ?? "Town unavailable"}
              <br />
              <em>Public Charger</em>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}
