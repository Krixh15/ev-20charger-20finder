/**
 * Shared code between client and server
 * Useful to share types between client and server
 * and/or small pure JS functions that can be used on both client and server
 */

/**
 * Example response type for /api/demo
 */
export interface DemoResponse {
  message: string;
}

export interface ChargerLocation {
  ID: number;
  AddressInfo: {
    Latitude: number;
    Longitude: number;
    Title: string;
    Town?: string;
  };
}

export type ChargersResponse = ChargerLocation[];
