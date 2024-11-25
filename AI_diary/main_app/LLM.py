from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"]="YOUR_API_KEY"

def generate_prompt(where=None, what=None, feeling=None, gender=None, hair=None):
    # template 정의
    template = """
    Stable Diffusion 모델을 활용하여 어린이의 그림일기에 삽입할 이미지 생성을 위한 프롬프트를 작성할 거야.
    사용자 외형 특징은 헤어스타일, 성별의 2가지 요소를 사용하여 인물의 프롬프트를 작성하고, 배경 및 사건 요소는 "어디서", "무엇을", 그리고 그 기분은 "어땠는지"를 바탕으로 설정할 거야.

    Stable Diffusion 프롬프트 작성은 기본적으로 다음과 같은 구조를 따르며, 각 요소를 명확하고 구체적으로 기술해야 해:
    - 주제 (Subject): 이미지의 주요 객체나 인물을 명확히 설명
    - 세부사항 (Details): 행동, 사건, 감정 등 이미지의 중요 요소 설명
    - 배경 (Background): 환경 및 위치 설명
    - 스타일 및 환경 (Style & Quality): 예술적 스타일과 이미지의 퀄리티 요소
    - 키워드는 and 및 쉼표(,)로 구분된 키워드가 20개를 넘어서는 안 돼.

    사용자 외형 특징: 헤어스타일: {hair}, 성별: {gender}
    어디서: {where}, 무엇을: {what}, 어땠는지: {feeling}

    프롬프트:
    """

    # PromptTemplate 생성
    prompt_template = PromptTemplate.from_template(template)

    # 기본값 설정
    hair = hair or "medium hair"
    gender = gender or "female"
    where = where or input("어디서 했나요? : ")
    what = what or input("무엇을 했나요? : ")
    feeling = feeling or input("어땠나요? : ")

    # LangChain 모델 초기화
    model = ChatOpenAI(model="gpt-4", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))

    # 프롬프트 생성
    sdprompt = prompt_template.format(hair=hair, gender=gender, where=where, what=what, feeling=feeling)

    # ChatGPT API 호출 (LangChain 방식)
    response = model.predict_messages([HumanMessage(content=sdprompt)])

    # Stable Diffusion 프롬프트와 한국어 일기 작성
    diary_prompt = f"""
    아래의 Stable Diffusion 프롬프트를 기반으로, 어린이가 직접 작성한 것처럼 자연스러운 일기 내용을 한국어로 작성해줘.
    내용을 최소 3문장 이상으로 길게 작성해줘.
    프롬프트: {sdprompt}

    작성된 일기:
    """

    diary_response = model.predict_messages([HumanMessage(content=diary_prompt)])
    return diary_response.content
