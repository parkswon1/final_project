from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product
from signapp.models_bookmark import FBookmark
from datetime import date

@require_POST
def like_button_view(request):
    # POST 요청에서 필요한 데이터를 가져옵니다.
    fno = request.POST.get('fno')
    customer = request.user

    product = Product.objects.get(prdlstReportNo=fno)
    title = product.prdlstNm

    # 현재 사용자와 제품에 대한 북마크가 이미 존재하는지 확인합니다.
    existing_bookmark = FBookmark.objects.filter(CNO=customer, FNO=product).first()

    if existing_bookmark:
        # 북마크가 이미 존재하는 경우, 북마크를 삭제하여 해제합니다.
        existing_bookmark.delete()
        return JsonResponse({'message': '찜해재했습니다.'})
    else:
        # 새로운 북마크를 생성합니다.
        bookmark = FBookmark.objects.create(
            TITLE=title,
            FNO=product,
            CNO=customer,
            CDATE=date.today()
        )
        return JsonResponse({'message': '찜했습니다.'})