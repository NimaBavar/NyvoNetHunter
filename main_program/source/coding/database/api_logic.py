from time import sleep
import requests
import json


api_call_url = "https://api.omniinfer.io/v2/txt2img"

inputted_prompt = input("Please enter the prompt you want the AI to generate image from: ")

data = {
    "prompt": inputted_prompt,
    "model_name": "AnythingV5_v5PrtRE.safetensors",
    "sampler_name": "Euler a",
    "batch_size": 1,
    "n_iter": 1,
    "steps": 20,
    "cfg_scale": 7,
    "seed": 3223553976,
    "height": 512,
    "width": 512
}

api_key_header = {
    "key": "bd4d3fc6-e8a3-4363-b4a7-9e58f39528d3"
}
serialized_data = json.dumps(data)


call_response = requests.post(url=api_call_url, data=serialized_data, headers=api_key_header)
task_id = call_response.json()
print(task_id)

progress_data = {
    "task_id": task_id
}

api_progress_url = f"https://api.omniinfer.io/v2/progress?task_id={task_id}"


sleep(20)
progress_response = requests.get(url=api_progress_url, data=progress_data)

image_url = ''.join(progress_response.json()["data"]["imgs"])

image_response = requests.get(image_url)


sleep(3)
with open("result.png", "wb") as image_file_object:
    image_file_object.write(image_response.content)