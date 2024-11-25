from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from diffusers import StableDiffusionPipeline
import torch
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from diffusers import StableDiffusionPipeline
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Diary
from .LLM import generate_prompt  # 프롬프트 생성 메서드




# # Stable Diffusion 모델 초기화
# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
# pipe.to("cpu")  # CPU 사용 (CUDA 사용 가능하면 "cuda"로 변경)

# def generate_image(prompt):
#     try:
#         print(f"이미지 생성 프롬프트: {prompt}")
#         # Stable Diffusion 이미지 생성
#         image = pipe(prompt).images[0]
#         output_path = os.path.join(settings.MEDIA_ROOT, "generated_image.png")
#         image.save(output_path)
#         print(f"이미지 저장 경로: {output_path}")
#         return os.path.join(settings.MEDIA_URL, "generated_image.png")
#     except Exception as e:
#         print(f"이미지 생성 실패: {str(e)}")
#         raise RuntimeError(f"이미지 생성 중 오류: {str(e)}")




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DiaryEntry
from .LLM import generate_prompt  # generate_prompt 함수가 있는 모듈을 임포트합니다.


def create_diary(request):
    if request.method == 'POST':
        return redirect('generate_prompt')
    return render(request, 'create_diary.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def prompt_view(request):
    if request.method == 'POST':
        # POST 요청으로부터 데이터를 받아옵니다.
        where = request.POST.get('where')
        what = request.POST.get('what')
        feeling = request.POST.get('feeling')
        gender = request.POST.get('gender')
        hair = request.POST.get('hair')

        # generate_prompt 함수를 호출하여 프롬프트를 생성합니다.
        try:
            prompt = generate_prompt(where, what, feeling, gender, hair)
            return JsonResponse({'prompt': prompt})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'prompt_form.html')

def result_page(request):
    prompt = request.GET.get('prompt', '프롬프트가 없습니다.')
    return render(request, 'result.html', {'prompt': prompt})





def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')
        
        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)
        UserProfile.objects.create(user=user, user_identifier=username, email=email)
        messages.success(request, 'Signup successful!')
        return redirect('login')
    
    return render(request, 'signup.html')



def user_login(request):  # 이름을 login_view 또는 user_login으로 변경
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 사용자 세션 시작
            messages.success(request, 'Login successful!')
            return redirect('home')  # 로그인 성공 후 리디렉션
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')  # 로그인 실패 후 다시 로그인 페이지로 리디렉션

    return render(request, 'login.html')

def user_logout(request):
    logout(request)  # 사용자 세션 종료
    return redirect('home')  # 로그아웃 후 홈으로 리디렉션

def about_us(request):
    return render(request, 'about-us.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def create_diary(request):
    return render(request, 'create-diary.html')

def emotion_tracking(request):
    return render(request, 'emotion-tracking.html')

def faq(request):
    return render(request, 'faq.html')

def gallery(request):
    return render(request, 'gallery.html')

def greet(request):
    return render(request, 'greet.html')

def how_it_works(request):
    return render(request, 'how-it-works.html')

model = None



# def initialize_model():
#     """
#     Stable Diffusion 모델 초기화 함수.
#     """
#     global model
#     if model is None:
#         model_path = settings.STABLE_DIFFUSION_MODEL_PATH
#         model = StableDiffusionPipeline.from_pretrained(
#             model_path, torch_dtype=torch.float16
#         )
#         model.to(settings.DEVICE)

# def generate_image(request):
#     """
#     텍스트에서 이미지를 생성하는 뷰.
#     """
#     if request.method == "POST":
#         prompt = request.POST.get("prompt")
#         initialize_model()  # 모델 초기화
#         generated_image = model(prompt).images[0]
        
#         # 이미지 저장
#         image_dir = "media/generated_images/"
#         os.makedirs(image_dir, exist_ok=True)
#         image_path = os.path.join(image_dir, f"{prompt.replace(' ', '_')}.png")
#         generated_image.save(image_path)

#         return render(request, "generate_image.html", {"image_path": image_path})
    
#     return render(request, "generate_image.html")

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import DiaryEntry
# from django.http import HttpResponse

# # 일기 생성
# def create_diary(request):
#     if request.method == 'POST':
#         text = request.POST.get('entry_text')
#         emotion = request.POST.get('emotion')
#         DiaryEntry.objects.create(entry_text=text, emotion=emotion)
#         return redirect('diary_list')
#     return render(request, 'create_diary.html')

# # 일기 목록 조회
# def diary_list(request):
#     diaries = DiaryEntry.objects.all()
#     return render(request, 'diary_list.html', {'diaries': diaries})

# # 일기 상세 조회
# def diary_detail(request, entry_id):
#     diary = get_object_or_404(DiaryEntry, id=entry_id)
#     return render(request, 'diary_detail.html', {'diary': diary})

# # 일기 수정
# def update_diary(request, entry_id):
#     diary = get_object_or_404(DiaryEntry, id=entry_id)
#     if request.method == 'POST':
#         diary.entry_text = request.POST.get('entry_text')
#         diary.emotion = request.POST.get('emotion')
#         diary.save()
#         return redirect('diary_detail', entry_id=entry_id)
#     return render(request, 'update_diary.html', {'diary': diary})

# # 일기 삭제
# def delete_diary(request, entry_id):
#     diary = get_object_or_404(DiaryEntry, id=entry_id)
#     if request.method == 'POST':
#         diary.delete()
#         return redirect('diary_list')
#     return render(request, 'delete_diary.html', {'diary': diary})
