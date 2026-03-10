import React, { useRef, useEffect } from "react"

export default function SparkEngine() {
    const canvasRef = useRef<HTMLCanvasElement>(null)

    useEffect(() => {
        const canvas = canvasRef.current
        if (!canvas) return
        const ctx = canvas.getContext("2d") as CanvasRenderingContext2D
        let sparks: any[] = []

        function resize() {
            canvas.width = window.innerWidth
            canvas.height = window.innerHeight
        }
        resize()
        window.addEventListener("resize", resize)

        function createSpark() {
            const x = Math.random() * canvas.width
            const y = Math.random() * canvas.height
            sparks.push({ x, y, r: 1, life: 0, max: 60 + Math.random() * 40 })
        }

        function drawSparks() {
            ctx.clearRect(0, 0, canvas.width, canvas.height)
            for (let i = sparks.length - 1; i >= 0; i--) {
                const s = sparks[i]
                s.life++
                s.r += 0.5

                ctx.beginPath()
                ctx.shadowBlur = 20
                ctx.shadowColor = "#9bd3ff"
                ctx.fillStyle = "#cfefff"
                ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2)
                ctx.fill()

                if (s.life > s.max) sparks.splice(i, 1)
            }
        }

        function loop() {
            if (Math.random() < 0.03) createSpark()
            drawSparks()
            requestAnimationFrame(loop)
        }

        requestAnimationFrame(loop)

        return () => window.removeEventListener("resize", resize)
    }, [])

    return <canvas ref={canvasRef} className="spark-canvas"></canvas>
}
