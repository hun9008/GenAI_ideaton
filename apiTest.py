import anthropic
from PyPDF2 import PdfReader

def summarize_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = "\n".join([page.extract_text() for page in reader.pages])
    return text

PdfText = "아래 내용을 블로그에 설명하는 방식으로 요약해줘. 블로그에 포스팅할거야. 한글로 설명하고 흥미를 끌 수 있게 글을 작성해봐. 그리고 첫 줄은 전체 내용에 대한 제목을 작성해줘.\n"
Text = summarize_pdf("./DB_08_More_SQL_SUMMARY.pdf")
PdfText += Text
# print(text)

client = anthropic.Anthropic(
    api_key=API_KEY,  # 환경 변수를 설정했다면 생략 가능
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": PdfText}
    ]
)

print(message)
print(message.content)
print("====================================")
print(message.content[0].text)