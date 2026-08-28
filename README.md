# Cloud-Based Irrigation System

Design Thinking Lab prototype: soil-moisture-triggered irrigation with a weather-API rain check, built to stop the common failure mode of timer-based irrigation, watering when the soil is already wet or rain is on the way.

## What this repo is

This is the deliverables archive for an RVCE Design Thinking Lab project (AS247DL/ME247DL, Team Hypernova, submitted 10 June 2025), not a source code repo. It holds the report, poster, presentation, and photo/video documentation of the hardware prototype. The ESP32/Arduino firmware and Blynk dashboard configuration described in the report are not included here.

## The idea

A capacitive soil-moisture probe reads the ground. If moisture is below threshold and OpenWeatherMap says no rain in the next 24 hours, a relay switches a pump on. If rain is forecast, the system waits. If the forecast is wrong and moisture keeps dropping past a second, lower threshold, the pump turns on anyway, so a bad forecast can't leave a plant dry. Everything reports to a Blynk dashboard with a manual pump override.

The survey behind this (~70 responses): 85.7% of respondents still water by hand, and 75.4% wanted a semi-automatic system they could still override, not a fully closed loop. That's why the manual switch exists on the dashboard rather than the loop running unattended.

## Hardware

| Component | Role |
|---|---|
| ESP32 / NodeMCU | Controller, Wi-Fi to Blynk and the weather API |
| Capacitive soil probe (FC-28 style) | Moisture sensing |
| Relay module + pump | Actuation |
| OpenWeatherMap API | 24h rain forecast |
| Blynk | Dashboard: moisture, rain probability, pump on/off, temperature, manual override |
| 3D-printed enclosure (SolidWorks) | Houses the probe and electronics, designed to push into soil |

<img src="images/1.png" alt="3D-printed probe housing, red enclosure with electrodes" width="300">

3D-printed housing with the probe electrodes exposed at the bottom.

<img src="images/2.png" alt="Circuit diagram: NodeMCU, relay, soil probe, pump, Blynk and weather API" width="500">

Wiring: NodeMCU/ESP32, relay, FC-28 probe, pump, with Blynk and the weather API on the Wi-Fi side.

## Documentation

- [`docs/DTL Report.pdf`](docs/DTL%20Report.pdf) — full project report
- [`docs/DTL Presentation.pdf`](docs/DTL%20Presentation.pdf) / `.pptx` — presentation deck
- [`docs/DTL Poster.pdf`](docs/DTL%20Poster.pdf) — project poster
- [`videos/Video.mp4`](videos/Video.mp4) — prototype demo

Review photos from project milestones are in `images/review_1.jpg`, `review_2.jpg`, `review_3.jpg`.

## What was tested

The report's target was at least 30% less water than a fixed-schedule timer. Small-scale testing with users and gardeners confirmed water savings, less manual labor, and fewer irrigation cycles ahead of rain, but no single farm-scale percentage was published, so none is claimed here beyond what's in the report.

## Known gap

The firmware (ESP32 sketch) and Blynk app configuration aren't in this repo, only the hardware design, documentation, and photos/video. If you want to reproduce the control logic, the report describes the threshold/forecast/failsafe decision logic in enough detail to reimplement it, but there's no code to pull from here directly.

## Next steps (from the report)

- Mobile-first UI and SMS fallback for feature phones
- Offline/edge decision-making for weak rural connectivity
- NPK and pH sensing alongside moisture
- LoRaWAN/GSM as an alternative to Wi-Fi-only, with solar for off-grid beds

## References

Full write-up: [`irrigation.html`](https://aboutkvs.vercel.app/irrigation.html) on the portfolio site.
