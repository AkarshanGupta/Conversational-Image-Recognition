import gradio as gr
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP model and processor
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def get_image_description(image, text_query):
    # Process the image
    inputs = blip_processor(images=image, return_tensors="pt")

    # Generate a description using BLIP
    outputs = blip_model.generate(**inputs)
    description = blip_processor.decode(outputs[0], skip_special_tokens=True)

    # Return the generated description
    return description


# Create Gradio interface
iface = gr.Interface(
    fn=get_image_description,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(lines=2, placeholder="Enter your query about the image...")
    ],
    outputs="text",
    title="Image and Text Interaction",
    description="Upload an image and enter a query to get a description of the image."
)

# Launch the interface
iface.launch()

