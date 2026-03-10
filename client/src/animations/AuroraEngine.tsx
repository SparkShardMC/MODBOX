import React, { useRef, useEffect } from "react"

export default function AuroraEngine() {
    const canvasRef = useRef<HTMLCanvasElement>(null)

    useEffect(() => {
        const canvas = canvasRef.current
        if (!canvas) return
        const ctx = canvas.getContext("2d") as CanvasRenderingContext2D

        function resize() {
            canvas.width = window.innerWidth
            canvas.height = window.innerHeight
        }
        resize()
        window.addEventListener("resize", resize)

        function draw(time: number) {
            const g = ctx.createLinearGradient(0, 0, canvas.width, canvas.height)
            const shift = Math.sin(time * 0.0002) * 200
            g.addColorStop(0, `rgb(${20 + shift / 10},${30 + shift / 5},80)`)
            g.addColorStop(1, `rgb(${80 + shift / 5},${140 + shift / 4},255)`)
            ctx.fillStyle = g
            ctx.fillRect(0, 0, canvas.width, canvas.height)
            requestAnimationFrame(draw)
        }

        requestAnimationFrame(draw)

        return () => window.removeEventListener("resize", resize)
    }, [])

    return <canvas ref={canvasRef} className="aurora-canvas"></canvas>
}
