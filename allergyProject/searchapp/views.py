from django.shortcuts import render
from .models import Product
from .models import UserData
from .models import PSimilarity
from .models import Allergy
from signapp.models import Customer
from django.db.models import Q
from django.core.cache import cache

# filter 함수의 Q함수: OR조건으로 데이터를 조회하기 위해 사용하는 함수
# objects.filter() 는 특정 조건에 해당하면 객체 출력 .get('kw') 은 kw만 반환
# __icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사. 사용법 "필드명"__icontains = 조건값

def filtering(products, list, query):
    if list != []:
        for i in list:
            products = products.filter(
                    (Q(prdlstNm__icontains=query) |
                    Q(prdkind__icontains=query)) &
                    ~Q(allergy__icontains=i)
                )
            list.remove(i)
            return filtering(products, list, query)
    return products


def CheckAll(user):
    allergies = []

    user_allerinfo = Customer.objects.get(
        username = user.username
    ).allerinfo
    allerinfo_list = [int(item) for item in user_allerinfo.strip('[]').split(', ')]

    for ano in allerinfo_list:
        allergy = Allergy.objects.all().get(
            Q(ano__exact = ano)
        ).allergy
        allergies.append(allergy)
    
    return allergies


# cache 적용 사례 #
def searchResult(request):
    user = request.user
    allergies = []
    
    if user.is_anonymous:
        if request.GET.get('afilter'):
            cache_key = request.GET.get('kw') + request.GET.get('afilter')
        else:
            cache_key = request.GET.get('kw')
    else:
        allergies = CheckAll(user)
        allergies_str = ' '.join(allergies)

        if request.GET.get('afilter'):
            cache_key = request.GET.get('kw') + request.GET.get('afilter') + allergies_str
        else:
            cache_key = request.GET.get('kw') + allergies_str
    products = cache.get(cache_key, None)

    if not products:
        # global query
        if ('kw' in request.GET):
            if ('afilter' in request.GET):
                query = request.GET.get('kw')
                afilter = request.GET.getlist('afilter')
                list = afilter.copy() + allergies
                products = Product.objects.all().order_by('prdlstNm')
                products = filtering(products, list, query)[:1000]
                cache.set(cache_key, products, 60*60)
                return render(request, 'search.html', {'query':query, 'afilter':afilter, 'products':products} )
        
            else:
                query = request.GET.get('kw')
                products = Product.objects.all().order_by('prdlstNm')
                products = filtering(products, allergies, query)[:1000]
                cache.set(cache_key, products, 60*60)
                return render(request, 'search.html', {'query':query, 'products':products} )

    return render(request, 'search.html', {'products':products})


def Detail(request):
    if ('pk' in request.GET):
        pk = request.GET.get('pk')
        detail = Product.objects.all()
        detail = detail.get(
            Q(prdlstReportNo__exact=pk)
        )

    try:
        user=UserData.objects.all().filter(
            Q(prdlstReportNo__exact=pk)
        )
    except UserData.DoesNotExist:
        user=UserData()
        user.gender='남성'
        user.older=25
        user.allergy='난류'
        user.prdlstNm=detail.prdlstNm
        user.rating=3
        user.prdlstReportNo=detail.prdlstReportNo
        user.save()

    similarities = Similarity(request)

    try:
        return render(request, 'detail.html', {'pk':pk, 'detail':detail, 'similarities':similarities[:6]})
    except Exception as ex:
        print(ex)
        return render(request, 'detail.html', {'pk':pk, 'detail':detail})


def Similarity(request):
    similarities = []

    if ('pk' in request.GET):
        pk = request.GET.get('pk')
        sim = PSimilarity.objects.all().order_by('prdNo')
        # SELECT simlist FROM similarity WHERE prdNo=pk;
        sim_list = sim.filter(
            Q(prdNo__exact=pk)
        ).get().simlist

        for sim_no in sim_list:
            similarity = Product.objects.all()
            similarity = similarity.get(
                Q(prdlstReportNo__exact = sim_no)
            )
            similarities.append(similarity)

    return similarities