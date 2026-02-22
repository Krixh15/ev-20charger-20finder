# ⚡ EV ChargeShare  
A Community-Driven Platform for Smart Electric Vehicle Charging Access  

## 📌 Overview
EV ChargeShare is a decentralized, community-powered EV charging platform that allows private charger owners to share their chargers with nearby EV drivers.

The platform provides:
- Map-based charger discovery
- Real-time availability tracking
- Secure authentication
- Time-slot booking system
- Atomic conflict resolution algorithm to prevent double booking

This system improves charger utilization, reduces waiting time, and promotes sustainable electric mobility.

---

## 🚀 Problem Statement
Despite increasing EV adoption, users face:

- Limited public charging stations  
- Long waiting times  
- Uneven charger distribution  
- Underutilized private chargers  
- Double booking issues during peak demand  

EV ChargeShare solves this using a decentralized sharing model with a robust booking algorithm.

---

## 🧠 Key Features

- 🔐 Secure User Authentication (Host & Driver roles)
- 🗺 Map-Based Charger Discovery (OpenStreetMap + Leaflet)
- ⚡ Real-Time Charger Availability
- 📅 Time-Based Slot Booking
- 🛡 Booking Conflict Resolution (Atomic FCFS Algorithm)
- 📈 Scalable 3-Tier Architecture

---

## 🏗 System Architecture

### Three-Tier Architecture

1. **Presentation Layer**
   - React + Vite
   - Tailwind CSS
   - Map UI

2. **Application Layer**
   - Django Backend
   - REST APIs
   - Booking Logic
   - Conflict Resolution

3. **Data Layer**
   - SQLite (Development)
   - PostgreSQL (Production)

---

## ⚙️ Booking Conflict Resolution Algorithm

To prevent double booking:

- Each request is treated as a transaction
- Slot is temporarily locked
- Availability is verified
- First valid request is confirmed
- Others are rejected or rescheduled
- Lock released after completion

This ensures:
- Fairness
- Database consistency
- No race conditions
- High-traffic reliability

---

## 🛠 Technology Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Leaflet

### Backend
- Django
- REST APIs

### Database
- SQLite
- PostgreSQL

### Tools
- Git
- GitHub
- VS Code

---

## 🌍 External APIs Used

- OpenStreetMap / Leaflet API
- Browser Geolocation API

---

## 📊 Results

- Eliminated double booking issues
- Improved charger utilization
- Reduced range anxiety
- Scalable architecture ready for expansion

---

## 🔮 Future Enhancements

- AI-based demand prediction
- Dynamic pricing
- Mobile application
- Government EV integration

---

## 👨‍💻 Author

**Krish Kumar**  
BCA – Amity University, Ranchi  
AIIT Department  

---

## 📜 License
This project is for academic and research purposes.
