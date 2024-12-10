from diffusers import StableDiffusionPipeline
from flask import Flask, request, jsonify
import torch

# Load the Stable Diffusion model
device = "cuda" if torch.cuda.is_available() else "cpu"
pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipeline.to(device)

# Flask App
app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "A serene sunset over a mountain range")
    
    # Generate an image
    image = pipeline(prompt).images[0]
    image_path = f"generated_image.png"
    image.save(image_path)
    
    return jsonify({"prompt": prompt, "image_path": image_path})

if __name__ == "__main__":
    app.run(debug=True)
