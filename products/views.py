from django.shortcuts import render, redirect
# from .forms import ImageUploadForm
from .models import Products#, ImageModel
from base64 import b64encode, b64decode
from PIL import Image
from io import BytesIO
import codecs

def compress_image(image):
    # img = Image.open(image)
    # img_io = BytesIO(image).read
    # img.save(img_io, 'JPEG', quality=70)  # Adjust quality as needed
    # img_io.seek(0)
    # return img_io.getvalue()
    file_content = image.read()
    
    # Convert the content to bytes
    bytes_content = BytesIO(file_content).read()
    
    return bytes_content

def handle_uploaded_file(f, i):
    with open(f"tmp{i}.jpeg", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_image(request):
    if request.method == 'POST':
        print()
        if request.FILES and len(request.POST.get("features")) != 0 and len(request.POST.get('name')) != 0:
            productName = request.POST.get('name')
            productImages = request.FILES.getlist('images')
            productFeatures = request.POST.get("features")
            print(productFeatures)
            # ind = 0
            # for i in productImages:
            #     handle_uploaded_file(i, ind)
            #     ind+=1
            # print(productName)
            # print(len(productImages))
            
            image_bytes = []
            for productImage in productImages:
                # print(productImage)
                # print(b''.join(list(productImage.chunks())))
                image_bytes.append(b64encode(b''.join(list(productImage.chunks()))))
            # print(image_bytes)
        
        # for form in form_data:
        #     print(form)
        # if form.is_valid():
        #     image = form.cleaned_data['image']
        #     name = form.cleaned_data['name']
            # image_bytes = b64encode(compress_image(image))  # Convert image to bytes
            # json_str = image_bytes.decode('utf-8')
            # print(len(image_bytes))
            # json_objs = json_str.split('\n')
            product_model = Products()
            # image_model.productId = 1
            product_model.productName = productName
            # if image_model.productImage:
            product_model.productImage.extend(image_bytes)
            product_model.productFeatures = productFeatures
            product_model.save()
            return redirect('image_display')
    return render(request, 'upload.html')

def display_image(request):
    product_model = Products.objects.last()  # Retrieve the last uploaded image
    print(product_model)
    if product_model:
        # print(len(image_model.productImage))
        name = product_model.productName
        print(name)
        images = []
        for image in product_model.productImage:
            images.append(codecs.decode(image, 'ascii'))
        # print(len(images))
        # print(images[0])
        print(product_model.productFeatures)
        features = product_model.productFeatures.split("\\n")
        return render(request, 'display.html', {'image_model': images, 'name':name, 'features':features})
    return render(request, 'display.html', {'image_model':"No Image Available",'name': ""})


# from django.shortcuts import render, redirect
# from .forms import ImageUploadForm
# from .models import ImageModel
# from PIL import Image
# from io import BytesIO

# def compress_image(image):
#     img = Image.open(image)
#     img_io = BytesIO()
#     img.save(img_io, 'JPEG', quality=70)  # Adjust quality as needed
#     img_io.seek(0)
#     return img_io.getvalue()

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             compressed_image_bytes = compress_image(image)
#             image_model = ImageModel(image_bytes=compressed_image_bytes)
#             image_model.save()
#             return redirect('image_display')
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload_image.html', {'form': form})
