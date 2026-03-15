from dotenv import load_dotenv
from openai import OpenAI

# 환경변수 로드 및 클라이언트 생성
load_dotenv()
client = OpenAI()

# Chat Completions API 호출
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "당신은 친절하고 간단하게 설명하는 AI 비서입니다."},
        {"role": "user", "content": "Chat Completions API가 뭐야?"}
    ]
)

print(response.choices[0].message.content)