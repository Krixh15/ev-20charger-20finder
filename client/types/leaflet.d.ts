declare module "leaflet" {
  export type LatLngExpression =
    | [number, number]
    | {
        lat: number;
        lng: number;
      };

  export type LatLngBoundsExpression = [LatLngExpression, LatLngExpression];

  export interface FitBoundsOptions {
    padding?: [number, number];
  }

  export interface MapOptions {
    center?: LatLngExpression;
    zoom?: number;
  }

  export interface TileLayerOptions {
    attribution?: string;
  }

  export class Map {}
  export class TileLayer {}

  const L: {
    Icon: {
      Default: {
        prototype: {
          _getIconUrl?: () => string;
        };
        mergeOptions: (options: Record<string, string>) => void;
      };
    };
  };

  export default L;
}
