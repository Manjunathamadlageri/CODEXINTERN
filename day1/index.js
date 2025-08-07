import express from "express"
const app = express () 
const PORT_NUMBER = 4000
app.get("/", (req,res) => {
return res.send("welcome to the Home page!")
})

app.get("/login", (req,res) => {
    return res.send("Please do login!")
})


app.listen(PORT_NUMBER, () => {
    console.log("Server is Running!")
})