import React from "react"
import { createRoot } from "react-dom/client"
import LandingPage from "./pages/landing/LandingPage"

const root = createRoot(document.getElementById("root")!)
root.render(<LandingPage />)
