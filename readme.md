# Alog (Auto-blog)

Alog는 AI를 활용한 자동 블로그 포스팅 서비스입니다. 사용자가 업로드한 PDF 파일의 내용을 AI가 요약하여 블로그 포스트를 자동으로 생성합니다.

## Motivation

블로그는 일상 기록, 학습 내용 정리, 여행 경험 공유 등 다양한 목적으로 널리 사용되고 있습니다. 하지만 한 포스트를 작성하는 데 평균 3-4시간이 소요되는 등 시간이 많이 걸리는 것이 단점입니다. Alog는 이러한 문제를 해결하고자 합니다.

Alog의 이름은 'Auto-Blog'의 약자이자, 'AI'와 'log'의 조합으로, AI 기술을 활용해 더 나은 블로그 플랫폼을 제공하겠다는 의미를 담고 있습니다.

## Main Function

- PDF 파일 업로드 및 텍스트 추출
- Claude AI API를 활용한 내용 요약
- 사용자 맞춤형 블로그 포스트 자동 생성
- 생성된 포스트 편집 및 게시
- 다양한 블로그 테마 제공

## Difference

1. 기존 내용 요약: 새로운 내용을 생성하는 것이 아니라, 사용자가 작성한 내용을 요약하고 정리합니다.
2. 사용자 말투 반영: AI가 요약한 내용을 사용자의 말투로 변환하여 자연스러운 포스팅을 만듭니다.
3. 낮은 진입 장벽: 웹 프로그래밍 지식 없이도 쉽게 사용할 수 있습니다.
4. 다양한 테마: 사용자의 취향에 맞는 다양한 블로그 테마를 제공합니다.

## Tech Stack

- Frontend: React, Flutter, JavaScript, TailwindCSS
- Backend: FastAPI, Spring
- Database: MongoDB, MySQL
- AI: Claude API
- Deployment: AWS (S3, CloudFront, EC2, Route53)

## Team Member

- Frontend: 김평주, 한도연
- Backend: 정용훈, 남현원

## Dev Schedule

- 2024.06.02 ~ 2024.06.09: 개발 환경 구축 및 요구사항 정의
- 2024.06.24 ~ 2024.06.30: 로그인 및 회원가입 기능 개발
- 2024.07.01 ~ 2024.07.07: 메인 페이지 및 사용자 관련 기능 개발
- 2024.07.08 ~ 2024.07.14: 블로그 게시 및 작성 기능 개발
- 2024.07.15 ~ 2024.07.17: 최종 테스트 및 버그 수정

## Business Model

1. 판매형: 블로그 스킨/테마 판매
2. 구독형: 프리미엄 기능 제공 (다양한 AI 모델 선택, 긴 입력 소스 지원 등)
3. 제휴형: 기존 블로그 플랫폼과의 제휴를 통한 수익 창출

## Reference

- [매경이코노미 - 2030세대가 반한 블로그 열풍](https://www.mk.co.kr/economy/view.php?sc=50000001&year=2021&no=523652)
- [서울시립대신문 - 블로그의 귀환](http://press.uos.ac.kr/news/articleView.html?idxno=13493)
- [Orbit Media Studios - 2023 Blogging Statistics](https://www.orbitmedia.com/blog/blogging-statistics/)