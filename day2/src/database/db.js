import mongoose from "mongoose";

const DBConnect = async () => {
  try {
    const response = await mongoose.connect("mongodb+srv://manjumadlageri765:01091998@cluster0.qtrrmkf.mongodb.net/tempDB");
    console.log("DB Connected Successfully");
  } catch (error) {
    console.error("MongoDB connection error:", error.message);
    throw error; // ✅ Important: rethrow so the caller knows it failed
  }
};

export default DBConnect;
