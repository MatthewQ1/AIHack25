from letta_client import Letta

# Initialize the Letta client
client = Letta(
    base_url="https://app.letta.com",
    token="sk-let-N2Y3ZGJmZGQtNmM3Zi00ZWE3LTlkODgtYjYzYzJhZDQxMDA0OjY1MjdkYTZmLWIzNTgtNDYzMy05MTM1LTg5NzRjMTg3MTZhNA=="
)

# Replace with your actual agent IDx
agent_id = "agent-78816e6b-e803-40e0-9fb5-29bdf280726c"

input1 = "San Jose, CA. I like driving fast. I like red. I want hybrid sedan."

# Send a message to the agent
response = client.agents.messages.create(
    agent_id=agent_id,
    messages=[
        {"role": "user", "content": "Here is my location and car preferences. Return a list of dealerships near me and a list of suggested cars" + input1}
    ]
)

# Print the assistant's response
for msg in response.messages:
    if msg.message_type == "assistant_message":
        print("Letta:", msg.content)
