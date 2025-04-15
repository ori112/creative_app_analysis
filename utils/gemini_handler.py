import google.generativeai as genai
from PIL import Image

def analyze_creatives(csv_file, image_files, api_key):
    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25", # or any other model you would like to use
    system_instruction="""
you are an experienced marketing data analyst with 5 years of experience
you are spcialized in data analysis, you have a sharp eye for creatives and specialize in creative factor analysis
you answer briefly and in a clear manner without to much content, concusions, insights and bottom lines
"""
)

    # Build contents list for prompt
    contents = []

    for i, img_file in enumerate(image_files):
        image = Image.open(img_file)
        caption = f"Creative ID: {i+1}"
        contents.extend([image, caption])

    # Append the CSV content
    csv_data = csv_file.read().decode("utf-8")
    contents.append(f"""
{csv_data}
TASK: Analyze the dataset and the creatives
analyze the creative elements (visuals, text, CTA, layout, etc.)
analyse the data provided
tell me which is the best creative the reason and most important creative elements
explain your reasoning
think step by step
""")

    # Generate content
    response = model.generate_content(contents)
    return response.text
