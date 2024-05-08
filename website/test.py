from gradio_client import Client

client = Client("https://1c4465d1074e417428.gradio.live/")
result = client.predict(
		prompt="Hello!!",
		api_name="/predict"
)
print(result)