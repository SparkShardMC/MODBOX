import React from "react"
import AuroraEngine from "../../animations/AuroraEngine"
import SparkEngine from "../../animations/SparkEngine"
import GetStartedButton from "../../components/GetStartedButton"
import FooterLinks from "../../components/FooterLinks"
import "../../styles/landing.css"

export default function LandingPage() {
    return (
        <div className="landing-container">
            <AuroraEngine />
            <SparkEngine />
            <div className="landing-content">
                <h1 className="landing-title">MODBOX</h1>
                <p className="landing-tagline">Build anything, Host anything, Share anything, Enjoy Everything</p>
                <div style={{ height: "128px" }}></div>
                <GetStartedButton />
            </div>
            <FooterLinks />
        </div>
    )
}
