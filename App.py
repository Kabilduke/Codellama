import requests
import json
import gradio as gr


url = "http://localhost:11434/api/generate"

 
headers = {
  'content-type' :'application/json'
 }

history = []

def  generate_code(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data={
        'model': 'azuna',
        'prompt': final_prompt,
        'stream' : False
    }

    response = requests.post(url,headers = headers, data = json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("Error:", response.text)


Interface = gr.Interface(
    fn = generate_code,
    inputs= gr.Textbox(lines=5, placeholder="Enter the prompt here."),
    outputs= "text"
)
Interface.launch(share=True)
