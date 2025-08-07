// src/app.js
import express from "express";

const app = express();

// Define your routes
app.get("/", (req, res) => {
  res.send("Welcome to the home page");
});

app.get("/login", (req, res) => {
  res.send("Enter your login credentials");
});

app.get("/purchase", (req, res) => {
  res.send("Confirm your purchase");
});

export default app;
