# Text Classification API (ONNX + FastAPI + Docker)

A production-ready NLP text classification API built with:

* **FastAPI** for high-performance REST API
* **ONNX Runtime** for optimized inference
* **Docker** for containerization
* **Model versioning** support
* **Health check monitoring**
* Designed for cloud deployment (Cloud Run, Render, etc.)

---

## 🚀 Overview
This is a repository created for the development and deployment of Besafe1.0.00
It contains a scalable text classification model service that:

* Accepts raw **text input**
* Converts text → tokenized sequence
* Runs inference using an **ONNX model**
* Returns prediction + confidence score
* Supports **model versioning**
* Includes a **health check endpoint** for production monitoring

The model was originally trained using TensorFlow/Keras and converted to ONNX for efficient deployment.

---

# 🧠 How It Works

```
User Text
   ↓
Tokenizer
   ↓
Integer Sequence
   ↓
Padding
   ↓
ONNX Runtime Inference
   ↓
Prediction + Confidence
```

---

#  Features

✅ ONNX optimized inference
✅ Model versioning via environment variables
✅ Health check endpoint
✅ Input validation with Pydantic
✅ Docker-ready
✅ Cloud-ready

---

# 🔒 Production Considerations

Recommended next steps:

* Add structured logging
* Add request rate limiting
* Add authentication
* Add CI/CD pipeline
* Add monitoring (Prometheus/Grafana)
* Store models in cloud storage instead of local disk

---
#  Future Improvements

* Multi-class classification support
* HuggingFace transformer ONNX pipeline
* Batch inference endpoint
* Async inference
* Model metadata endpoint (`/info`)
* A/B testing between model versions

---

# 🧑‍💻 Author

Built as part of an AI Engineering production deployment pipeline.

---

# 📜 License

MIT License

---


This repository demonstrates:

* Practical ML system design
* Production deployment mindset
* Scalable model serving
* Clean API architecture

---

# 🧠 Final Notes

This project represents a real-world machine learning deployment pipeline.
It is structured to reflect how ML services are built in industry environments.

If you found this useful, consider starring the repository 

---
