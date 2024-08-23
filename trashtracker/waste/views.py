from django.shortcuts import render, redirect
from .models import WasteImage
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST' and request.FILES['wasteImage']:
        waste_image = request.FILES['wasteImage']
        fs = FileSystemStorage()
        filename = fs.save(waste_image.name, waste_image)
        uploaded_file_url = fs.url(filename)

        # Here you would process the image using your ML model
        # For now, we will simulate the result
        plastic_percentage = 40.0
        metal_percentage = 30.0
        # Add logic for other waste types

        # Save the result to the database
        WasteImage.objects.create(
            image=waste_image,
            plastic_percentage=plastic_percentage,
            metal_percentage=metal_percentage,
            # Add other percentages
        )

        return render(request, 'results.html', {
            'uploaded_file_url': uploaded_file_url,
            'plastic_percentage': plastic_percentage,
            'metal_percentage': metal_percentage,
            # Pass other percentages
        })
    return render(request, 'upload.html')

def results(request):
    # Logic to display results
    return render(request, 'results.html')
