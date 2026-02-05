import ChargerMap from "@/components/ChargerMap";

export default function Index() {
  return (
    <div className="min-h-screen bg-slate-50">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex w-full max-w-6xl flex-col gap-4 px-6 py-8 md:flex-row md:items-center md:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
              EV ChargeShare
            </p>
            <h1 className="mt-2 text-3xl font-semibold text-slate-900">
              Find nearby chargers across India
            </h1>
            <p className="mt-3 max-w-2xl text-sm text-slate-600">
              Explore public EV charging locations powered by Open Charge Map.
              Zoom in to discover stations and tap markers for details.
            </p>
          </div>
          <div className="rounded-2xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-600 shadow-sm">
            <p className="font-semibold text-slate-700">Tips</p>
            <ul className="mt-2 list-disc space-y-1 pl-4">
              <li>Use the scroll wheel to zoom into a city.</li>
              <li>Tap a marker to view charger details.</li>
              <li>Data refreshes from the server API.</li>
            </ul>
          </div>
        </div>
      </header>
      <main className="mx-auto w-full max-w-6xl px-6 py-10">
        <ChargerMap />
        <div className="mt-8 grid gap-6 md:grid-cols-3">
          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
            <h2 className="text-base font-semibold text-slate-900">
              Faster discovery
            </h2>
            <p className="mt-2 text-sm text-slate-600">
              Pulls charger data from the backend so you can add caching,
              filtering, or API keys without exposing them in the browser.
            </p>
          </div>
          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
            <h2 className="text-base font-semibold text-slate-900">
              Driver friendly
            </h2>
            <p className="mt-2 text-sm text-slate-600">
              Pinpoint stations with clear markers, then enrich them with
              pricing or availability later.
            </p>
          </div>
          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
            <h2 className="text-base font-semibold text-slate-900">
              Ready for growth
            </h2>
            <p className="mt-2 text-sm text-slate-600">
              Add filters, user accounts, or bookings as the platform expands.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
}
