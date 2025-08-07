import express from "express"

const app  = express ()

app.get("/", (req, res) => {
    res.send("welcome to the home page!")
})

app.get("/login", (req, res) => {
    res.send("enter your login credentials!")
})
app.get("/purchase", (req, res) => {
    res.send("confirm your purchase")
})

export default app