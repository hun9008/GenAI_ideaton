import anthropic
from PyPDF2 import PdfReader

def summarize_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = "\n".join([page.extract_text() for page in reader.pages])
    return text

# PdfText = "아래 내용을 블로그에 설명하는 방식으로 요약해줘. 블로그에 포스팅할거야. 한글로 설명하고 흥미를 끌 수 있게 글을 작성해봐. 그리고 첫 줄은 전체 내용에 대한 제목을 작성해줘.\n"
PreText = "이렇게 주간일기 기록을 진행하면서 뭔가 한 주간 내 생활을 되돌아볼 수 있기도 하고 기록을 읽어주시는분들께서 재미진다고도 해주셔서 더 즐겁고 행복하게 기록하게 되는것 같아요. 이번주 블챌 주간일기 챌린지 기록도바로 시작해볼게욧! ♥♡"
MainText = "아래 내용을 위의 글씨체로 작성해줘. 나의 일상을 소개하는 블로그를 작성할거야. 한글로 작성해줘. 내용은 아래와 같아.\n"
Text = summarize_pdf("./DB_08_More_SQL_SUMMARY.pdf")

daily = "안녕하세요. 오늘은 2024년 5월 21일 화요일입니다. 오늘 하루 일과는 다음과 같습니다.\n7시 기상 후 스트레칭과 가벼운 운동으로 하루를 시작했습니다. 건강한 아침식사를 위해 요구르트, 과일, 그래놀라를 먹었습니다. 9시부터 회사에서 프로젝트 회의가 있었습니다. 새로운 기능 개발 계획을 논의하고 업무를 분담했습니다. 점심시간에는 동료들과 근처 식당에서 맛있는 멕시코 요리를 먹었습니다. 오후에는 프로그래밍 작업에 집중했습니다. 버그 수정과 코드 최적화 작업을 했고, 테스트도 진행했습니다. 잠시 휴식을 취하고 저녁 무렵 퇴근했습니다. 집에 돌아와 간단한 저녁 식사를 한 후, 책을 읽으며 여가시간을 가졌습니다. 오늘 하루는 생산적이고 알차게 보냈습니다. 내일은 더 열심히 일하고 운동도 하려고 합니다. ===== 오늘의 소감 ===== 바쁜 하루 일정이었지만 균형 잡힌 생활을 할 수 있어서 만족스러웠습니다. 프로젝트 진척도 잘 되고 있어 기분이 좋습니다. 앞으로도 열심히 하는 삶을 살아가야겠습니다."
PdfText = PreText + "\n" + MainText + "\n" + Text + "\n" + daily
# print(text)

client = anthropic.Anthropic(
    api_key="API_KEY", 
     # 환경 변수를 설정했다면 생략 가능
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

# print(message)
# print(message.content)
print("====================================")
print(message.content[0].text)