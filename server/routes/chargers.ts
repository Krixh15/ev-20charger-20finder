import { RequestHandler } from "express";
import { ChargersResponse } from "@shared/api";
import { OPENCHARGE_API_KEY, OPENCHARGE_COUNTRY, OPENCHARGE_MAX_RESULTS } from "../config/keys";

const OPEN_CHARGE_BASE_URL = "https://api.openchargemap.io/v3/poi/";
const CACHE_TTL_MS = 5 * 60 * 1000;
let cachedResponse: ChargersResponse | null = null;
let cacheTimestamp = 0;

export const handleChargers: RequestHandler = async (_req, res) => {
  try {
    const now = Date.now();
    if (cachedResponse && now - cacheTimestamp < CACHE_TTL_MS) {
      return res.status(200).json(cachedResponse);
    }

    const url = new URL(OPEN_CHARGE_BASE_URL);
    url.searchParams.set("output", "json");
    url.searchParams.set("countrycode", OPENCHARGE_COUNTRY);
    url.searchParams.set(
      "maxresults",
      OPENCHARGE_MAX_RESULTS
    );

    if (OPENCHARGE_API_KEY) {
      url.searchParams.set("key", OPENCHARGE_API_KEY);
    }

    const response = await fetch(url);

    if (!response.ok) {
      return res.status(response.status).json({
        error: "Unable to fetch charger data",
      });
    }

    const data = (await response.json()) as ChargersResponse;
    cachedResponse = data;
    cacheTimestamp = now;
    return res.status(200).json(data);
  } catch (error) {
    console.error("OpenChargeMap request failed:", error);
    return res.status(500).json({ error: "Unexpected server error" });
  }
};
